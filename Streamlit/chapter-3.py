import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala Chai")
    st.image("https://images.pexels.com/photos/16228436/pexels-photo-16228436/free-photo-of-a-table-with-a-tea-pot-and-a-candle-on-it.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=200)
    vote1 = st.button("Vote Masala Chai")

with col2:
    st.header("Adrak Chai")
    st.image("https://images.pexels.com/photos/29054033/pexels-photo-29054033/free-photo-of-elegant-overhead-view-of-tea-on-checkered-tablecloth.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", width=200)
    vote2 = st.button("Vote Adrak Chai")

if vote1:
    st.success("Thanks for voting masala Chai")
elif vote2:
    st.success("Thanks for voting Adrak Chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "kesar", "Adrak"])

st.write(f"Welcome {name} and your {tea} chai is getting ready")


with st.expander("Show Chai Making INstructions"):
    st.write("""
    1. Boil water with tea leaves
    2. Add milk and spices
    3. Serve hot
""")
    
st.markdown('# Welcome to Chai App')
st.markdown('> Blockquote ')