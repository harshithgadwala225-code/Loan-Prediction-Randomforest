# Loan Target Prediction App (Machine Learning + Streamlit)

## 📌 Project Overview

This project is a Machine Learning based web application that predicts a
numeric target value based on user financial and demographic details.

The system is built using:

-   Python
-   Scikit-learn
-   Random Forest Regression
-   Streamlit

It demonstrates the complete flow from **data preprocessing → model
training → deployment as a web app**.

------------------------------------------------------------------------

## 📊 Dataset Details

Dataset used: `task1_dataset.csv`

### Input Features

-   Age
-   Income
-   Loan Amount
-   Credit Score
-   Number of Transactions
-   Annual Spend
-   City
-   Employment Type
-   Loan Type

### Target Variable

-   `target`

### Data Preprocessing

-   Removed unnecessary columns (date)
-   Handled missing values using median strategy
-   Encoded categorical features using LabelEncoder
-   Split data into training and testing sets

------------------------------------------------------------------------

## 🤖 Machine Learning Model

### Algorithm Used: Random Forest Regressor

### Why Random Forest?

Random Forest was chosen because:

-   Works very well on structured (tabular) datasets

-   Captures complex and nonlinear relationships

-   More stable compared to a single Decision Tree

-   Less prone to overfitting

-   Provided better performance compared to:

    -   Linear Regression
    -   KNN
    -   Decision Tree

Hence, it was selected as the final model.

------------------------------------------------------------------------

## 💾 Model Saving

The trained model is saved as:

    RandomForestRegressor.pkl

This allows prediction without retraining the model every time.

------------------------------------------------------------------------

## 🌐 Streamlit Web Application

The Streamlit interface allows users to:

-   Enter personal and financial details
-   Select categorical inputs using dropdowns
-   Get predicted target value instantly

This converts the ML model into an interactive web application.

------------------------------------------------------------------------

## 📁 Project Structure

    Loan_prediction_app/
    │
    ├── app.py
    ├── RandomForestRegressor.pkl
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ▶️ How to Run Locally

Install dependencies:

    pip install -r requirements.txt

Run the app:

    streamlit run app.py

------------------------------------------------------------------------

## 📈 Future Improvements

-   Add full preprocessing pipeline inside the deployed app
-   Try advanced models like Gradient Boosting / XGBoost
-   Improve UI design
-   Add validation for user inputs
-   Store user prediction data for model improvement

------------------------------------------------------------------------

## 🧠 Learning Outcomes

Through this project, the following concepts were explored:

-   Data preprocessing and feature handling
-   Training and evaluating regression models
-   Model selection based on performance
-   Saving and reusing trained ML models
-   Converting ML models into web applications
-   Basic deployment workflow

------------------------------------------------------------------------

## 📜 License

This project is created for learning and demonstration purposes.
