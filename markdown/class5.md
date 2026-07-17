以下是整理成**適合國小學生閱讀**的 Python 課堂筆記，用簡單的文字說明每個指令的用途，方便複習。

# 📖 Python 課堂筆記（圖片、購物網站、AI聊天機器人）

## 第一部分：顯示圖片 🖼️

### 1. 載入需要的工具

```python
import streamlit as st
import os
```

### 這是在做什麼？

- `streamlit`：可以快速做出網頁。
- `os`：可以操作電腦裡的資料夾和檔案。

---

### 2. 顯示標題

```python
st.title("圖片元件")
```

📌 功能：
在網頁最上方顯示一個大標題。

---

### 3. 顯示一張圖片

```python
st.image("image/apple.png", width=300)
```

📌 功能：
把圖片放到網頁上。

- `width=300`：圖片寬度是300像素。

---

### 4. 找出資料夾裡所有圖片

```python
image_folder = "image"
image_files = os.listdir(image_folder)
```

📌 功能：

假設 image 資料夾裡有：

```
image
├── apple.png
├── banana.png
└── orange.png
```

`os.listdir()` 就會得到

```python
["apple.png","banana.png","orange.png"]
```

---

### 5. 顯示資料夾裡有哪些圖片

```python
st.write(image_files)
```

📌 功能：

把剛剛找到的檔案名稱顯示出來。

---

### 6. 讓使用者決定圖片大小

```python
st.number_input(...)
```

例如：

```python
image_size = st.number_input(
    "圖片大小",
    min_value=50,
    max_value=500,
    step=50,
    value=100
)
```

📌 功能：

做出一個可以輸入數字的小工具。

意思是：

- 最小50
- 最大500
- 每次增加50
- 預設100

---

### 7. 使用 for 迴圈顯示所有圖片

```python
for image_file in image_files:
```

📌 功能：

一張一張把圖片拿出來。

例如：

```
apple.png
banana.png
orange.png
```

就會依序顯示三張圖片。

---

### 8. 依照使用者設定大小顯示圖片

```python
st.image(..., width=image_size)
```

📌 功能：

圖片大小會跟著使用者輸入改變。

---

### 9. 自動填滿畫面

```python
st.image(..., use_container_width=True)
```

📌 功能：

圖片會自動變成和畫面一樣寬。

---

### 10. 顯示成功訊息

```python
st.success("購買成功！")
```

畫面會出現綠色成功提示。

---

# 第二部分：購物平台 🛒

## 1. 設定網頁

```python
st.set_page_config(...)
```

可以設定：

- 網頁名稱
- 網頁圖示
- 網頁排版

---

## 2. session_state（很重要⭐⭐⭐）

```python
st.session_state
```

📌 功能：

就像一個**小背包**。

可以把資料放進去，不會因為重新整理就消失。

例如：

```python
購物車
總金額
聊天紀錄
```

都可以放在裡面。

---

## 3. 商品資料

```python
products = {
    ...
}
```

📌 功能：

把所有商品整理成一本「商品資料簿」。

每個商品都有：

- 名稱
- 價格
- 圖片
- Emoji

例如：

🍎蘋果

價格10元

圖片apple.png

---

## 4. 建立三欄

```python
cols = st.columns(3)
```

📌 功能：

把畫面分成三格。

像這樣：

```
🍎    🍌    🍊
```

---

## 5. enumerate()

```python
for idx, product in enumerate(...):
```

📌 功能：

除了知道資料內容，

還會知道它是第幾個。

例如：

```
0 蘋果
1 香蕉
2 橘子
```

---

## 6. with

```python
with cols[idx]:
```

📌 功能：

表示下面的東西都放到第 idx 欄。

---

## 7. try / except

```python
try:
    ...
except:
    ...
```

📌 功能：

如果程式出錯，

不要當掉，

改成顯示提醒。

例如：

圖片不見了

就顯示：

> 找不到圖片

---

## 8. os.path.exists()

```python
os.path.exists(...)
```

📌 功能：

檢查檔案存不存在。

有：

✅ True

沒有：

❌ False

---

## 9. Image.open()

```python
Image.open(...)
```

📌 功能：

打開圖片。

---

## 10. 加入購物車

按下

```python
st.button()
```

就可以：

- 檢查數量
- 放進購物車
- 更新總金額

---

## 11. st.warning()

黃色提醒。

例如：

⚠️ 請輸入數量。

---

## 12. st.info()

藍色資訊。

例如：

購物車是空的。

---

## 13. st.balloons()

🎈 放出很多氣球。

通常結帳成功會使用。

---

## 14. st.rerun()

重新整理整個網頁。

讓最新資料立刻更新。

---

# 第三部分：OpenAI AI聊天 🤖

## 1. 載入套件

```python
import openai
```

使用 OpenAI 的 AI。

---

## 2. 載入 .env

```python
load_dotenv()
```

把秘密資料讀進來。

例如：

API Key。

---

## 3. 取得 API Key

```python
os.getenv(...)
```

從 .env 找到金鑰。

---

## 4. 設定 API Key

```python
openai.api_key = ...
```

讓程式知道要使用哪個帳號。

---

## 5. input()

```python
input("你:")
```

在終端機等待使用者輸入。

---

## 6. while True

一直重複聊天。

直到輸入：

```
exit
```

或

```
quit
```

才停止。

---

## 7. AI聊天

```python
openai.chat.completions.create(...)
```

請 AI 回答問題。

裡面要設定：

- AI模型
- 對話內容

---

## 8. messages

```python
messages=[]
```

聊天紀錄。

裡面會放：

```
system
user
assistant
```

三種角色。

---

### role 是什麼？

#### system

告訴 AI 要遵守什麼規則。

例如：

請全部使用繁體中文。

---

#### user

使用者說的話。

---

#### assistant

AI 回答的內容。

---

## 9. append()

```python
messages.append(...)
```

把新的聊天內容加到最後。

例如：

```
你好
```

加入聊天紀錄。

---

# 第四部分：Streamlit 聊天介面 💬

## 1. 聊天泡泡

```python
st.chat_message()
```

可以做出聊天介面。

例如：

🧒：

你好

🤖：

你好！

---

## 2. avatar

```python
avatar="🪄"
```

可以換頭像。

例如：

🪄

✨

😀

🐱

都可以。

---

## 3. st.chat_input()

建立聊天輸入框。

使用者可以直接輸入訊息。

---

## 4. 顯示聊天紀錄

利用

```python
for
```

把每一句聊天重新顯示。

---

## 5. 清空聊天

按按鈕後：

```python
st.session_state.history = []
```

聊天紀錄全部清空。

---

## 6. st.text_input()

建立文字輸入框。

例如：

修改 AI 的系統訊息。

---

## 7. st.selectbox()

建立下拉式選單。

例如：

可以選擇：

- gpt-4o-mini
- gpt-4
- gpt-4o-search-preview

---

# 🌟 今天學到的重要指令整理

| 指令                               | 功能                 |
| ---------------------------------- | -------------------- |
| `import`                           | 載入工具             |
| `st.title()`                       | 顯示標題             |
| `st.write()`                       | 顯示文字或資料       |
| `st.image()`                       | 顯示圖片             |
| `st.number_input()`                | 輸入數字             |
| `st.text_input()`                  | 輸入文字             |
| `st.chat_input()`                  | 聊天輸入框           |
| `st.chat_message()`                | 聊天泡泡             |
| `st.button()`                      | 按鈕                 |
| `st.success()`                     | 成功提示             |
| `st.warning()`                     | 警告提示             |
| `st.info()`                        | 資訊提示             |
| `st.columns()`                     | 分欄排版             |
| `st.session_state`                 | 暫存資料（像小背包） |
| `st.rerun()`                       | 重新整理畫面         |
| `st.balloons()`                    | 放氣球動畫           |
| `for`                              | 重複做事情           |
| `if`                               | 判斷條件             |
| `while`                            | 一直重複執行         |
| `try / except`                     | 避免程式出錯停止     |
| `append()`                         | 新增資料到列表       |
| `os.listdir()`                     | 取得資料夾裡所有檔案 |
| `os.path.exists()`                 | 檢查檔案是否存在     |
| `Image.open()`                     | 打開圖片             |
| `openai.chat.completions.create()` | 呼叫 AI 回答問題     |

# 🎯 今天學會了什麼？

今天我們學會了：

✅ 在網頁顯示圖片。
✅ 使用迴圈一次顯示很多圖片。
✅ 建立簡單的購物平台。
✅ 使用購物車記住購買的商品。
✅ 使用 OpenAI API 與 AI 聊天。
✅ 建立聊天介面，讓 AI 和使用者像聊天軟體一樣互動。
✅ 使用 `st.session_state` 保存聊天紀錄和購物車資料，讓資料不會因重新整理而消失。
