以下是整理成**適合國小學生閱讀**的 Python 課堂筆記，用簡單、容易理解的方式說明。

# 🐍 Python 入門筆記

## 1. 什麼是 Python？

Python 是一種程式語言，就像和電腦說話的方法。我們可以用 Python 做遊戲、網站、AI、機器人，還可以幫忙計算很多事情。

---

# 🖨️ 2. print()：讓電腦顯示文字

`print()` 可以把文字或數字顯示在畫面上。

### 範例

```python
print("Hello World!")
print("我是小明")
print(100)
```

畫面會顯示：

```
Hello World!
我是小明
100
```

### 換行

`\n` 表示「換到下一行」。

```python
print("第一行\n第二行")
```

會顯示：

```
第一行
第二行
```

---

# 💬 3. 註解（給人看的說明）

註解是寫給自己或其他人看的，Python 不會執行。

## 單行註解

```python
# 這是一行註解
```

## 多行註解

```python
"""
這是第一行
這是第二行
"""
```

💡 小技巧：

按 **Ctrl + /** 可以快速註解或取消註解。

---

# 📦 4. 資料型態（資料的種類）

Python 有很多不同種類的資料。

| 型態  | 名稱           | 範例             |
| ----- | -------------- | ---------------- |
| int   | 整數           | 10、50           |
| float | 小數           | 3.14、5.8        |
| str   | 文字（字串）   | "apple"、"Hello" |
| bool  | 布林值（真假） | True、False      |

例如：

```python
print(10)
print(3.14)
print("apple")
print(True)
```

---

# 📦 5. 變數（放資料的小盒子）

變數就像一個有名字的小盒子，可以把資料放進去。

```python
name = "小明"
age = 10
```

要使用時：

```python
print(name)
print(age)
```

如果重新放新的東西，舊的內容就會被換掉。

```python
name = "小美"
```

---

# ➕ 6. 數學運算

Python 可以幫我們算數學。

| 符號 | 功能     | 範例       |
| ---- | -------- | ---------- |
| +    | 加法     | 3+2        |
| -    | 減法     | 5-2        |
| \*   | 乘法     | 4\*3       |
| /    | 除法     | 8/2        |
| //   | 取整數商 | 7//2 = 3   |
| %    | 取餘數   | 7%2 = 1    |
| \*\* | 次方     | 2\*\*3 = 8 |

---

# 📖 7. 運算順序

算式會照下面順序計算：

1. () 括號
2. \*\* 次方
3. - / // %
4. - -

例如：

```python
print((2+3)*4)
```

---

# 🔤 8. 字串運算

文字也可以運算。

## 合併文字

```python
print("apple" + "pen")
```

結果：

```
applepen
```

## 重複文字

```python
print("Hi!" * 3)
```

結果：

```
Hi!Hi!Hi!
```

---

# 😊 9. f 字串（把資料放進句子裡）

可以把變數放進一句話中。

```python
name = "小明"
age = 10

print(f"我是{name}，今年{age}歲。")
```

結果：

```
我是小明，今年10歲。
```

---

# 📏 10. len()：算有幾個字

```python
print(len("apple"))
```

結果：

```
5
```

因為 apple 有 5 個字母。

---

# 🔍 11. type()：看看資料是什麼種類

```python
print(type(10))
print(type(3.14))
print(type("apple"))
print(type(True))
```

可以知道它是整數、小數、文字還是真假值。

---

# 🔄 12. 資料型態轉換

有時候要把資料變成另一種型態。

例如：

```python
int(3.8)
```

變成：

```
3
```

其他常用轉換：

```python
int()      # 變整數
float()    # 變小數
str()      # 變文字
bool()     # 變 True 或 False
```

⚠️ 注意：

```python
int("hello")
```

會出錯，因為 hello 不是數字。

---

# ⌨️ 13. input()：請使用者輸入資料

可以請使用者輸入資料。

```python
name = input("請輸入名字：")
print(name)
```

如果要算數學，要先變成數字：

```python
age = int(input("請輸入年齡："))
```

或

```python
r = float(input("請輸入半徑："))
```

---

# 🟠 14. 計算圓面積

公式：

```
圓面積 = 3.14 × 半徑 × 半徑
```

程式：

```python
r = float(input("請輸入半徑："))
print(f"圓面積是：{3.14 * r**2}")
```

---

# 📚 15. 計算平均成績

例如：

```python
mid = float(input("請輸入期中成績："))
final = float(input("請輸入期末成績："))

print(f"平均成績：{(mid+final)/2}")
```

---

# 🌐 16. Streamlit（做網頁）

Streamlit 可以把 Python 做成漂亮的網頁。

先匯入：

```python
import streamlit as st
```

---

## st.title()

做最大的標題。

```python
st.title("我的第一個網站")
```

---

## st.write()

可以顯示很多不同資料。

```python
st.write("Hello")
st.write(100)
```

---

## st.text()

只能顯示普通文字。

```python
st.text("Hello")
```

---

## st.markdown()

可以做漂亮的排版。

例如：

```python
st.markdown("# 大標題")
```

還可以：

- 做項目清單
- 粗體文字
- 斜體文字
- 放圖片
- 放連結
- 顯示程式碼

例如：

```markdown
# 大標題

## 第二層標題

- 蘋果
- 香蕉
- 西瓜

**粗體**

_斜體_
```

---

# ⭐ 今天學到的重要指令

| 指令                   | 功能             |
| ---------------------- | ---------------- |
| print()                | 顯示資料         |
| input()                | 接收使用者輸入   |
| len()                  | 計算長度         |
| type()                 | 查看資料型態     |
| int()                  | 轉整數           |
| float()                | 轉小數           |
| str()                  | 轉文字           |
| bool()                 | 轉 True 或 False |
| import streamlit as st | 使用 Streamlit   |
| st.title()             | 網頁標題         |
| st.write()             | 顯示內容         |
| st.text()              | 顯示純文字       |
| st.markdown()          | 顯示漂亮排版     |

---

# 🎯 本日重點整理

✅ `print()`：顯示內容。

✅ `input()`：讓使用者輸入資料。

✅ 變數：像放資料的小盒子。

✅ Python 有四種常見資料型態：整數、小數、文字、真假。

✅ 可以做加、減、乘、除等數學運算。

✅ `f"..."` 可以把變數放進句子裡。

✅ `len()` 可以算文字有幾個字。

✅ `type()` 可以知道資料是什麼型態。

✅ `int()`、`float()`、`str()`、`bool()` 可以改變資料型態。

✅ Streamlit 可以把 Python 做成簡單又漂亮的網頁。
