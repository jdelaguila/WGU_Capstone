import streamlit as st
import pandas as pd
import seaborn as sns
from predict_page import show_predict_page

# change condition to readable display
def clean_condition(x):
    if x == 0:
        return "No heart disease"
    else:
        return "Heart disease"

# change sex to readable display
def clean_sex(x):
    if x == 0:
        return "Female"
    else:
        return "Male"

# change chest pain to readable display
def clean_chest_pain(x):
    if x == 0:
        return "Typical angina"
    elif x == 1:
        return "Atypical angina"
    elif x == 2:
        return "Non-anginal pain"
    else:
        return "Asymptomatic"

# change blood sugar to readable display
def clean_blood_sugar(x):
    if x == 0:
        return 'Greater than or equal to 120 mg/dl'
    else:
        return 'Less than 120 mg/dl'

# change electrocardiographic results to readable display
def clean_ecg(x):
    if x == 0:
        return 'Normal'
    elif x == 1:
        return 'Having ST-T wave abnormality'
    else:
        return 'showing probable or definite left ventricular hypertrophy by Estes\' criteria'

# change exercise induced angina to readable display
def clean_exang(x):
    if x == 0:
        return 'no'
    else:
        return 'yes'

# change the slope of the peak exercise ST segment to readable display
def clean_slope(x):
    if x == 0:
        return 'upsloping'
    elif x == 1:
        return 'flat'
    else:
        return 'downsloping'

# change Thalassemia attributes to readable display
def clean_thal(x):
    if x == 0:
        return 'normal'
    elif x == 1:
        return 'fixed defect'
    else:
        return 'reversible defect'

@st.cache
def load_data():
    data_frame = pd.read_csv('heart_cleveland_upload.csv')

    # make dataframe readable for display
    data_frame = data_frame.rename({'trestbps': 'resting blood pressure'}, axis=1)
    data_frame = data_frame.rename({'restecg': 'resting electrocardiographic results'}, axis=1)
    data_frame = data_frame.rename({'thalach': 'maximum heart rate achieved'}, axis=1)
    data_frame = data_frame.rename({'chol': 'serum cholesterol (mg/dl)'}, axis=1)
    data_frame = data_frame.rename({'fbs': 'fasting blood sugar'}, axis=1)
    data_frame = data_frame.rename({'exang': 'exercise induced angina'}, axis=1)
    data_frame = data_frame.rename({'oldpeak': 'ST depression induced by exercise relative to rest'}, axis=1)
    data_frame = data_frame.rename({'slope': 'slope of the peak exercise ST segment'}, axis=1)
    data_frame = data_frame.rename({'cp': 'chest pain'}, axis=1)
    data_frame = data_frame.rename({'ca': 'number of major vessels colored by flouroscopy'}, axis=1)
    data_frame = data_frame.rename({'thal': 'thalassemia'}, axis=1)
    data_frame['fasting blood sugar'] = data_frame['fasting blood sugar'].apply(clean_blood_sugar)
    data_frame['resting electrocardiographic results'] = data_frame['resting electrocardiographic results'].apply(clean_ecg)
    data_frame['condition'] = data_frame['condition'].apply(clean_condition)
    data_frame['sex'] = data_frame['sex'].apply(clean_sex)
    data_frame['chest pain'] = data_frame['chest pain'].apply(clean_chest_pain)
    data_frame['exercise induced angina'] = data_frame['exercise induced angina'].apply(clean_exang)
    data_frame['slope of the peak exercise ST segment'] = data_frame['slope of the peak exercise ST segment'].apply(clean_slope)
    data_frame['thalassemia'] = data_frame['thalassemia'].apply(clean_thal)

    return data_frame

data_frame = load_data()

# create separate dataframes for male and female
data_frame_male = data_frame[data_frame['sex'] == 'Male']
data_frame_female = data_frame[data_frame['sex'] == 'Female']

def show_explore_page():
    st.title("Explore Heart Disease Data")

    st.write("""#### Complete Dataset""")
    st.dataframe(data_frame)

    figure1 = sns.displot(data=data_frame, x="age", col='condition', kde=True)
    figure2 = sns.displot(data_frame_male, x="age", col='condition', color=(0.1, 0.2, 0.5), kde=True)
    figure3 = sns.displot(data_frame_female, x="age", col='condition', color=(0.5, 0.1, 0.1), kde=True)
    figure4 = sns.jointplot(data=data_frame, x='serum cholesterol (mg/dl)', y='resting blood pressure', hue='condition')


    st.write("""#### Distribution of heart disease by age""")
    st.pyplot(figure1)

    st.write("""\n#### Distribution of male heart disease by age""")
    st.pyplot(figure2)

    st.write("""\n#### Distribution of female heart disease by age""")
    st.pyplot(figure3)

    st.write("""\n#### Joinplot of Cholesterol and Resting blood pressure for disease/no disease""")
    st.pyplot(figure4)

    st.write("""#### Interactive query: Show Jointplot of Cholesterol and Resting blood pressure between the ages 'a' and 'b'""")
    a = st.number_input("Enter a: ", 0, 120)
    b = st.number_input("Enter b: ", 0, 120)

    run = st.button('Run Query')

    # show jointplot of cholesterol and resting blood pressure based on user input
    if run:
        if a <= b:
            data_frame2 = data_frame[(data_frame['age'] <= b) & (data_frame['age'] >= a)]
            figure5 = sns.jointplot(data=data_frame2, x='serum cholesterol (mg/dl)', y='resting blood pressure',
                                    hue='condition')
            st.pyplot(figure5)
        else:
            data_frame2 = data_frame[(data_frame['age'] <= a) & (data_frame['age'] >= b)]
            figure5 = sns.jointplot(data=data_frame2, x='serum cholesterol (mg/dl)', y='resting blood pressure',
                                    hue='condition')
            st.pyplot(figure5)

    st.write("""#### Interactive query: Choose which columns you would like to drop from data frame""")
    options = st.multiselect("Choose columns: ", ['age', 'sex', 'chest pain', 'resting blood pressure',
                                                  'serum cholesterol (mg/dl)', 'fasting blood sugar',
                                                  'resting electrocardiographic results', 'maximum heart rate achieved',
                                                  'exercise induced angina',
                                                  'ST depression induced by exercise relative to rest',
                                                  'slope of the peak exercise ST segment',
                                                  'number of major vessels colored by flouroscopy',
                                                  'thalassemia', 'condition', ])

    run1 = st.button('Display Data')

    # show dataframe based on user query
    if run1:
        data_frame3 = data_frame
        for string in options:
            data_frame3 = data_frame3.drop(string, axis=1)
        st.dataframe(data_frame3)


