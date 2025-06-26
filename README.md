# Autism-Prediction-Model
Autism Spectrum Disorder (ASD) Prediction
This project focuses on building a machine learning model that predicts the likelihood of Autism Spectrum Disorder (ASD) based on input features extracted from a publicly available dataset. The project evaluates the performance of three supervised learning models — Decision Tree, Random Forest, and XGBoost Classifier — to determine which algorithm provides the most accurate predictions.

Dataset
The dataset contains a mixture of behavioral, demographic, and screening features.
It includes responses to ten behavioral questions (AQ-10), age, gender, family history, ethnicity, and other relevant features.
The target variable is a binary class: whether or not the individual is likely to have ASD.

Tools and Libraries
The following Python libraries were used throughout the project:
Pandas – for data loading and manipulation
NumPy – for numerical operations
Seaborn & Matplotlib – for data visualization and exploration
Scikit-learn – for preprocessing, modeling, evaluation
XGBoost – for advanced gradient boosting model implementation

 Project Workflow
 
1. Data Preprocessing
Handled missing values, categorical encoding, and irrelevant columns.

Applied Label Encoding and One-Hot Encoding where necessary.

Performed feature scaling (if needed) to normalize the data.

2. Exploratory Data Analysis (EDA)
Used Seaborn and Matplotlib to visualize feature distributions and correlations.

Plotted class imbalance, age distribution, and response patterns.

Identified key features contributing to ASD prediction.

3. Modeling
Three different classification models were trained and evaluated:

Decision Tree Classifier

Random Forest Classifier

XGBoost Classifier

Each model was trained using a train-test split, and evaluated using:

Accuracy
Classification Report
Confusion Matrix

4. Hyperparameter Tuning
Used RandomizedSearchCV to tune model parameters.
Selected the best combination of hyperparameters for each model.

5. Evaluation
Compared performance of all three models on the same test set.
XGBoost Classifier performed best in terms of precision and overall accuracy.
