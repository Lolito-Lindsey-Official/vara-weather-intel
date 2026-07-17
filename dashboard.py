import streamlit as st
from weather import get_weather
from decision import decision_engine

st.title("🌦️VARA Weather Intel")
st.subheader(" Decision Intelligence Prototype")

city = st.text_input("Enter a city: ")

if st.button("Analyze"):
  weather_data = get_weather(city)

  temp = weather_data["main"]["temp"]
  condition = weather_data["weather"][0]["description"]
  humidity = weather_data["main"]["humidity"]
  wind = weather_data["wind"]["speed"]
  visibility = weather_data["visibility"] / 1000

  st.divider()
  st.subheader(city.title())
  st.write(f"🌡️ Temperature {temp: .1f} C")
  st.write(f"☁️Conditions {condition.title()}")
  st.write(f"💧Humidity {humidity}%")
  st.write(f"💨Wind Speed {wind} m/s")
  st.write(f"👀Visibility {visibility: .1f} km")

  st.divider()
  st.subheader("Decision Guidance")

  decision = decision_engine(condition, temp, wind, humidity, visibility)

  st.write(decision)



