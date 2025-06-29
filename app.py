import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib

st.set_page_config(layout="wide")

# Load scaler and model with error handling
@st.cache_resource
def load_models():
    try:
        scaler = joblib.load("scaler.pkl")
        model = joblib.load("mlmodel.pkl")
        return scaler, model
    except Exception as e:
        st.error(f"Error loading models: {e}")
        st.stop()

# Load models once
scaler, model = load_models()

st.title("Restaurant Rating Prediction App")
st.caption("This app helps you predict a restaurant's rating")
st.divider()

# User inputs
averagecost = st.number_input("Please enter the average cost for two", min_value=50, max_value=100000, value=1000, step=200)
tablebooking = st.selectbox("Restaurant has table booking or not: ", ["Yes", "No"])
onlinedelivery = st.selectbox("Restaurant has online delivery?", ["Yes", "No"])
pricerange = st.selectbox("What is the price range (1 = Cheapest, 4 = Most Expensive)", [1, 2, 3, 4])

predictbutton = st.button("Predict the rating")

if predictbutton:
    try:
        # Convert categorical inputs to numerical
        bookingstatus = 1 if tablebooking == "Yes" else 0
        deliverystatus = 1 if onlinedelivery == "Yes" else 0
        
        # Prepare input array
        values = [[averagecost, bookingstatus, deliverystatus, pricerange]]
        my_X_values = np.array(values)
        
        # Scale the input
        X = scaler.transform(my_X_values)
        
        # Make prediction
        prediction = model.predict(X)[0]  # Get single prediction value
        
        st.snow()
        st.write(f"Predicted Rating: {prediction:.2f}")
        
        # Rating categories
        if prediction < 2.5:
            st.write("**Rating Category: Poor** 😞")
        elif prediction < 3.5:
            st.write("**Rating Category: Average** 😐")
        elif prediction < 4.0:
            st.write("**Rating Category: Good** 😊")
        elif prediction < 4.5:
            st.write("**Rating Category: Very Good** 😍")
        else:
            st.write("**Rating Category: Excellent** 🌟")
            
    except Exception as e:
        st.error(f"Prediction error: {e}")
        st.write("Please check your inputs and try again.")
