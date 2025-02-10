
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('linear_regression_model.pkl')

# Streamlit App Title
st.title('Car Selling Price Prediction')

# User Inputs
year = st.number_input('Year of Manufacture', min_value=1980, max_value=2025, value=2015)
km_driven = st.number_input('Kilometers Driven', min_value=0, max_value=500000, value=50000)
mileage = st.number_input('Mileage (km/l)', min_value=0.0, max_value=50.0, value=20.0)
engine = st.number_input('Engine Capacity (cc)', min_value=500, max_value=5000, value=1500)
max_power = st.number_input('Max Power (bhp)', min_value=20.0, max_value=500.0, value=100.0)
seats = st.number_input('Number of Seats', min_value=2, max_value=14, value=5)

# Predict Button
if st.button('Predict Selling Price'):
    input_data = pd.DataFrame([[year, km_driven, mileage, engine, max_power, seats]], 
                              columns=['year', 'km_driven', 'mileage(km/ltr/kg)', 'engine', 'max_power', 'seats'])
    prediction = model.predict(input_data)
    st.success(f'Estimated Selling Price: ₹ {int(prediction[0])}')
