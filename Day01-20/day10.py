# 1. 元组基础：定义三元组与四元组，演示索引、切片、len。
'''tupleEx = ('hello', 1, 'world')
tupleEx1 = ('ni', 2, 'hao', 'ma')
print(tupleEx, tupleEx1)
print(tupleEx[1], tupleEx1[2])
print(len(tupleEx), len(tupleEx1))
print(tupleEx[0:2])
print(tupleEx1[-1:-5:-1])
'''

# 2. 打包与解包：a = 1,10,100；i,j,k = a 打印；再演示 i,*mid,k = range(1,10)。
'''a = 1, 10, 100
print(type(a))
i, j, k = a
print(i, j, k)
i, *mid, k = range(1, 10)
print(i, mid, k)
'''

# 3. 交换变量：a,b = b,a；再做 a,b,c = b,c,a。
'''a, b, c= 10, 12, 14
a, b = b, a
a, b, c = b, c, a
print(a, b, c)
'''

# 4. 不可变验证：尝试修改元组元素并捕获 TypeError，打印解释。
'''tupleEx = (1, 2, 3)
tupleEx[2] = 4
'''

# 5. 组合/比较：连接两个元组并比较大小与相等性。
tuple0 = (2, 3, 4)
tuple1 = (1, 4, 5)
tuple2 = (2, 3, 4)
print(tuple0 > tuple1)
print(tuple0 == tuple2)