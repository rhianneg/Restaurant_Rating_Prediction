## Restaurant Rating Predictor project

I created this machine learning project helps potential restraunters find the best combination of services that lead to good ratings.

The dataset I used is from Kaggle (link: https://www.kaggle.com/datasets/mohdshahnawazaadil/restaurant-dataset). 

### Project Overview
This project analyzes restaurant data to predict ratings and identify key factors that influence customer satisfaction. The analysis helps answer the crucial question: "What combination of restaurant features leads to the best ratings?"
Dataset: Restaurant Dataset from Kaggle

Size: 9,551 restaurant ratings
Original Features: 17 features including restaurant name, city, cuisine, and other restaurant characteristics


#### Step 1: Data Analysis and Feature Engineering
##### Data Loading and Exploration 

Loaded the restaurant dataset containing 9,551 ratings across 17 features and performed exploratory data analysis on restaurant characteristics including name, city, cuisine, and service features
Analyzed the distribution of ratings and various restaurant attributes
Identified patterns and correlations between different variables

##### Feature Selection and Scaling

Applied data scaling techniques to normalize features and performed feature importance analysis to identify the most impactful variables
I then selected the top 4 features that significantly influence restaurant ratings.

Average cost for 2 people: Price point indicator
Has table reservation: Booking availability feature
Has online delivery: Digital service offering
Price range: Restaurant category (cheap/moderate/expensive)



#### Step 2: Machine Learning Model Development
#####Model Training and Evaluation
Implemented and compared multiple machine learning algorithms with detailed performance metrics:

###### Support Vector Regression (SVR):

Mean Absolute Error: 0.370
Mean Squared Error: 0.474


###### Decision Tree Regressor:

Mean Absolute Error: 0.349
Mean Squared Error: 0.445


###### Random Forest:

Mean Absolute Error: 0.350
Mean Squared Error: 0.444


###### K-Nearest Neighbors (KNN):

Mean Absolute Error: 0.351
Mean Squared Error: 0.447


###### AdaBoost:

Mean Absolute Error: 0.365
Mean Squared Error: 0.450

##### Model Performance Analysis

Evaluated all models using Mean Absolute Error (MAE) and Mean Squared Error (MSE) as primary metrics and conducted comparative analysis across five different algorithms
Key Finding: Decision Tree and Random Forest models achieved the best performance with the lowest MSE scores

##### Best Performing Models:

Decision Tree Regressor: MSE = 0.445
Random Forest: MSE = 0.444 (best overall performance)


I then selected and saved the Random Forest model for deployment due to its superior performance and robustness

#### Step 3: Interactive Web Application
Streamlit Deployment

Developed a user-friendly web application using Streamlit
Created an interactive interface for real-time restaurant rating predictions
Enables users to input restaurant features and receive instant rating predictions

Application Features

Input fields for the four key restaurant features
Real-time prediction display
Clean, intuitive user interface for easy interaction

Key Insights

Model Performance Ranking:

Random Forest achieved the best performance (MSE: 0.444)
Decision Tree was second best (MSE: 0.445)
Tree-based models significantly outperformed other approaches


Feature Importance: The analysis revealed that cost, reservation availability, delivery options, and price range are the most significant predictors of restaurant ratings
Algorithm Effectiveness: Tree-based algorithms outperformed traditional regression methods, suggesting complex non-linear relationships between features and ratings
Business Application: The model provides actionable insights for restaurateurs to optimize their service offerings with quantifiable impact predictions
