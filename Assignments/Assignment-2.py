"""
    Make a calculator that calculates the age of the person according to his birth date.
    """

import streamlit as st 

st.header("Age Calculator")
st.subheader("Calculate your Age.")

# enter name
name=st.text_input("Please Enter your Name :")

if name:
    st.write(f"Mr. {name} Please ,Enter your Date of Birth")

date1= st.date_input("From")
date2= st.date_input("To")

button=st.button("Calculate Age")

if button:
    st.write(f"Thank you Mr. {name} , Your Responce has been submitted.")
    st.success(f"Calculating your age.")
    
from dateutil.relativedelta import relativedelta

age_difference=relativedelta(date2,date1)
st.write(f"Age Difference:{age_difference.years} Years ,{age_difference.months} Months ,{age_difference.days} Days.")

