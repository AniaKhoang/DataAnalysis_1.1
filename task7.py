import numpy as np
import os
import time

print("Задание 7.1")
rows = 50000
cols = 200
m = np.memmap("big.dat", dtype=np.float32, mode="w+", shape=(rows, cols))
for i in range(rows):
    m[i] = np.random.uniform(-100, 100, cols)
print("Ожидаемый размер файла\n", rows * cols * 4)
print("Реальный размер файла\n", os.path.getsize("big.dat"))

print("Задание 7.2")
m = np.memmap("big.dat", dtype=np.float32, mode="r", shape=(rows, cols))
batch = 1000
min = 1000000000
max = -1000000000
s = 0.0
count = 0
for start in range(0, rows, batch):
    chunk = m[start:start + batch]
    if chunk.min() < min:
        min = chunk.min()
    if chunk.max() > max:
        max = chunk.max()
    s += chunk.sum()
    count += chunk.size
print("Глобальный min", min)
print("Глобальный max", max)
print("Среднее значение", s / count)
del m

print("Задание 7.3")
n = 3000
c = np.arange(n * n, dtype=np.float64).reshape(n, n)
f = np.asfortranarray(c)
for name, arr in [("C-order", c), ("F-order", f)]:
    t = time.time()
    s = 0.0
    for i in range(n):
        for j in range(n):
            s += arr[i, j]
    print(f"{name}, построчно: {time.time() - t:.3f} сек")
    t = time.time()
    s = 0.0
    for j in range(n):
        for i in range(n):
            s += arr[i, j]
    print(f"{name}, постолбцово: {time.time() - t:.3f} сек")

print("Задание 7.4")
n = 10000000
a = np.random.uniform(0, 100, n)
b = np.random.uniform(0, 100, n)
a_l = a.tolist()
b_l = b.tolist()
t = time.time()
res = []
for i in range(n):
    res.append((a_l[i] + b_l[i]) / (a_l[i] - b_l[i] + 1))
print("Python-цикл с list:", time.time() - t, "сек")
t = time.time()
res = (a + b) / (a - b + 1)
print("Numpy-выражение в одну строку:", time.time() - t, "сек")
num = np.empty(n)
den = np.empty(n)
out = np.empty(n)
t = time.time()
np.subtract(a, b, out=den)
np.add(den, 1, out=den)
np.divide(num, den, out=out)
print("Numpy-выражение с out=:", time.time() - t, "сек")
