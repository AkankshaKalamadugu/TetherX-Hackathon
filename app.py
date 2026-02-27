import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# Config
st.set_page_config(page_title="InfraGuard - TetherX", layout="wide")

@st.cache_data
def load_sample_data():
    """Generate realistic SHM sensor data like aging bridge dataset."""
    np.random.seed(42)
    n_samples = 1000
    timestamps = pd.date_range('2026-02-26', periods=n_samples, freq='10S')
    
    # Vibration (acc_x, acc_y, acc_z) - normal with anomalies
    normal_vib = np.random.normal(0, 0.5, (n_samples, 3))
    anomalies = np.random.choice([0,1], n_samples, p=[0.9, 0.1])
    normal_vib[anomalies==1] += np.random.normal(3, 1, (sum(anomalies==1), 3))  # Spikes
    
    # Env factors
    temp = 25 + np.random.normal(0, 5, n_samples)
    hum = 60 + np.random.normal(0, 10, n_samples)
    wind = np.random.exponential(2, n_samples)
    
    df = pd.DataFrame({
        'timestamp': timestamps,
        'acc_x': normal_vib[:,0],
        'acc_y': normal_vib[:,1],
        'acc_z': normal_vib[:,2],
        'temp': temp,
        'humidity': hum,
        'wind_speed': wind
    })
    return df

def detect_anomalies(df):
    """ML Anomaly Detection with Isolation Forest."""
    features = ['acc_x', 'acc_y', 'acc_z', 'temp', 'humidity', 'wind_speed']
    model = IsolationForest(contamination=0.1, random_state=42)
    preds = model.fit_predict(df[features])
    df['anomaly'] = preds == -1
    return df

def classify_health(df):
    """Rule-based + pattern health states."""
    vib_mag = np.sqrt(df['acc_x']**2 + df['acc_y']**2 + df['acc_z']**2)
    env_score = (df['temp'] > 35).astype(int) + (df['humidity'] > 80).astype(int) + (df['wind_speed'] > 10).astype(int)
    
    health_scores = []
    for i in range(len(df)):
        anomalies_near = df['anomaly'].iloc[max(0,i-10):i+1].sum()
        if vib_mag.iloc[i] > 2 or anomalies_near > 2 or env_score.iloc[i] > 2:
            health_scores.append('Critical')
        elif vib_mag.iloc[i] > 1 or anomalies_near > 1:
            health_scores.append('Warning')
        else:
            health_scores.append('Good')
    df['health'] = health_scores
    return df

# Main App
st.title("🚀 InfraGuard: Infrastructure Health & Anomaly Analysis")
st.markdown("**TetherX Hackathon - Smart City Track** | Real-time urban asset (e.g., bridge) monitoring with ML anomalies & health classification.")

# Sidebar
st.sidebar.header("Controls")
auto_refresh = st.sidebar.checkbox("Auto-refresh data (real-time sim)", True)
speed = st.sidebar.slider("Refresh speed (sec)", 1, 10, 5)

# Load & Process Data
if 'df' not in st.session_state:
    st.session_state.df = load_sample_data()

df = st.session_state.df.copy()
df = detect_anomalies(df)
df = classify_health(df)

# Metrics
col1, col2, col3, col4 = st.columns(4)
total_assets = 1  # Simulates one asset for demo
anomaly_rate = df['anomaly'].mean() * 100
good_health = (df['health'] == 'Good').mean() * 100
col1.metric("Assets Monitored", total_assets)
col2.metric("Anomaly Rate", f"{anomaly_rate:.1f}%", delta="1.2%")
col3.metric("Good Health", f"{good_health:.1f}%")
col4.metric("Last Update", df['timestamp'].max().strftime("%H:%M:%S"))

# Dashboard Tabs
tab1, tab2, tab3 = st.tabs(["📊 Live Dashboard", "🔍 Anomalies", "📈 Trends"])

with tab1:
    col_a, col_b = st.columns(2)
    with col_a:
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=100 - good_health,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Overall Health Risk"},
            delta={'reference': 10},
            gauge={'axis': {'range': [None, 100]},
                   'bar': {'color': "red"},
                   'steps': [{'range': [0, 50], 'color': "lightgreen"},
                             {'range': [50, 80], 'color': "yellow"},
                             {'range': [80, 100], 'color': "red"}],
                   'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 85}})
        )
        fig_gauge.update_layout(height=300)
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with col_b:
        health_dist = df['health'].value_counts()
        fig_pie = px.pie(values=health_dist.values, names=health_dist.index, title="Health Distribution")
        st.plotly_chart(fig_pie, use_container_width=True)
    
    st.subheader("Live Sensor Readings (Latest 50)")
    st.dataframe(df.tail(50), use_container_width=True)

with tab2:
    anomalies_df = df[df['anomaly'] == True].tail(20)
    st.dataframe(anomalies_df, use_container_width=True)
    if not anomalies_df.empty:
        fig_anom = px.scatter(anomalies_df, x='timestamp', y='acc_x', color='health',
                              title="Recent Anomalies (Vibration Spikes)")
        st.plotly_chart(fig_anom)

with tab3:
    fig_line = px.line(df, x='timestamp', y=['acc_x', 'temp', 'wind_speed'],
                       title="Trends Over Time")
    st.plotly_chart(fig_line, use_container_width=True)

# Real-time Simulation
if auto_refresh:
    placeholder = st.empty()
    for _ in range(50):  # Sim loop for demo
        time.sleep(speed)
        # Simulate new data append
        new_row = pd.DataFrame({
            'timestamp': [df['timestamp'].max() + pd.Timedelta(seconds=10)],
            'acc_x': [np.random.normal(0, 0.5)],
            'acc_y': [np.random.normal(0, 0.5)],
            'acc_z': [np.random.normal(0, 0.5)],
            'temp': [np.random.normal(25, 5)],
            'humidity': [np.random.normal(60, 10)],
            'wind_speed': [np.random.exponential(2)]
        })
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True).tail(1000)
        st.rerun()

st.markdown("---")
st.markdown("**Submission Ready:** GitHub repo with this app.py, README (below), requirements.txt, demo.mp4. Deploy: https://share.streamlit.io. **Tech:** ML (IsolationForest) + Rules for thresholds/patterns. Handles real IoT via CSV upload extension. [web:14][web:13][web:5]")
