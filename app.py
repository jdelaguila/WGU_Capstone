import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
import pyrebase
from datetime import datetime


firebaseConfig = {
  'apiKey': "AIzaSyA0-DQ1d41LoYiQDnDXf7H-nobdi6DJmzg",
  'authDomain': "streamlit-authorization.firebaseapp.com",
  'projectId': "streamlit-authorization",
  'databaseURL': "https://streamlit-authorization-default-rtdb.firebaseio.com/",
  'storageBucket': "streamlit-authorization.appspot.com",
  'messagingSenderId': "806113993596",
  'appId': "1:806113993596:web:c54906290b850da2d4baf9",
  'measurementId': "G-FNR2Q6P7ZB"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db = firebase.database()
storage = firebase.storage()

st.sidebar.title("Heart Disease Prediction Login")

email = st.sidebar.text_input("Please enter your email:")
password = st.sidebar.text_input("Please enter your password: ", type='password')

login = st.sidebar.checkbox("Login")

if login:
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        st.write("You logged in")
        page = st.radio("Go to: ", ("Diagnose", "Explore"))

        if page == "Diagnose":
            show_predict_page()
        else:
            show_explore_page()

    except Exception:
        st.title("Invalid username/password. Please try again.")








