import streamlit as st
from predictor import predict


st.title("Wildfire Spread Analysis")
st.write("This model works on the algorithm named Random Forest Regressor")

temperature = st.number_input("Temperature (°C) (20-50)", min_value=-20.0, max_value=50.0, value=20.0)
windspeed = st.number_input("Windspeed (km/h) (5-30)", min_value=5.0, max_value=30.0, value=10.0)
fuel_moisture_code = st.number_input("Fuel Moisture Code (25-93)", min_value=25, max_value=93, value=50)
duff_moisture_code = st.number_input("Duff Moisture Code  (1-65)", min_value=1, max_value=65, value=50)
initial_spread_index = st.number_input("Initial Spread Index  (1-5)", min_value=0.0, max_value=5.0, value=2.0)

if st.button("Submit"):
    input_data = {
        'Temperature': temperature,
        'Windspeed': windspeed,
        'Fuel Moisture Code ': fuel_moisture_code,
        'Duff Moisture Code': duff_moisture_code,
        'Initial Spread Index': initial_spread_index
    }
    
    st.write("Input Data:")
    st.json(input_data)


    predictionmaybe = predict(input_data)

    if predictionmaybe < 0.17 and predictionmaybe >= 0:
        st.success('The probability of a wildfire occurring is VERY LOW based on the current conditions')
    elif predictionmaybe > 0.17 and predictionmaybe <= 0.50:
        st.success('The probability of a wildfire occurring is MODERATE based on the current conditions')
    else:
        st.success('The probability of a wildfire occurring is VERY HIGH based on the current conditions')


 