import requests
import os
from datetime import datetime
import streamlit as st  

def show_weather():
    user_api_key = os.environ.get("api_key")  
    location = st.text_input("Enter location:", "Hyderabad")

    if st.button("Get Weather"):
        if not user_api_key:
            st.error("❌ API key not found. Set your OpenWeatherMap API key as an environment variable named `api_key`.")
            return

        complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api_key}"
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data.get('cod') == '404':
            st.error(f"Invalid city: {location}, please check your city name.")
        else:
            temp_city = api_data['main']['temp'] - 273.15
            weather_desc = api_data['weather'][0]['description'].capitalize()
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

            st.markdown(f"### 🌦️ Weather for **{location.upper()}**  — {date_time}")
            st.write(f"**Temperature:** {temp_city:.2f}°C")
            st.write(f"**Description:** {weather_desc}")
            st.write(f"**Humidity:** {hmdt}%")
            st.write(f"**Wind Speed:** {wind_spd} km/h")
