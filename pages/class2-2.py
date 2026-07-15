import streamlit as st # 匯入streamlit模組並重新命名為st

# st.number_input()可以讓可以讓使用者輸入數字,設定step=1可以讓使用者只能輸入整數
# min_value=0設定最小值為0,max_value=100可以設定最大值為100
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100)
# st.markdown()可以在網頁使用markdown語法顯示文字
st.markdown(f"你輸入的數字是: {number}") 

number = st.number_input("請輸入你的分數", step=1, min_value=0, max_value=100)
if number>=90:
    st.markdown("你的成績是A")
elif number>=80:
    st.markdown("你的成績是B")
elif number>=70:
    st.markdown("你的成績是C")

elif number>=60:
    st.markdown("你的成績是D")
else:
    st.markdown("你的成績是f")

st.markdown("---")
st.markdown("### 按鈕練習")
# st.button()可以在網頁上顯示一個按鈕,使用者可以點擊按鈕
# key按鈕的識別名稱,可以用來區分不同的按鈕
# 如果使用者點擊按鈕,st.button()會回傳True,否則回傳False
if st.button("按我一下", key="button1"):
    st.markdown("你按了按鈕1")
else:
    st.markdown("你沒有按按鈕1")
if st.button("按我一下", key="balloons"):
    st.balloons()
if st.button("按我一下", key="snow"):
    st.snow()
if st.button("按我一下", key="T-rex"):
    st.Trex()
st.markdown("---")