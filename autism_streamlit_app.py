import streamlit as st
import requests

st.title("Autism Prediction System")

# All input fields
a1 = st.number_input("A1 Score")
a2 = st.number_input("A2 Score")
a3 = st.number_input("A3 Score")
a4 = st.number_input("A4 Score")
a5 = st.number_input("A5 Score")
a6 = st.number_input("A6 Score")
a7 = st.number_input("A7 Score")
a8 = st.number_input("A8 Score")
a9 = st.number_input("A9 Score")
a10 = st.number_input("A10 Score")
age = st.number_input("Age")
gen = st.number_input("Gender (0=Female, 1=Male)")
eth = st.number_input("Ethnicity")
jaund = st.number_input("Jaundice (0=No, 1=Yes)")
austim = st.number_input("Austim (0=No, 1=Yes)")  # ✅ NEW FIELD
c_o_r = st.number_input("Country of Residency")
u_a_b = st.number_input("Used App Before (0=No, 1=Yes)")
res = st.number_input("Result")
rel = st.number_input("Relation")

# Button click logic
if st.button("Predict Autism"):
    input_data = {
        "A1_Score": a1,
        "A2_Score": a2,
        "A3_Score": a3,
        "A4_Score": a4,
        "A5_Score": a5,
        "A6_Score": a6,
        "A7_Score": a7,
        "A8_Score": a8,
        "A9_Score": a9,
        "A10_Score": a10,
        "age": age,
        "gender": gen,
        "ethnicity": eth,
        "jaundice": jaund,
        "austim": austim,  # ✅ Include it here too
        "contry_of_res": c_o_r,
        "used_app_before": u_a_b,
        "result": res,
        "relation": rel
    }

    try:
        response = requests.post("http://127.0.0.1:8000/autism_prediction", json=input_data)
        if response.status_code == 200:
            result = response.json().get("prediction", "")
            st.success(f"Prediction: {result}")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Connection Error: {e}")
