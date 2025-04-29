import streamlit as st 

st.title("Hello Chai App")
st.subheader("Brewed With Streamlit.")
st.text("Welcome to your First interective app")
st.write("Choose your favourite varity of chai.")

chai=st.selectbox("Your fav. chai : ",["Masala chai","Kesar Chai","Adrak Chai","Lemon Tea"])
st.write(f"You are choose {chai}. Excellent Choice.")

st.success("Your chai has been brewed.")
