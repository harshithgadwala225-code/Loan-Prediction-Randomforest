import streamlit as st
import joblib
import numpy as np

# load model
model = joblib.load("RandomForestRegressor.pkl")

st.title("🛡️ Loan Target Prediction App")

st.write("Enter User Details")

# USER INPUTS
age = st.number_input("Enter Age", min_value=18, max_value=100, value=25)

income = st.number_input("Enter Income", value=10000)

loan_amount = st.number_input("Enter Loan Amount")

credit_score = st.number_input("Enter Credit Score")

num_transactions = st.number_input("Number of Transactions")

annual_spend = st.number_input("Annual Spend")

# TELANGANA TOP CITIES
city = st.selectbox(
    "Select City",
    ["Hyderabad","Delhi", "Mumbai", "Chennai", "Bangalore"]
)

employment_type = st.selectbox(
    "Employment Type",
    ["Salaried", "Self-employed", "Business"]
)

loan_type = st.selectbox(
    "Loan Type",
    ["Home", "Personal", "Education"]
)

# SIMPLE ENCODING (must match training)
city_map = {
    "Bangalore": 0,
    "Chennai": 1,
    "Delhi": 2,
    "Hyderabad": 3,
    "Mumbai": 4
}

emp_map = {
    "Salaried": 0,
    "Self-employed": 1,
    "Business": 2
}

loan_map = {
    "Home": 0,
    "Personal": 1,
    "Education": 2
}

if st.button("Predict"):

    data = np.array([[age, income, loan_amount, credit_score,
                  num_transactions, annual_spend,
                  city_map[city], emp_map[employment_type],
                  loan_map[loan_type]]])

    prediction = model.predict(data)

    st.success(f"Predicted Target: {prediction[0]}")

#Based on our Dataset Context:

# 680 (average case)
# 720 (good case)
# 780 (excellent case)

#Mainly we get bettter results of this model only when we use these as followed:

# when we  retrain with new data
# when we update training dataset
# when we do hyperparameter tuning
# when we do feature engineering
 
# In Real Industry Process:

# In companies:

# 1. Deploy model
# 2. Collect user data
# 3. Store predictions + actual outcomes
# 4️. Retrain monthly
# 5️. Deploy new version