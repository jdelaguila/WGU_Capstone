import streamlit as st
import pickle
import numpy as np



def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

desicion_tree_loaded = data["model"]

def show_predict_page():
    st.title("Heart Disease Prediction")

    st.write("""Enter test results for preliminary diagnosis:""")

    age = st.number_input("Enter age: ", 0, 120)
    sex = st.selectbox("Select sex: ", ["Male", "Female"])
    chest_pain = st.selectbox("Select chest pain type: ", ["Typical Angina", "Atypical Angina",
                                                          "Non-Anginal Pain", "Asymptomatic"])
    resting_bp = st.number_input("Enter resting blood pressure: ", 0, 300)
    cholesterol = st.number_input("Enter serum cholesterol in mg/dl: ", 0, 700)
    fasting_blood_sugar = st.selectbox("Select fasting blood sugar: ", ["Less than 120 mg/dl",
                                                                       "Greater than 120 mg/dl"])
    resting_ecg = st.selectbox("Select resting electrocardiographic result: ", ["Normal", "ST-T wave abnormality",
                                                                                "Left ventricular hypertrophy by Estes' "
                                                                                "criteria (probably or definite)"])
    max_heart_rate = st.number_input("Enter maximum heart rate achieved: ", 0, 300)
    exercise_induced_angina = st.selectbox("Exercise induced angina: ", ["Yes", "No"])
    old_peak = st.number_input(label="ST depression induced by exercise relative to rest",
                               min_value=0.0, max_value=10.0, step= 0.1, format="%.1f")
    slope = st.selectbox("The slope of the peak exercise ST segment", ["Unsloping", "Flat", "Downsloping"])
    thalassemia = st.selectbox("Thalassemia: ", ["Normal", "Fixed defect", "Reversable defect"])
    ca = st.number_input("Number of major vessels colored by fluoroscopy", 0 ,5)

    submit = st.button("Make Diagnosis")
    if submit:
        if sex == "Female":
            sex_int = 0
        else:
            sex_int = 1
        if chest_pain == "Typical Angina":
            chest_pain_int = 0
        elif chest_pain == "Atypical Angina":
            chest_pain_int = 1
        elif chest_pain == "Non-Anginal Pain":
            chest_pain_int = 2
        else:
            chest_pain_int = 3
        if fasting_blood_sugar == "Less than 120 mg/dl":
            fasting_blood_sugar_int = 0
        else:
            fasting_blood_sugar_int = 1
        if resting_ecg == "Normal":
            resting_ecg_int = 0
        elif resting_ecg == "ST-T wave abnormality":
            resting_ecg_int = 1
        else:
            resting_ecg_int = 2
        if exercise_induced_angina == "No":
            exercise_induced_angina_int = 0
        else:
            exercise_induced_angina_int = 1
        if slope == "Unsloping":
            slope_int = 0
        elif slope == "Flat":
            slope_int = 1
        else:
            slope_int = 2
        if thalassemia == "Normal":
            thalassemia_int = 0
        elif thalassemia == "Fixed defect":
            thalassemia_int = 1
        else:
            thalassemia_int = 2

        X = np.array([[age, sex_int, chest_pain_int, resting_bp, cholesterol, fasting_blood_sugar_int, resting_ecg_int,
                       max_heart_rate, exercise_induced_angina_int, old_peak, slope_int, ca, thalassemia_int]])
        diagnosis = desicion_tree_loaded.predict(X)
        if diagnosis[0] == 0:
            st.subheader("Diagnosis: No heart disease")
        else:
            st.subheader("Diagnosis: Heart disease")







