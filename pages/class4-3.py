# 購物平台 - shopping_platform.py
import streamlit as st
from PIL import Image
import os

# 設定頁面標題和圖示
st.set_page_config(
    page_title="購物平台",
    page_icon="🛒",
    layout="wide"
)

# 初始化購物車
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "total_price" not in st.session_state:
    st.session_state.total_price = 0

# 商品資料
products = {
    "apple": {
        "name": "蘋果",
        "price": 10,
        "image": "image/apple.png",  # 修改為 image 資料夾
        "emoji": "🍎"
    },
    "banana": {
        "name": "香蕉",
        "price": 10,
        "image": "image/banana.png",  # 修改為 image 資料夾
        "emoji": "🍌"
    },
    "orange": {
        "name": "橘子",
        "price": 10,
        "image": "image/orange.png",  # 修改為 image 資料夾
        "emoji": "🍊"
    }
}

# 顯示標題
st.title("🛒 歡迎來到購物平台")
st.write("---")



# 使用欄位顯示商品
st.write("## 🛍️ 商品列表")

# 創建3欄顯示商品
cols = st.columns(3)

for idx, (key, product) in enumerate(products.items()):
    with cols[idx]:
        st.markdown(f"### {product['emoji']} {product['name']}")
        
        # 嘗試顯示圖片
        try:
            if os.path.exists(product['image']):
                image = Image.open(product['image'])
                st.image(image, width=200)
            else:
                st.info(f"📷 圖片 {product['image']} 未找到")
        except Exception as e:
            st.info(f"📷 圖片 {product['image']} 無法載入")
        
        st.write(f"💰 價格: ${product['price']} 元")
        
        # 數量選擇
        qty = st.number_input(
            f"購買數量",
            min_value=0,
            max_value=100,
            step=1,
            key=f"qty_{key}"
        )
        
        # 加入購物車按鈕
        if st.button(f"🛒 加入購物車", key=f"add_{key}"):
            if qty > 0:
                if key in st.session_state.cart:
                    st.session_state.cart[key] += qty
                else:
                    st.session_state.cart[key] = qty
                st.session_state.total_price += qty * product['price']
                st.success(f"✅ 已加入 {qty} 個 {product['name']} 到購物車！")
                st.rerun()
            else:
                st.warning("⚠️ 請選擇購買數量（要大於0）")
        
        st.write("---")

# 購物車區域
st.write("## 🛒 購物車")

# 顯示購物車內容
if st.session_state.cart:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.write("#### 商品清單")
        for key, qty in st.session_state.cart.items():
            product = products[key]
            st.write(f"{product['emoji']} {product['name']} x {qty} = ${qty * product['price']} 元")
    
    with col2:
        st.write("#### 總計")
        st.write(f"💰 總金額: **${st.session_state.total_price}** 元")
        
        # 結帳按鈕
        if st.button("💳 結帳"):
            st.success(f"🎉 感謝您的購買！總共 ${st.session_state.total_price} 元")
            st.balloons()
            # 清空購物車
            st.session_state.cart = {}
            st.session_state.total_price = 0
            st.rerun()
        
        # 清空購物車按鈕
        if st.button("🗑️ 清空購物車"):
            st.session_state.cart = {}
            st.session_state.total_price = 0
            st.warning("購物車已清空")
            st.rerun()
else:
    st.info("🛒 購物車是空的，請選購商品吧！")

# 顯示底部資訊
st.write("---")
st.write("### 📋 購物須知")
st.write("""
- 💰 所有商品均為 10 元
- 📦 單次購買數量上限 100 個
- ✅ 選購完畢後請點擊「結帳」按鈕
""")

# 顯示背景圖片（如果存在）
try:
    bg_path = "image/bg.png"  # 修改為 image 資料夾
    if os.path.exists(bg_path):
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("{bg_path}");
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
except:
    pass

