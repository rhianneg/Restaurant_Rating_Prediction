import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

st.set_page_config(layout = "wide")

scaler = joblib.load("scaler.pkl")

st.title("Restaurant Rating Prediction App")

st.caption("This app helps you predict a restaurants rating ")

st.divider()

averagecost = st.number_input("Please enter the average cost for two", min_value=50, max_value=100000, value = 1000, step = 200)

tablebooking = st.selectbox("Restaurant has table booking or not: ", ["Yes","No"])

onlinedelivery = st.selectbox("Restaurant has online delivery?", ["Yes", "No"])

pricerange = st.selectbox("What is the price range (1 = Cheapest, 4 = Most Expensive)", [1,2,3,4])

predictbutton = st.button("Predict the rating")

model = joblib.load("mlmodel.pkl")

bookingstatus = 1 if tablebooking == "Yes" else 0

deliverystatus = 1 if onlinedelivery == "Yes" else 0

# averagecost = scaler.fit_transform(averagecost)
# bookingstatus = scaler.fit_transform(bookingstatus)
# deliverystatus = scaler.fit_transform(deliverystatus)
# pricerange = scaler.fit_transform(pricerange)

values = [(averagecost, bookingstatus, deliverystatus, pricerange)]
my_X_values = np.array(values)

X = scaler.transform(my_X_values)

if predictbutton:
    st.snow()

    prediction = model.predict(X)

    st.write(prediction)

    if prediction < 2.5:
        st.write("Poor")
    elif prediction < 3.5:
        st.write("Average")
    elif prediction < 4.0:
        st.write("Good")
    elif prediction < 4.5:
        st.write("Very Good")
    else:
        st.write("Excellent")