# 1. 素数打印：输出 100 以内所有素数，按行/空格分隔均可。
'''count = 0
for i in range(2, 101):
    pointer = 2
    is_prime = True
    while pointer <= int(i ** 0.5):
        if i % pointer == 0:
            is_prime = False
            break
        pointer += 1
    if is_prime == True:
        count += 1
        print(f"{i}是素数")
print(f"共有{count}个素数")'''

# 2. 斐波那契：输出前 n 项（n>=1），从 1,1,... 或 0,1,... 二选一，保持一致。
'''a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)'''
    
# 3. 水仙花数：打印所有 3 位水仙花数。
'''for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(f"{num}是水仙花数")'''

# 4. 百钱百鸡：求所有整数解并打印（公鸡5钱、母鸡3钱、小鸡3只1钱；共 100 钱买 100 只）。
for x in range(0, 21):
    for y in range(0, 34):
        if(100 - x - y) % 3 == 0:
            if 5 * x + 3 * y + (100 - x - y) // 3 == 100:
                print (f"{x}只公鸡{y}只母鸡{100 - x - y}只雏鸡")

# 5. 最大公约数与最小公倍数：输入 a,b，输出 gcd 与 lcm（欧几里得算法）。


# 6. 完美数：输出 1..10000 中的完美数（真因子和等于自身）。