# 求任意整数的几何级数
a = int(input("请输入一个整数："))
q = int(input("请输入一个整数："))
n = int(input("请输入一个整数："))
s = 0
for i in range(0, n+1):
    num = a*(q**i)
    s += num
print(s)