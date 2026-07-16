# 算數指定運算子
a=1
a+=1 # a=a+1
print(a) # 2
a-=1 # a=a-1
print(a) # 1
a*=2 # a=a*2
print(a) # 2
a/=2 # a=a/2
print(a) # 1.0
a%=2 # a=a%2
print(a) # 1.0
a**=2 # a=a**2
print(a) # 1.0
a**=2 # a =a ** 2
print(a) # 1.0

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
# 9. = += -= *= /= //= %= **= 算數指定運算子

# while 迴圈
# while 可以搭配一個條件式來使用
# while True 時會一直執行迴圈
# 條件式為 False 時會跳出迴圈
# 每次迴圈執行完都會重新檢查條件有沒有變成 False
i =0
while i < 5:
    print(i)
    i += 1

import random # 匯入 random 模組

#random.randrange()設定抽籤範圍的方式跟range()一樣
print(random.randrange(7)) # 0~6
print(random.randrange(1,6)) # 1~6
print(random.randrange(1,6,2)) # 1~5,間隔2

