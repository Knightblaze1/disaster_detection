# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import requests
from sklearn.ensemble import RandomForestClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Conv2D, MaxPooling2D, Flatten
from twilio.rest import Client
import folium
from streamlit_folium import folium_static

# Twilio credentials (replace with your own)
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_number"
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Fetch flood data (example: river levels)
def fetch_flood_data():
    url = "https://water.weather.gov/ahps2/hydrograph_to_xml.php?gage=abcd&output=csv"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(url)
    else:
        raise Exception("Failed to fetch flood data")

# Fetch tsunami data (example: DART buoy data)
def fetch_tsunami_data():
    url = "https://www.ndbc.noaa.gov/data/realtime2/ABCD.txt"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(url, delim_whitespace=True)
    else:
        raise Exception("Failed to fetch tsunami data")

# Fetch tornado data (example: weather data)
def fetch_tornado_data():
    url = "https://www.spc.noaa.gov/climo/reports/today.csv"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(url)
    else:
        raise Exception("Failed to fetch tornado data")

# Fetch wildfire data (example: NASA FIRMS)
def fetch_wildfire_data():
    url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Global_7d.csv"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(url)
    else:
        raise Exception("Failed to fetch wildfire data")

# Fetch earthquake data (example: USGS)
def fetch_earthquake_data():
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(url)
    else:
        raise Exception("Failed to fetch earthquake data")

# LSTM model for flood prediction
def build_flood_model():
    model = Sequential([
        LSTM(50, input_shape=(10, 1)),  # 10 time steps, 1 feature
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

# Random Forest model for tornado prediction
def build_tornado_model():
    model = RandomForestClassifier(n_estimators=100)
    return model

# CNN model for wildfire detection
def build_wildfire_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Send SMS alerts
def send_alert(phone_number, message):
    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    return message.sid

# Streamlit dashboard
def main():
    st.title("Disaster Detection and Alert System")
    st.sidebar.header("Settings")
    phone_number = st.sidebar.text_input("Enter your phone number for alerts")

    # Flood prediction
    st.header("Flood Detection")
    flood_data = fetch_flood_data()
    st.write("River Level Data:", flood_data.head())
    if st.button("Predict Flood Risk"):
        model = build_flood_model()
        # Train model (example)
        X = np.array(flood_data['level']).reshape(-1, 10, 1)
        y = np.array(flood_data['level']).reshape(-1, 1)
        model.fit(X, y, epochs=10, verbose=0)
        prediction = model.predict(X[-1].reshape(1, 10, 1))
        st.write(f"Predicted River Level: {prediction[0][0]}")
        if prediction[0][0] > 10:  # Example threshold
            st.warning("Flood risk detected!")
            if phone_number:
                send_alert(phone_number, "Flood risk detected in your area!")

    # Tsunami detection
    st.header("Tsunami Detection")
    tsunami_data = fetch_tsunami_data()
    st.write("DART Buoy Data:", tsunami_data.head())
    if st.button("Check Tsunami Risk"):
        seismic_activity = tsunami_data['seismic'].iloc[-1]
        ocean_level = tsunami_data['level'].iloc[-1]
        if seismic_activity > 5 and ocean_level > 1:  # Example thresholds
            st.warning("Tsunami risk detected!")
            if phone_number:
                send_alert(phone_number, "Tsunami risk detected in your area!")

    # Tornado prediction
    st.header("Tornado Detection")
    tornado_data = fetch_tornado_data()
    st.write("Weather Data:", tornado_data.head())
    if st.button("Predict Tornado Risk"):
        model = build_tornado_model()
        # Train model (example)
        X = tornado_data[['wind_speed', 'pressure']]
        y = tornado_data['tornado_risk']
        model.fit(X, y)
        prediction = model.predict(X.iloc[-1].values.reshape(1, -1))
        st.write(f"Predicted Tornado Risk: {prediction[0]}")
        if prediction[0] == 1:  # Example threshold
            st.warning("Tornado risk detected!")
            if phone_number:
                send_alert(phone_number, "Tornado risk detected in your area!")

    # Wildfire detection
    st.header("Wildfire Detection")
    wildfire_data = fetch_wildfire_data()
    st.write("Wildfire Data:", wildfire_data.head())
    if st.button("Check Wildfire Risk"):
        model = build_wildfire_model()
        # Train model (example)
        X = np.random.rand(100, 64, 64, 3)  # Replace with actual image data
        y = np.random.randint(2, size=100)
        model.fit(X, y, epochs=10, verbose=0)
        prediction = model.predict(X[-1].reshape(1, 64, 64, 3))
        st.write(f"Predicted Wildfire Risk: {prediction[0][0]}")
        if prediction[0][0] > 0.5:  # Example threshold
            st.warning("Wildfire risk detected!")
            if phone_number:
                send_alert(phone_number, "Wildfire risk detected in your area!")

    # Earthquake detection
    st.header("Earthquake Detection")
    earthquake_data = fetch_earthquake_data()
    st.write("Earthquake Data:", earthquake_data.head())
    if st.button("Check Earthquake Risk"):
        magnitude = earthquake_data['mag'].iloc[-1]
        if magnitude > 5:  # Example threshold
            st.warning("Earthquake risk detected!")
            if phone_number:
                send_alert(phone_number, "Earthquake risk detected in your area!")

    # Interactive map
    st.header("Global Disaster Map")
    m = folium.Map(location=[20, 0], zoom_start=2)
    for _, row in wildfire_data.iterrows():
        folium.CircleMarker(
            location=(row['latitude'], row['longitude']),
            radius=5,
            color='red',
            fill=True
        ).add_to(m)
    folium_static(m)

if __name__ == "__main__":
    main()