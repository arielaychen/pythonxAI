import streamlit as st
import random

# 初始化遊戲狀態
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.message = ""
    st.session_state.low = 1      # 目前最小範圍
    st.session_state.high = 100   # 目前最大範圍

st.title("🎯 猜數字遊戲")
st.write(f"請猜一個 {st.session_state.low}~{st.session_state.high} 之間的數字")

# 顯示提示訊息
if st.session_state.message:
    st.markdown(st.session_state.message)

# 顯示目前範圍
st.info(f"📌 目前範圍：{st.session_state.low} ~ {st.session_state.high}")

# 數字輸入（範圍會動態更新）
guess = st.number_input(
    "請輸入你猜的數字：", 
    step=1, 
    min_value=st.session_state.low, 
    max_value=st.session_state.high, 
    key="guess_input"
)

# 猜按鈕
col1, col2 = st.columns(2)
with col1:
    if st.button("🔍 猜看看", key="guess_btn"):
        if st.session_state.game_over:
            st.warning("遊戲已經結束囉！請按「重新開始」")
        else:
            st.session_state.attempts += 1
            
            if guess == st.session_state.secret_number:
                st.session_state.message = f"🎉 恭喜你猜對了！答案是 {st.session_state.secret_number}，你總共猜了 {st.session_state.attempts} 次！"
                st.session_state.game_over = True
                st.balloons()  # 猜對時氣球飛出來
                
            elif guess > st.session_state.secret_number:
                st.session_state.high = guess - 1  # 縮小範圍：上限變成猜的數字-1
                st.session_state.message = f"❌ 太大了！{guess} 太大了，範圍縮小為 {st.session_state.low}~{st.session_state.high}"
                
            else:  # guess < secret_number
                st.session_state.low = guess + 1   # 縮小範圍：下限變成猜的數字+1
                st.session_state.message = f"❌ 太小了！{guess} 太小了，範圍縮小為 {st.session_state.low}~{st.session_state.high}"

with col2:
    if st.button("🔄 重新開始", key="restart_btn"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.message = "遊戲已重新開始！"
        st.session_state.low = 1
        st.session_state.high = 100
        st.rerun()

# 顯示遊戲狀態
st.write("---")
st.write(f"📊 已猜次數：{st.session_state.attempts}")
if st.session_state.game_over:
    st.success(f"🎯 答案就是 {st.session_state.secret_number}")
else:
    st.info(f"💡 提示：數字在 {st.session_state.low}~{st.session_state.high} 之間")