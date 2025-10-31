# 1. 列表基础：创建 [35,12,99,68,55]，演示索引读/写、切片、in、拼接 + 与重复 *。
'''list1 = [35, 12, 99, 68, 55]
print(list1[1:4])
list1[3:5] = ['a', 'b']
print(list1)
print('a' in list1)
print('c' not in list1)
print(list1 + ['c', 'd', 'e'])
print(list1 * 2)
'''
# 2. 从输入构造：读取一行整数（空格分隔）转成列表，打印最小值、最大值、平均值（保留 2 位）。
'''list_in = [int(ch) for ch in input("一行整数：") if ch != ' ']

max = list_in[0]
min = list_in[0]
sum = 0
for _ in list_in:
    if _ > max:
        max = _
    if _ < min:
        min = _
    sum += _
print(f'Max = {max}, Min = {min}, Avg = {sum / len(list_in)}')
'''
# 3. 切片练习：给定列表，切出奇数位/偶数位子序列与倒序序列。
'''list_listed = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list_odd = list_listed[0:len(list_listed):2]
print(list_odd)
list_even = list_listed[1:len(list_listed):2]
print(list_even)
list_odd_reverse = list_listed[-1:-len(list_listed)-1:-2]
print(list_odd_reverse)
list_even_reverse = list_listed[-2:-len(list_listed):-2]
print(list_even_reverse)
'''
# 4. 二维表格：用嵌套列表保存 5 个学生 3 门成绩，打印每个学生总分与全班各科平均。
'''student_grade = [[100,99,98], [60,61,62], [80,85,90]]
student1_sum = sum(student_grade[0])
student2_sum = sum(student_grade[1])
student3_sum = sum(student_grade[2])
print(f"三个学生每个学生总分：{student1_sum}, {student2_sum}, {student3_sum}")
avg1 = int(student_grade[0][0] + student_grade[1][0] + student_grade[2][0]) / 3
avg2 = int(student_grade[0][1] + student_grade[1][1] + student_grade[2][1]) / 3
avg3 = int(student_grade[0][2] + student_grade[1][2] + student_grade[2][2]) / 3
print(f"全班各科平均分：{avg1}, {avg2}, {avg3}")
'''
# 5. 骰子统计：模拟掷骰 6000 次，用列表记录 1..6 频次，打印分布。
import random
list_count = [0] * 6
for _ in range(6000):
    face = random.randrange(1, 7)
    list_count[face - 1] += 1
print(list_count)