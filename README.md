## Restaurant Rating Predictor project

I created this machine learning project helps potential restraunters find the best combination of services that lead to good ratings.

The dataset I used is from Kaggle (link: https://www.kaggle.com/datasets/mohdshahnawazaadil/restaurant-dataset). 

**Step 1**
After loading the data into a notebook, I anallysed and scaled it to find the top features that impacted the ratings og restaurants
a) Average cost of 2 people
b) Has table reservation
c) Has online delivery
d) Price range (Is it considered cheap or expensive)

**Step 2**
I used ML models (Logistic Regression, SVR, Random forests, ADAboost) to train the modlels and evaluated their accuracy. 

Observation: Tree based mdels performed the best when comparing their MSE and saved the model. 

**Step 3**
Lastly I created a streamlit app to allow users to enter values for the features as they choose and predict the reating.
