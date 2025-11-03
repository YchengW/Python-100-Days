# 1. 增删改查：对 languages = ['Python','Java','C++'] 进行 append/insert/remove/pop/clear 等操作并打印中间结果。
'''languages = ['Python', 'Java', 'C++']
languages.append('hello')
print(languages)
languages.insert(1, 'niHao')
print(languages)
languages.remove('Java')
print(languages)
pop = languages.pop()
print(languages, f'pop = {pop}')
languages.clear()
print(f'after clear', languages)
'''

# 2. 频次与索引：对 items = ['Py','Java','Java','C++','Py'] 打印 'Py' 次数与首次、从索引 1 起的索引。
'''items = ['Py', 'Java', 'Java', 'C++', 'Py']
print(items.count('Py'))
print(items.index('Py', 1))
'''

# 3. 排序与反转：对一组数升序排序后反转；再用 sorted(reverse=True) 验证等价结果。
'''numbers = [1,5,12,54,65,321,87,12,36,3,5,9,6]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
'''

# 4. 列表生成式：生成 [i for i in 1..99 if i%3==0 or i%5==0]。
'''items = [i for i in range(1, 99) if i % 3 == 0 or i % 5 == 0]
print(items)
'''

# 5. 嵌套生成式：生成 5×3 的随机成绩矩阵（60–100），打印每行与每列平均。
'''import random 
scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)
'''
