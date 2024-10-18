- 👋 import streamlit as st

# Title of the app
st.title("Temperature Converter")

# Dropdown for selecting the conversion type
conversion_type = st.selectbox("Choose conversion type", 
                               ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Input field for temperature value
temp_input = st.number_input("Enter the temperature to convert", value=0.0)

# Perform the conversion
if conversion_type == "Celsius to Fahrenheit":
    converted_temp = (temp_input * 9/5) + 32
    st.success(f"{temp_input}°C is equal to {converted_temp}°F")
elif conversion_type == "Fahrenheit to Celsius":
    converted_temp = (temp_input - 32) * 5/9
    st.success(f"{temp_input}°F is equal to {converted_temp}°C")


