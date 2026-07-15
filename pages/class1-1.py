print('Hello World!')
print('Ariel 陳安穎')
print('不要低頭\n雙下巴會出來')

"""
這是多行註解
"""

#這是單行註解
print('Hello World!') #print是在終端機顯示文字的指令
# ctrl+?可快速註解/取消註解
 
# 基本形態
print(1.0 ) # float 這是浮點數
print(1.234 ) # float 這是浮點數
print("apple") # str 這是字串
print(True) # bool 這是布林值
print(False) # bool 這是布林值

# 變數
a=10 # 新增一個儲存空間並取名為a，"="的功能是將右邊的值10存入左邊的a
print(a) # 在終端機顯示a所存的值
a="apple" # 將a的值改為"apple"
print(a) # 在終端機顯示a所存的值
# 運算子
print(1+1) # 加法
print(1-1) # 減法   
print(1*1) # 乘法
print(1/1) # 除法       
print(1//1) # 取商
print(1%1) # 取餘數
print(1**1) # 次方

# # 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減

# 字串運算 , + 、 *
print("apple" + "pen") # 字串相加
print("apple" * 3) # 字串重複   

# 字串格式化
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示

print(len("apple")) # len()是計算字串長度的函式,可以計算字串的長度
print(len("apple")) # len()是計算字串長度的函式,可以計算字串的長度
#type() # 可以查看變數的資料型態
print(type(1)) # <class 'int'> 
print(type(1.0)) # <class 'float'> 
print(type("apple")) # <class 'str'> 
print(type(True)) # <class 'bool'>  

# 型態轉變
print(int(1.0)) # float轉int
print(float(1)) # int轉float
print(str(1)) # int轉str
print(bool(1)) # int轉bool
print(bool(1)) # float轉bool
print(int(1.234)) # float轉int
print(float("1.234")) # str轉float
print(str(1.234)) # float轉str
print(bool(1.234)) # float轉bool
 # print(int("hello")) # 這行會報錯，因為字串裡面如果有非數字的字元,無法轉換成數字
 
# 都要了使用者輸入半徑,再計算圓的面積
r=float(input("請輸入半徑: "))
print(f"圓的面積為: {3.14*r**2}")

o=float(input("請輸入國文期中成績: "))
p=float(input("請輸入國文期末成績: "))
print(f"國文平均成績為: {(o+p)/2}")
