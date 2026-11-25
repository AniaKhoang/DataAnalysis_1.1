import numpy as np
import scipy.sparse as sp
import time

print("Задание 8.1")
row  = np.random.randint(0, 5000, size=10000)
col  = np.random.randint(0, 5000, size=10000)
data = np.random.randint(0, 10000, size=10000)
A = sp.coo_matrix((data, (row, col)), shape=(5000, 5000))
C = A.tocsr()
A2 = sp.coo_matrix((data, (row, col)), shape=(5000, 5000))
A2.sum_duplicates()
print("Корректен" if C.nnz == A2.nnz else "Некорректен")

print("Задание 8.2")
n = 4000
d = 0.005
A = sp.random(n, n, density=d, format='coo', random_state=0)
C = A.tocsr()
D = A.toarray()
b1 = n * n * 8
b2 = C.data.nbytes + C.indices.nbytes + C.indptr.nbytes
print("Объём памяти для dense:", round(b1 / 1024**2, 2), "MB")
print("Объём памяти для CSR:", round(b2 / 1024**2, 2), "MB")
x = np.random.rand(n)
t = time.perf_counter()
y1 = D @ x
t1 = time.perf_counter() - t
t = time.perf_counter()
y2 = C @ x
t2 = time.perf_counter() - t
print("Время умножения на вектор для dense:", round(t1 * 1000, 3), "ms")
print("Время умножения на вектор для CSR  :", round(t2 * 1000, 3), "ms")

print("Задание 8.3")
n = 2000
ds = [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0]
x = np.random.rand(n)
t1s = []
t2s = []
for d in ds:
    A = sp.random(n, n, density=d, format='coo', random_state=0)
    C = A.tocsr()
    D = A.toarray()
    t = time.perf_counter()
    y1 = D @ x
    t1 = time.perf_counter() - t
    t = time.perf_counter()
    y2 = C @ x
    t2 = time.perf_counter() - t
    t1s.append(t1 * 1000)
    t2s.append(t2 * 1000)
print("Плотность | dense, ms | CSR, ms")
for d, a, b in zip(ds, t1s, t2s):
    print(f"{d:9} | {a:9.3f} | {b:8.3f}")
cross = None
for d, a, b in zip(ds, t1s, t2s):
    if b >= a:
        cross = d
        break
print("Sparse перестаёт выигрывать при плотности ≈", cross)