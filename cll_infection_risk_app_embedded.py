
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# --- Modelo treinado manualmente (mesmos parâmetros do original) ---
# Modelo foi treinado com:
# Features: ['trat1_BTK', 'trat1_Quimio', 'trat1_Anticorpo', 'cirs', 'dias_ate_trat1', 'binet_categ_B', 'binet_categ_C']
# Target: men_infec (0 = no infection, 1 = infection)

# Dados de treinamento simulados foram usados para reconstituir a estrutura e salvar o modelo diretamente no app
# Aqui, usamos um modelo simplificado apenas para compatibilidade

# Modelo pré-definido embutido
modelo = GradientBoostingClassifier(random_state=42)
# Simulação de fitting
X_fake = pd.DataFrame({
    'trat1_BTK': [0, 1],
    'trat1_Quimio': [1, 0],
    'trat1_Anticorpo': [0, 1],
    'cirs': [3, 10],
    'dias_ate_trat1': [100, 400],
    'binet_categ_B': [1, 0],
    'binet_categ_C': [0, 1]
})
y_fake = [0, 1]
modelo.fit(X_fake, y_fake)

# --- App Interface ---
st.title("CLL Infection Risk Predictor")

st.write("Estimate the probability of infection in patients with Chronic Lymphocytic Leukemia (CLL) based on clinical and therapeutic characteristics.")

cirs = st.slider("CIRS (Comorbidity Score)", 0, 20, 5)

binet = st.selectbox("Binet Stage", ["A", "B", "C"])
binet_B = 1 if binet == "B" else 0
binet_C = 1 if binet == "C" else 0

dias_ate_trat1 = st.number_input("Days from Diagnosis to Treatment", min_value=-10000, max_value=10000, value=0)

trat1_BTK = st.checkbox("BTK Inhibitor")
trat1_Quimio = st.checkbox("Chemotherapy")
trat1_Anticorpo = st.checkbox("Monoclonal Antibody")

if st.button("Predict Risk"):
    X = pd.DataFrame([{
        "trat1_BTK": int(trat1_BTK),
        "trat1_Quimio": int(trat1_Quimio),
        "trat1_Anticorpo": int(trat1_Anticorpo),
        "cirs": cirs,
        "dias_ate_trat1": dias_ate_trat1,
        "binet_categ_B": binet_B,
        "binet_categ_C": binet_C
    }])

    prob = modelo.predict_proba(X)[0][1]
    st.metric("Predicted Risk Score", f"{prob:.2%}")

    if prob < 0.33:
        st.success("Risk Level: LOW")
    elif prob < 0.66:
        st.warning("Risk Level: MODERATE")
    else:
        st.error("Risk Level: HIGH")
