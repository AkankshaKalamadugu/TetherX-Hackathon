#  InfraGuard  
### Infrastructure Health & Anomaly Analysis System  

AI-powered real-time infrastructure monitoring system developed to identify anomalies and evaluate the structural health of infrastructure for smart city use cases

##  Quick Access

 **Live Application:** https://smartinfraanomaly.streamlit.app

 **Demo Video & PPT:** https://drive.google.com/your-folder-link  

---

##  Problem Statement

Aging infrastructure and rising environmental factors threaten the structural integrity of the system. Conventional systems of inspection are manual, reactive, and inefficient, often identifying problems only after visible damage has been done.

There is a requirement for a real-time, intelligent system capable of identifying anomalies and allowing for predictive maintenance.

---

##  Proposed Solution

InfraGuard is a real-time infrastructure health monitoring dashboard that:

- Continuously processes live sensor data  
- Detects anomalies using Machine Learning (Isolation Forest)  
- Calculates infrastructure health scores  
- Visualizes risk levels through interactive dashboards  
- Enables predictive maintenance instead of reactive repair  

---

##  Tech Stack

- **Frontend & Dashboard:** Streamlit   
- **Machine Learning:** Scikit-learn (Isolation Forest)  
- **Deployment:** Streamlit Cloud  

---

##  How It Works

1. Simulated or live sensor data is ingested.  
2. Features like vibration, temperature, wind speed, stress, and humidity are monitored.  
3. An Isolation Forest model detects abnormal patterns.  
4. Each reading is classified as:  
   - ✅ Good  
   - ⚠️ Warning  
   - 🔴 Critical  
5. A health score and anomaly rate are computed.  
6. Interactive graphs visualize trends and structural stability.  

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
