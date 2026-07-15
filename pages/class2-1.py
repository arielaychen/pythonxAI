# 比較運算子,只要同樣類型做比較
print(1==1) # True
print(1!=1) # False
print(1<1) # False
print(1>1) # False
print(1<=1) # True
print(1>=1) # True

# 邏輯運算子
# 運算子,只要一個條件為False,結果就是False
print(True and True)  # True
print(True and False) # False
print(False and False) # False
print(False and True) # False

# or 運算子,只要一個條件為True,結果就是True
print(True or True)  # True
print(True or False) # True
print(False or False) # False
print(False or True) # True

# not 運算子
print(not True)  # False
print(not False)  # True

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or

# 密碼門檢查
password = input("請輸入密碼：")
if password == "123456":
    print("歡迎Jeffrey")
elif password == "5678":
    print("歡迎Tim")
elif password == "0000":
    print("歡迎Chloe")
else:
    print("密碼錯誤")
# 連續使用if跟使用if elif else的差別
# elif真的可以排除前面有判斷過的條件,所以縮短判斷條件的復雜度，也節省了時間
# 但是如果是使用多個if來做獨立判斷，則每個if都會被執行,所以效率較低  