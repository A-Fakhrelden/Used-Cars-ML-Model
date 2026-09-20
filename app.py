import streamlit as st
import pandas as pd
import joblib
df=pd.read_csv('Used.csv')

# Load the trained model
model = joblib.load('car_price_predictor.pkl')

# Now you can use the model to make predictions or any other operations

# Function to predict car price
def predict_car_price(features):
    # Convert the features list to a pandas DataFrame
    feature_columns = ['Year', 'Kilometers_Driven', 'Mileage', 'Engine', 'Power', 'Seats', 
                       'Location', 'Fuel_Type', 'Transmission', 'Owner_Type', 'Car_maker', 'Car_model']
    
    # Create a DataFrame with the input features
    input_df = pd.DataFrame([features], columns=feature_columns)
    
    # Predict the price using the pipeline
    prediction = model.predict(input_df)
    
    return prediction[0]

# Streamlit UI elements
st.title("Car Price Prediction")

# Input form
year = st.number_input('Year of Manufacture', min_value=1900, max_value=2025, value=2020)
kilometers_driven = st.number_input('Kilometers Driven', min_value=0, value=50000)
mileage = st.number_input('Mileage (km/l)', min_value=0.0, value=15.0)
engine = st.number_input('Engine Capacity (cc)', min_value=0, value=1500)
power = st.number_input('Power (bhp)', min_value=0, value=100)
seats = st.number_input('Seats', min_value=2, max_value=10, value=5)

car_maker = st.selectbox('Brand', df['Car_maker'].unique())
car_model = st.selectbox('Model', df['Car_model'].unique())
location = st.selectbox('Location', ['Location_1', 'Location_2', 'Location_3'])  # Update with actual locations
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'Electric'])  # Update with actual fuel types
transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])  # Update with actual transmission types
owner_type = st.selectbox('Owner Type', ['First', 'Second', 'Third'])  # Update with actual owner types

# If the "Predict" button is pressed, predict the car price
if st.button('Predict'):
    # Prepare the input data
    input_data = [year, kilometers_driven, mileage, engine, power, seats, location, fuel_type, transmission, owner_type, car_maker, car_model]
    
    # Predict the price
    predicted_price = predict_car_price(input_data)
    
    # Display the predicted price
    st.subheader(f"Predicted Car Price: {predicted_price:.2f}K $")
