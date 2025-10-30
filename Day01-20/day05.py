# 1.BMI 分类器：输入身高(cm)与体重(kg)，计算 BMI，按文档区间输出中文提示（含 <18.5、[18.5,24)、[24,27)、[27,30)、[30,35)、>=35）。
'''height = float(input("height = ")) / 100
weight = float(input("weight = "))
bmi = weight / (height * height)
if(bmi < 18.5):
    print("过轻")
elif(bmi < 24):
    print("正常")
elif(bmi < 27):
    print("过重")
elif(bmi < 30):
    print("轻度肥胖")
elif(bmi < 35):
    print("中度肥胖")
else:
    print("重度肥胖")'''

# 2.分段计价：输入电量 kwh，按阶梯价格计算电费；用 if/elif/else 实现，打印总价，保留 2 位小数。
'''kwh = float(input("kwh = "))
if(kwh <= 120):
    price = kwh * 0.52
elif(kwh <= 330):
    price = 120 * 0.52 + (kwh - 120) * 0.55
elif(kwh <= 500):
    price = 120 * 0.52 + 210 * 0.55 + (kwh - 330) * 0.60
else:
    price = 120 * 0.52 + 210 * 0.55 + 170 * 0.60 + (kwh - 500) * 0.65
print("price = %.2f" % price)'''

# 3.match-case 状态码：输入 HTTP 状态码，使用 match 输出对应英文描述；未覆盖的输出 Unknown Status Code。
'''status_code = int(input("status_code = "))
match status_code:
    case 200:
        print("OK")
    case 301:
        print("Moved Permanently")
    case 400:
        print("Bad Request")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case 502:
        print("Bad Gateway")
    case 503:
        print("Service Unavailable")
    case _:
        print("Unknown Status Code")
'''

# 4.链式比较：输入三边 a b c，仅用 a<b<c 形式判断是否严格递增；再判断能否成三角形。各打印 True/False。
'''a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if(a < b < c):
    print("True")
else:
    print("False")
if( a + b > c and a + c > b and b + c > a):
    print("True")
else:
    print("False")'''

# 5.条件表达式：输入整数，打印“偶数”或“奇数”（只能用 x % 2 == 0 and '偶数' or '奇数' 或 A if cond else B）。
'''num = int(input("num = "))
print(num % 2 == 0 and '偶数' or '奇数')'''

# 6.成绩评级：输入 0–100 分数，越界则提示 Invalid，否则输出 A/B/C/D/F；要求用区间+链式比较。
score = float(input("score = "))
if(0 <= score <= 100):
    if(score >= 90):
        print("A")
    elif(score >= 80):
        print("B")
    elif(score >= 70):
        print("C")
    elif(score >= 60):
        print("D")
    else:
        print("F")
else:
    print("Invalid")