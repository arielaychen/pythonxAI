import streamlit as st

number = st.number_input("請輸入一個數字", step=1, min_value=1, max_value=9)
st.markdown(f"你輸入的數字是: {number}")

for i in range(1,number+1):
    st.markdown(str(i)*i)