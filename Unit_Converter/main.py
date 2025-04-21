import streamlit as st

# Page Setup
st.set_page_config(
    page_title="Universal Unit Converter",
    page_icon="🧮",
    layout="centered"
)

# Dictionary containing conversion factors relative to a base unit for each category
conversion_factors = {
    "Length": {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254,
        "Nautical Mile": 1852,
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 1e-6,
        "Tonne": 1000,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    },
    "Temperature": {
        "Celsius": None,       # Custom logic needed
        "Fahrenheit": None,    # Custom logic needed
        "Kelvin": None,        # Custom logic needed
    },
    "Time": {
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month": 2629746,      # Approximate average
        "Year": 31556952,      # Approximate average
    },
    "Speed": {
        "Meter per second": 1,
        "Kilometer per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Knot": 0.514444,
    },
    "Area": {
        "Square meter": 1,
        "Square kilometer": 1e6,
        "Square mile": 2.59e6,
        "Square yard": 0.836127,
        "Square foot": 0.092903,
        "Square inch": 0.00064516,
        "Hectare": 10000,
        "Acre": 4046.86,
    },
}

# Title
st.title("🌐 Unit Converter")

# Description
st.write("Convert values between different units like Length, Weight, Temperature, Time, Speed, and Area.")

# Dropdown menu (Length, Weight, etc.)
category = st.selectbox("Select a category", list(conversion_factors.keys()))

# Populate "From" and "To" unit dropdowns based on selected category
units = list(conversion_factors[category].keys())
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", [unit for unit in units if unit != from_unit])  # Prevent selecting the same unit

# Input field to enter the value
value = st.number_input("Enter the value to convert", step=1.0, format="%.4f")

# Conversion function
def convert(category, value, from_unit, to_unit):
    # Handle temperature conversions separately
    if category == "Temperature":
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius":
            return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
        elif from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    else:
        # Convert input value to base unit and then to target unit
        factor_from = conversion_factors[category][from_unit]
        factor_to = conversion_factors[category][to_unit]
        return value * factor_from / factor_to

# Trigger conversion on button click
if st.button("Convert"):
    result = convert(category, value, from_unit, to_unit)
    # Display result rounded to 4 decimal places
    st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")