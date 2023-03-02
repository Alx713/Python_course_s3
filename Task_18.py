"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

N = int(input())
A = list(range(1, N+1))
X = float(input())
def nearest_value(A, X):
    found = A[0]
    for item in A:
        if abs(item - X) < abs(found - X):
            found = item
    return found
print(nearest_value(A, X))