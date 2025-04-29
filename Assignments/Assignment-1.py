"""
    make a language app, in which we are select the language.
    """


import streamlit as st 

st.title("Code Runner")
st.subheader("Programming app.")
st.write("Choose your language.")

language=st.selectbox("Choose any one language : ",["Python","Java","C","C++","Java Script","Django"])
st.write("Excellent choice.")
st.success(f"Now You Can Write Here Your {language} Code.")