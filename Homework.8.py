grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Решение 1
a_ = list(students)
a = a_.sort()
#print(a_)
general1 = sum(grades[0]) / len(grades[0])
general2 = sum(grades[1]) / len(grades[1])
general3 = sum(grades[2]) / len(grades[2])
general4 = sum(grades[3]) / len(grades[3])
general5 = sum(grades[4]) / len(grades[4])
print('Ученик:', a_[0], '| Средняя оценка:', general1)
print('Ученик:', a_[1], '| Средняя оценка:', general2)
print('Ученик:', a_[2], '| Средняя оценка:', general3)
print('Ученик:', a_[3], '| Средняя оценка:', general4)
print('Ученик:', a_[4], '| Средняя оценка:', general5)
#Решение 2
stu = sorted(students)
gr = [
    sum(grades[0]) / len(grades[0]),
    sum(grades[1]) / len(grades[1]),
    sum(grades[2]) / len(grades[2]),
    sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4]),
]
ob = dict(zip(stu, gr))
print(ob)