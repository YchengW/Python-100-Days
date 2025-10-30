# 第04章｜Python 运算符——精简版全覆盖（8题）

# 1. 算术与格式化
# 读入两个数 `a, b`（可为浮点）。按顺序打印：`a+b, a-b, a*b, a/b, a//b, a%b, a**b`；
# 若 `b==0` 的运算（`/ // %`）输出 `None`。
# > 覆盖：`+ - * / // % **` 与零值处理。
"""
a = float(input("a = "))
b = float(input("b = "))
print(a + b)
print(a - b)
print(a * b)
print(a / b if b != 0 else None)
print(a // b if b != 0 else None)
print(a % b)
print(a ** b)
"""

# 2. 比较与逻辑 & 链式比较
# 读入三数 `a b c`：
# 第一行输出：是否**严格递增**（只能写成 `a < b < c` 的链式比较）。
# 第二行输出：是否能组成三角形（`a+b>c and a+c>b and b+c>a`）。
# > 覆盖：比较运算符、`and`、链式比较。
"""
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if(a < b < c):
    print("严格递增")
else:
    print("不严格递增")
if( a + b > c and a + c > b and b + c > a):
    print("能组成三角形")
else:
    print("不能组成三角形")
"""

# 3. 短路逻辑的“安全除法”
# 实现 `safe_div(a,b)`：不写 `if`，仅用 `and / or` 的**短路**返回 `a/b` 或 `None`（当 `b==0`）。
# 写若干组用例打印结果。
# > 覆盖：短路求值、逻辑运算。

def safe_div(a,b):
    return b and a / b or None

# 例子1：华氏温度转摄氏温度
# 要求：输入华氏温度将其转换为摄氏温度，华氏温度到摄氏温度的转换公式为：C = （F-32) / 1.8
'''f = float(input("temperature = "))
c = (f - 32) / 1.8
print("c = %.2f" % c)'''

# 例子2：计算圆的周长和面积
# 要求：输入一个圆的半径，计算并输出该圆的周长和面积，π取3.14159
'''r = float(input("radius = "))
c = 2 * 3.14159 * r
s = 3.14159 * r * r
print("c = %.2f" % c)
print("s = %.2f" % s)'''

# 例子3：判断闰年
# 要求：输入一个 1582 年以后的年份，判断该年份是不是闰年。
year = int(input("year = "))
if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print("是闰年")
else:
    print("不是闰年")