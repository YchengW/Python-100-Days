# 1. 求和对比：分别用 for、while 计算 1..n 之和并对比结果。
'''sum = 0
n = int(input("输入一个n:"))
for i in range( n + 1 ):
    sum += i
print("sum = %d" % sum)
'''

'''sum = 0
i = 0
n = int(input("input a number:"))
while i <= n:
    sum += i
    i += 1
print(f"sum = {sum}")
'''

# 2. 乘法表：打印 9×9 乘法表（上三角/整表任选一种），要求用嵌套循环。
'''row = 1
col = 1
while row <= 9:
    while col <= row:
        print(f"{row} × {col} = {row * col}", end = "  ")
        col += 1
    print()
    row += 1
    col = 1
'''

# 3. 阶乘：输入 n(>=0)，计算 n!；0! = 1。
'''n = int(input("input a number:"))
total = 1
while n > 1:
    total *= n
    n -= 1
print(f"total = {total}")'''

# 4. 猜数字：随机生成 1–100，循环输入直到猜中；用 break 结束，统计尝试次数。
'''import random
right = random.randint(1,100)
print(right)
guess = int(input("猜一个数字"))
while guess != right:
    guess = int(input("猜错了，重新猜："))
print("right!")
'''

# 5. 求质数个数：输入 n，统计 <=n 的素数数量；用 continue 跳过非素数候选的内部循环。
'''n = int(input("输入一个数："))
is_prime = True
for i in range(2, int((n ** 0.5) + 1)):
    if n % i == 0:
        is_prime = False
        break
    i += 1
if is_prime == True:
    print("Yes is prime")
else:
    print("No is not prime")
'''
# 6. 数位反转：输入正整数，输出其倒序数（如 123→321）；仅用算术与循环，不得转字符串。
n = int(input("正整数："))
sum = 0
while n != 0:
    sum = sum * 10
    
    i = n % 10
    
    sum = sum + i
   
    n =int(n / 10)
    
print(f"sum = {sum}")