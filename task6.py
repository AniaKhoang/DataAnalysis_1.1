import numpy as np
import random

print("Задание 6.1")
arr = np.arange(20)
A1 = arr[1::3]
print("Каждый третий элемент: ", A1)
A2 = arr[5:15][::-1]
print("Элементы с 5-го по 15-й: ", A2)
A3 = arr[15:20][::-1]
print("Последние 5 элементов", A3)

print("Задание 6.2")
arr = np.random.randint(0, 10, size=(6, 6))
print(arr)
A1 =  arr[1:4, 0:3]
print("Подматрица из строк 2–4 и истолбцов 1–3\n", A1)
A2 = np.diagonal(arr)
print("Главная диагональ", A2)
i, j = np.indices(arr.shape)
mask = (i + j) % 2 == 0
A3 = arr[mask]
print("Шахматный узор", A3)

print("Задание 6.3")
a = np.array([10, 20, 30, 40, 50, 60])
m = np.arange(12).reshape(3, 4)
print("Элементы a по индексам", a[np.array([0, 2, 4])])
print("Из матрицы m выбрать элементы", m[np.array([0, 1, 2]), np.array([1, 3, 0])])
row = np.array([0, 2]).reshape(-1, 1)
col = np.array([1, 3]).reshape(1, -1)
A = m[row, col]
print("Из матрицы m выбрать блок", A)

print("Задание 6.4")
x = np.random.randn(1000)
a = np.count_nonzero(x > 1)
print("Количество элементов, больших 1: ", a)
left = np.sign(x[:-2])
right = np.sign(x[2:])
i = left != right
x[x < 0] = 0
print("Замените все отрицательные элементы на 0\n", x)
x[1:-1][i] = 0
print("\nОбнулите элементы, стоящие на позициях\n", x)