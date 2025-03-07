import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Streamlit UI
st.title("🔄 Google-Style Unit Converter")
st.write("Convert between different units easily!")

# Unit categories
categories = {
    "Length": ["meter", "kilometer", "mile", "inch", "foot", "yard"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "cup"],
    "Time": ["second", "minute", "hour", "day"]
}

# Select category
category = st.selectbox("Choose a category:", list(categories.keys()))

# Select units
from_unit = st.selectbox("From:", categories[category])
to_unit = st.selectbox("To:", categories[category])

# Input value
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Convert button
if st.button("Convert"):
    try:
        converted_value = (value * ureg(from_unit)).to(to_unit)
        st.success(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
    except Exception as e:
        st.error(f"Conversion error: {e}")


