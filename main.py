# health_insurance_cost_prediction | © 2025 All rights reserved

import streamlit as st
from prediction_helper import predict

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Health Insurance Cost Estimator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------
# Custom Styling
# ------------------------------------------------------------
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 1100px;
        }
        h1 {
            text-align: center;
            color: #1b263b;
            font-weight: 600;
            margin-bottom: 0.5em;
        }
        .subtitle {
            text-align: center;
            color: #495057;
            margin-bottom: 2em;
            font-size: 1rem;
        }
        .section-header {
            font-size: 1.15rem;
            font-weight: 600;
            color: #1b263b;
            margin-top: 2em;
            margin-bottom: 1em;
            border-bottom: 2px solid #dee2e6;
            padding-bottom: 0.3em;
        }
        .result-card {
            background-color: #f8f9fa;
            padding: 1.5em;
            border-radius: 10px;
            border: 1px solid #dee2e6;
            margin-top: 1.2em;
        }
        .result-value {
            font-size: 1.6rem;
            font-weight: 700;
            color: #0a9396;
            margin-bottom: 0.4em;
        }
        .summary-box {
            background-color: #f9f9f9;
            padding: 1.2em;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
            margin-top: 1em;
        }
        .summary-item {
            font-size: 0.95rem;
            margin-bottom: 0.4em;
            color: #343a40;
        }
        div.stButton > button:first-child {
            background-color: #0a9396;
            color: white;
            font-weight: 500;
            border-radius: 6px;
            height: 2.8em;
            width: 100%;
        }
        div.stButton > button:first-child:hover {
            background-color: #007f86;
            color: white;
        }
        @media (max-width: 768px) {
            .block-container { padding: 1.2rem; }
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
st.markdown("<h1>Health Insurance Cost Estimator</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle'>Enter your details below to estimate your expected health insurance premium.</p>",
    unsafe_allow_html=True
)


categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# Create four rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to the grid
with row1[0]:
    age = st.number_input('Age', min_value=18, step=1, max_value=100)
with row1[1]:
    number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
with row1[2]:
    income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

with row2[0]:
    genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
with row2[1]:
    insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
with row2[2]:
    employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

with row3[0]:
    gender = st.selectbox('Gender', categorical_options['Gender'])
with row3[1]:
    marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
with row3[2]:
    bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

with row4[0]:
    smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
with row4[1]:
    region = st.selectbox('Region', categorical_options['Region'])
with row4[2]:
    medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

st.markdown("")
predict_button = st.button("Predict Insurance Cost")

if predict_button:
    with st.spinner("Calculating..."):
        result = predict(input_dict)

    if isinstance(result, (int, float)):
        # Result Card
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-value">₹{result:,.0f}</div>
                <div>Estimated Annual Health Insurance Cost</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Summary Section (Simplified)
        st.markdown("<div class='section-header'>Summary</div>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class='summary-box'>
                <div class='summary-item'><strong>Age Group:</strong> {'Below 25' if age <= 25 else '25 and above'}</div>
                <div class='summary-item'><strong>Medical History:</strong> {medical_history}</div>
                <div class='summary-item'><strong>Region:</strong> {region}</div>
                <div class='summary-item'><strong>Selected Plan:</strong> {insurance_plan}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.error(result)

st.markdown("<hr style='margin-top:2em;'>", unsafe_allow_html=True)
st.caption("Health Insurance Cost Estimator | © 2025")
