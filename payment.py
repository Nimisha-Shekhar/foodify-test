import streamlit as st 
import json
import os 

def payment_foodify():
    st.title("SELECT THE RESPECTIVE PAYMENT OPTION:")
    st.button("GPAY",type="primary")
    st.button("PhonePE",type="primary")
    st.button("UPI",type="primary")
    st.button("Cash On Delivery",type="primary")
    st.title("RATE FOODIFY:")
    feedback=st.select_slider('Select',['Needs Improvement','Bad','Good','Outstanding'])
    st.write("You Selected:",feedback)
    