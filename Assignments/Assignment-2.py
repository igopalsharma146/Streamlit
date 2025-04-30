"""
    Make a calculator that calculates the age of the person according to his birth date.
    """

import streamlit as st 
from datetime import datetime, date


st.header("Age Calculator")

st.image("https://images.pexels.com/photos/6345282/pexels-photo-6345282.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",width=200)
# st.subheader("Calculate your Age.")

# enter name
name=st.text_input("Please Enter your Name :")

if not name:
    st.warning("Name cannot be empty. Please enter your name!")
else:
    st.write(f"Mr. {name}, Please enter your Date of Birth")


min_date = date(1900, 1, 1)  # सबसे पुरानी तारीख़ जो चुनी जा सकती है
max_date = date.today()
date1= st.date_input("From",min_value=min_date,max_value=max_date)
date2= st.date_input("To")

button=st.button("Calculate Age")

if button:
    st.write(f"Thank you Mr. {name} , Your Responce has been submitted.")
    st.success(f"Calculating your age.")
    
from dateutil.relativedelta import relativedelta

age_difference=relativedelta(date2,date1)

if button:
    st.write(f"Age Difference:{age_difference.years} Years ,{age_difference.months} Months ,{age_difference.days} Days.")

