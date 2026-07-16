你的課程內容很多，我幫你整理成一份**適合國小學生閱讀**的版本，保留重要觀念，但用比較簡單、容易理解的方式說明。

# Python 學習筆記（國小版）

## 第 1 部分：Streamlit 畫面設計

### 1. `st.title()`

**功能：** 在畫面上放一個大標題。

```python
st.title("我的程式")
```

畫面會看到：

> 我的程式

---

### 2. `st.write()`

**功能：** 顯示文字、數字或資料。

```python
st.write("哈囉！")
```

---

### 3. `st.columns()`

**功能：** 把畫面分成很多欄。

例如：

```python
col1, col2 = st.columns(2)
```

畫面就會變成左右兩欄。

也可以設定大小：

```python
col1, col2 = st.columns([1,2])
```

表示：

* 左邊 1 份
* 右邊 2 份（比較寬）

---

### 4. `with`

**功能：** 告訴程式：「下面的東西都放在這一欄。」

例如：

```python
with col1:
    st.button("按鈕")
```

意思就是：

把按鈕放到左邊那一欄。

---

### 5. `st.button()`

**功能：** 建立按鈕。

```python
st.button("開始")
```

按下按鈕後，可以讓程式做事情。

---

### 6. `st.text_input()`

**功能：** 建立文字輸入框。

```python
name = st.text_input("請輸入名字")
```

使用者可以輸入自己的名字。

---

### 7. `st.number_input()`

**功能：** 建立數字輸入框。

例如：

```python
age = st.number_input("請輸入年齡")
```

只能輸入數字。

---

### 8. `st.info()`

**功能：** 顯示藍色提示。

```python
st.info("請輸入資料")
```

---

### 9. `st.success()`

**功能：** 顯示成功訊息（綠色）。

```python
st.success("完成！")
```

---

### 10. `st.warning()`

**功能：** 顯示警告（黃色）。

```python
st.warning("請重新輸入")
```

---

### 11. `st.markdown()`

**功能：** 顯示比較漂亮的文字。

可以加入：

* 粗體
* 顏色
* Emoji

---

### 12. `st.balloons()`

**功能：** 放煙火（氣球）。

```python
st.balloons()
```

通常猜對遊戲時會使用。

---

### 13. `st.rerun()`

**功能：** 重新執行整個程式。

就像按一次重新整理。

---

# 第 2 部分：Session State（記憶功能）

平常程式重新整理後，變數都會變回原本的值。

例如：

```python
ans = 1
```

每次重新整理都會變回 1。

所以 Streamlit 提供：

```python
st.session_state
```

它就像程式的小背包。

可以一直記住資料。

例如：

```python
st.session_state.score = 10
```

即使重新整理，分數也還在。

---

# 第 3 部分：算數指定運算子

它們都是簡寫。

原本：

```python
a = a + 1
```

可以寫成：

```python
a += 1
```

常用的有：

| 寫法  | 意思  |
| --- | --- |
| +=  | 加   |
| -=  | 減   |
| *=  | 乘   |
| /=  | 除   |
| %=  | 取餘數 |
| **= | 次方  |

例如：

```python
a = 5
a += 2
```

最後

```
a = 7
```

---

# 第 4 部分：運算優先順序

先算：

1. ()
2. 次方 **
3. 乘、除、取餘數
4. 加減
5. 比較大小
6. not
7. and
8. or
9. =

例如：

```
2+3*4
```

不是 20

而是

```
14
```

因為乘法先算。

---

# 第 5 部分：while 迴圈

意思：

**一直重複做事情。**

例如：

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

輸出：

```
0
1
2
3
4
```

每做一次，

就再檢查一次：

```
i < 5 ?
```

如果不是，

就停止。

---

# 第 6 部分：Random（亂數）

先載入：

```python
import random
```

---

## random.randint()

取得一個範圍內的整數。

例如：

```python
random.randint(1,100)
```

可能得到：

```
23
88
61
```

---

## random.randrange()

跟 range 很像。

例如：

```python
random.randrange(5)
```

可能得到：

```
0~4
```

---

# 第 7 部分：猜數字遊戲

遊戲流程：

① 電腦先偷偷選一個數字。

↓

② 玩家輸入數字。

↓

③ 判斷：

* 太大
* 太小
* 猜對

↓

④ 修改提示範圍。

例如：

```
1~100
```

猜：

50

太小

變成：

```
51~100
```

一直猜到正確。

程式裡利用：

* session_state（記住答案）
* if（判斷）
* number_input（輸入數字）
* button（按鈕）
* balloons（猜對）

一起完成整個遊戲。

---

# 第 8 部分：Dictionary（字典）

字典就是：

**用「名字」找資料。**

格式：

```python
{
    key : value
}
```

例如：

```python
student = {
    "小明":90,
    "小美":88
}
```

意思：

小明 → 90

小美 → 88

---

## 取得資料

```python
student["小明"]
```

得到：

```
90
```

---

## 新增資料

```python
student["小華"] = 95
```

---

## 修改資料

```python
student["小明"] = 100
```

---

## 刪除資料

```python
student.pop("小明")
```

---

## 檢查有沒有這個 Key

```python
"小明" in student
```

得到：

```
True
```

---

# 第 9 部分：keys()、values()、items()

假設：

```python
d = {
    "a":1,
    "b":2
}
```

## keys()

取得所有名字。

```
a
b
```

---

## values()

取得所有數字。

```
1
2
```

---

## items()

一次取得：

名字 + 數字。

```
a 1
b 2
```

---

# 第 10 部分：成績系統

資料長這樣：

```python
{
    "小明":{
        "國文":[90,80,70],
        "數學":[85,75,65]
    }
}
```

代表：

小明

↓

國文

↓

三次考試：

```
90
80
70
```

---

可以取得：

```python
grade["小明"]["數學"]
```

得到：

```
[85,75,65]
```

---

還可以算平均：

```python
sum(scores)
```

把全部加起來。

再除以：

```python
len(scores)
```

就是平均。

---

# 第 11 部分：for 迴圈

for 可以一直重複做事情。

例如：

```python
for i in range(5):
    print(i)
```

輸出：

```
0
1
2
3
4
```

也可以拿來走訪字典：

```python
for key, value in d.items():
```

一次拿到：

* key（名字）
* value（內容）

---

# 今天學到的重要觀念整理

✅ Streamlit 可以做互動網頁。

✅ columns 可以把畫面分成很多欄。

✅ button 可以建立按鈕。

✅ text_input 可以輸入文字。

✅ number_input 可以輸入數字。

✅ session_state 可以記住資料。

✅ while 可以一直重複執行。

✅ random 可以產生亂數。

✅ Dictionary（字典）可以用「名稱」找資料。

✅ for 可以重複處理很多資料。

✅ 猜數字遊戲結合了按鈕、輸入框、判斷、亂數和 session_state，是一個完整的小遊戲程式。
