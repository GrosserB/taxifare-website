import streamlit as st
import requests


'''
# Taxi Fare Prediction App
'''
# Collect input values from app user


pickup_date = st.text_input('Pickup Date Year-MM-DD', value='2013-07-06')
pickup_time = st.text_input('Pickup Time', value='17:18:00')
pickup_longitude = st.number_input('Pickup Longitude', value=40.7614327)
pickup_latitude = st.number_input('Pickup Latitude', value =-73.9798156)
dropoff_longitude = st.number_input('Dropoff Longitude', value=40.6513111)
dropoff_latitude = st.number_input('Dropoff Latitude', value=-73.8803331)
passenger_count = st.number_input('Number of Passengers', value=1)

pickup_datetime = f'{pickup_date} {pickup_time}'

# Build a dictionary to store these parameters so they can be passed into the API-request function


params_dict = {'pickup_datetime': pickup_datetime,
               'pickup_longitude': pickup_longitude,
                'pickup_latitude': pickup_latitude,
                'dropoff_longitude': dropoff_longitude,
                'dropoff_latitude': dropoff_latitude,
                'passenger_count': passenger_count}



# Pass the parameters into the API-request function. Take the 'fare' output of the response JSON and display it to the user

url = 'https://taxifare.lewagon.ai/predict'

response = requests.get(url=url, params=params_dict).json()['fare']

st.write('Fare prediction $ ', round(response, 2))
