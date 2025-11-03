# 1. 转义与原始：打印包含引号与反斜杠的字符串；再打印同内容的原始字符串 r'...'，观察差别。
# string0 = '\'helloWorld\''
# print(string0)
# string1 = r'hello\world'
# print(string1)

# 2. 长度与切片：对 "abc123456" 打印 len、[2:5]、[::-1]。
'''string0 = "abc123456"
print(len(string0))
print(string0[2:5])
print(string0[::-1])
'''

# 3. 查找：用 find/index/rfind 搜索 'o'、子串 'or'；分别处理未找到的情况。
'''s = "hello, world"
print(s.find('o'))
print(s.find('or', 9))
print(s.index('o'))
'''

# 4. 大小写与标题：对 "hello, world!" 演示 capitalize/title/upper/lower。
'''s = "hello, world"
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
'''

# 5. 性质判断：对若干字符串分别用 isdigit/isalpha/isalnum/startswith/endswith。
'''s1 = "hello, world"
s2 = "Nihao"
s3 = "123kookanism"
s4 = "123456"
print(s1.isdigit(), s4.isdigit())
print(s1.isalpha(), s3.isalnum())
print(s1.startswith('hel'), s3.endswith('sm'))
'''

# 6. 词频统计：输入一行英文，按空格切分，统计词频并按频次降序打印前 5。
s1 = "sadba jk sadjhaks saljhdl kalshlkn  lsjadljknl lkjnb lk lkjn  lkn lkn"
words = s1.split(' ')
print(words)