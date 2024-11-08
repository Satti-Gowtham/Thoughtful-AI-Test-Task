import streamlit as st
from sort import sort

st.title("Package Sorting System")

# Input fields
width = st.number_input("Width (cm)", min_value=1.0, step=.5)
height = st.number_input("Height (cm)", min_value=1.0, step=.5)
length = st.number_input("Length (cm)", min_value=1.0, step=.5)
mass = st.number_input("Mass (kg)", min_value=.5, step=.5)

if st.button("Sort Package"):
    result = sort(width, height, length, mass)

    st.subheader(f"Package should be sent to the {result} stack.")
