#  InfraGuard  
### Infrastructure Health & Anomaly Analysis System  

AI-powered real-time infrastructure monitoring system developed to identify anomalies and evaluate the structural health of infrastructure for smart city use cases

##  Quick Access

 **Live Application:** https://smartinfraanomaly.streamlit.app

 **Demo Video & PPT:** https://drive.google.com/drive/folders/1kXS8uSfiH4e_ItUcfd1A7cjKs4ergkVr?usp=sharing  

---

##  Problem Statement

Aging infrastructure and rising environmental factors threaten the structural integrity of the system. Conventional systems of inspection are manual, reactive, and inefficient, often identifying problems only after visible damage has been done.

There is a requirement for a real-time, intelligent system capable of identifying anomalies and allowing for predictive maintenance.

---

## Approach

InfraGuard is intended to be a real-time infrastructure health monitoring dashboard that:

- Continuously processes live or simulated sensor data  
- Identifies anomalies using Machine Learning (Isolation Forest)  
- Calculates infrastructure health scores  
- Categorizes structural health into Good, Warning, and Critical levels  
- Supports predictive maintenance rather than reactive maintenance  

The system aims to provide early anomaly detection to minimize risks of structural failure. 

---

## Implementation Details

1. Sensor data (simulated/live) is ingested into the system.  
2. Key parameters monitored include:
   - Vibration  
   - Temperature  
   - Wind Speed  
   - Structural Stress  
   - Humidity  

3. An Isolation Forest model analyzes patterns and identifies abnormal behavior.  
4. Each data point is classified as:
   - ✅ Good  
   - ⚠️ Warning  
   - 🔴 Critical   

5. A health score and anomaly rate are computed dynamically.  
6. Interactive visualizations display trends, risk levels, and system stability in real time.

---

## Tech Stack

- **Frontend & Dashboard:** Streamlit    
- **Machine Learning:** Scikit-learn (Isolation Forest)  
- **Deployment:** Streamlit Cloud  

---

##  Key Features

-  Live Sensor Monitoring  
-  Real-Time Anomaly Detection  
-  Time-Series Trend Analysis  
-  Risk Level Visualization  
-  Infrastructure Health Score  
-  Live Deployed Application

---

##  Installation & Setup (Run Locally)

Clone the repository:

```bash
git clone https://github.com/AkankshaKalamadugu/TetherX-Hackathon
cd TetherX-Hackathon
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

##  Impact

InfraGuard changes the infrastructure monitoring paradigm from:

**Reactive Inspection → Predictive Intelligence**

It allows for:

- Early anomaly detection  
- Lower risk of structural failure  
- Enhanced smart city safety  
- Efficient infrastructure monitoring  

---

##  Future Scope

- Real IoT sensor network integration  
- Deep learning-based anomaly detection  
- SMS / Email notification system  
- Cloud database integration  
- Mobile dashboard integration  

---

##  Developed For

Hackathon Submission – TetherX Hackathon(VIT Chennai)
---
