import streamlit as st
import pandas as pd
import seaborn as sns

def clean_condition(x):
    if x == 0:
        return "No heart disease"
    else:
        return "Heart disease"

def clean_sex(x):
    if x == 0:
        return "Female"
    else:
        return "Male"

@st.cache
def load_data():
    data_frame = pd.read_csv('heart_cleveland_upload.csv')
    data_frame = data_frame.rename({'trestbps': 'Resting blood pressure'}, axis=1)
    data_frame = data_frame.rename({'chol': 'Serum cholesterol (mg/dl)'}, axis=1)
    data_frame['condition'] = data_frame['condition'].apply(clean_condition)
    data_frame['sex'] = data_frame['sex'].apply(clean_sex)
    return data_frame

data_frame = load_data()
data_frame_male = data_frame[data_frame['sex'] == 'Male']
data_frame_female = data_frame[data_frame['sex'] == 'Female']

def show_explore_page():
    st.title("Explore Heart Disease Data")

    figure1 = sns.displot(data=data_frame, x="age", col='condition', kde=True)
    figure2 = sns.displot(data_frame_male, x="age", col='condition', color=(0.1, 0.2, 0.5), kde=True)
    figure3 = sns.displot(data_frame_female, x="age", col='condition', color=(0.5, 0.1, 0.1), kde=True)
    figure4 = sns.jointplot(data=data_frame, x='Serum cholesterol (mg/dl)', y='Resting blood pressure', hue='condition')


    st.write("""#### Distribution of heart disease by age""")
    st.pyplot(figure1)

    st.write("""\n#### Distribution of male heart disease by age""")
    st.pyplot(figure2)

    st.write("""\n#### Distribution of female heart disease by age""")
    st.pyplot(figure3)

    st.write("""\n#### Joinplot of Cholesterol and Resting blood pressure for disease/no disease""")
    st.pyplot(figure4)
