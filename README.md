# CLL Infection Risk Prediction App

This Streamlit web application allows clinicians and researchers to estimate the risk of infection in patients with Chronic Lymphocytic Leukemia (CLL) based on real-world data and a trained machine learning model.

## 🔍 Purpose

To predict the probability of infectious events using clinical and therapeutic features such as:

- Comorbidity burden (CIRS)
- Binet clinical stage
- Treatment type (BTK inhibitors, chemotherapy, monoclonal antibodies)
- Time from diagnosis to treatment

## 🧠 Model

This app uses a trained Gradient Boosting Classifier (`scikit-learn`) based on a Brazilian multicenter CLL cohort. The model outputs a risk score and a categorical classification: **Low**, **Moderate**, or **High Risk**.

## 📦 Files

- `cll_infection_risk_app.py`: Main app script
- `modelo_risco_infeccao_CLL.pkl`: Trained machine learning model
- `requirements.txt`: Python dependencies

## 🚀 How to Run Locally

1. Clone this repository or download the files.
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run cll_infection_risk_app.py
   ```

## 🌐 How to Deploy on Streamlit Cloud

1. Fork or upload this repo to your GitHub account.
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click “New app” and select:
   - Repo: your-username/cll-infection-risk-app
   - File: `cll_infection_risk_app.py`
4. Click “Deploy”.

Enjoy predicting and stratifying risk in your CLL cohort!

---

Developed with ❤️ for research and clinical decision support.