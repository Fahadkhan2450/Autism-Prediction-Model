# Autism-Prediction-Model
Overview
This project aims to develop a machine learning-based system that predicts the likelihood of Autism Spectrum Disorder (ASD) in individuals based on behavioral and demographic input features. The final solution integrates data analysis, model training, a REST API using FastAPI, and a user-friendly interface built with Streamlit. The model is also containerized using Docker for easy deployment.

Dataset
The dataset contains a combination of behavioral scores (AQ-10), demographic details (age, gender, ethnicity), and clinical factors (family history, jaundice, prior app usage, etc.).

The target variable indicates whether the individual is likely to have ASD or not (binary classification).

Tools and Libraries
Pandas – data manipulation and cleaning

NumPy – numerical operations

Matplotlib & Seaborn – data visualization and pattern analysis

Scikit-learn – model training, preprocessing, and evaluation

XGBoost – gradient boosting model implementation

FastAPI – for creating the backend API

Streamlit – for designing an interactive web UI

Docker – for containerizing the FastAPI application

Project Workflow
1. Data Preprocessing
Loaded and cleaned the dataset using Pandas

Handled missing values and encoded categorical variables

Applied label encoding and one-hot encoding where needed

Scaled features as appropriate for model input

2. Exploratory Data Analysis (EDA)
Used Seaborn and Matplotlib to explore and visualize:

Feature correlations

Distribution of age and ASD likelihood

Response patterns to screening questions

Class imbalance

3. Model Training
Trained and evaluated the following classification algorithms:

Decision Tree Classifier

Random Forest Classifier

XGBoost Classifier

Each model was evaluated using:

Accuracy score

Confusion matrix

Classification report (precision, recall, F1-score)

4. Hyperparameter Tuning
Applied RandomizedSearchCV to optimize model parameters

Identified best-performing configuration for each model

5. Model Deployment
Saved the trained model using pickle

Developed a FastAPI backend to serve predictions via an API endpoint

Built a Streamlit web application to collect user input and display predictions interactively

Dockerized the FastAPI backend for scalable and portable deployment


