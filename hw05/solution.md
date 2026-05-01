# ДЗ 5 — дуальный код Хэмминга и симплекс-код

## Задача 1

Проверить, что код, дуальный коду Хэмминга, действительно является симплексом.  
Для доказательства написать программу, которая вычисляет необходимые величины.

---

### Теоретическая часть

Рассматриваем двоичный код Хэмминга $(7,4,3)$.  
Его проверочная матрица (один из стандартных вариантов):

$$
H=
\begin{pmatrix}
0&0&0&1&1&1&1\\
0&1&1&0&0&1&1\\
1&0&1&0&1&0&1
\end{pmatrix}.
$$

Столбцы $H$ — все ненулевые векторы длины 3, значит $H$ корректно задает код Хэмминга $(7,4)$.

По определению дуального кода:

$$
C^\perp=\{x\in \mathbb F_2^7:\ x c^T=0 \ \forall c\in C\}.
$$

Если $H$ — проверочная матрица кода $C$, то строки $H$ порождают $C^\perp$.  
Следовательно, порождающая матрица дуального кода:

$$
G^\perp = H.
$$

Размеры матрицы $G^\perp$: $3\times 7$, поэтому:

- длина дуального кода: $n=7$,
- размерность дуального кода: $k=3$,
- число кодовых слов: $2^k=8$.

Для симплекс-кода с параметром $m$:

$$
[n,k,d]=[2^m-1,\ m,\ 2^{m-1}].
$$

При $m=3$ ожидаем:

$$
[n,k,d]=[7,3,4].
$$

Чтобы полностью подтвердить это, программно проверим:

1. ранг $G^\perp$ равен 3;
2. построено ровно 8 различных кодовых слов;
3. весовое распределение: $A_0=1,\ A_4=7$;
4. минимальное расстояние $d_{\min}=4$.

---

### Программа проверки

```python
import numpy as np
from itertools import product
from collections import Counter


def hamming_weight(v):
    """Вес Хэмминга: число единиц."""
    return int(np.sum(v))


def hamming_distance(a, b):
    """Расстояние Хэмминга."""
    return hamming_weight((a + b) % 2)


def rank_gf2(matrix):
    """Ранг матрицы над GF(2) методом Гаусса."""
    A = matrix.copy() % 2
    rows, cols = A.shape
    rank = 0

    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if A[row, col] == 1:
                pivot = row
                break

        if pivot is None:
            continue

        A[[rank, pivot]] = A[[pivot, rank]]

        for row in range(rows):
            if row != rank and A[row, col] == 1:
                A[row] = (A[row] + A[rank]) % 2

        rank += 1

    return rank


# Проверочная матрица кода Хэмминга (7,4,3).
# Она же порождающая матрица дуального кода.
G_dual = np.array([
    [0, 0, 0, 1, 1, 1, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1],
], dtype=int)

n = G_dual.shape[1]
k = rank_gf2(G_dual)

messages = list(product([0, 1], repeat=k))
codewords = []

print("Кодовые слова дуального кода Хэмминга:")
print("u   -> c        вес")

for coeffs in messages:
    u = np.array(coeffs, dtype=int)
    c = (u @ G_dual) % 2
    wt = hamming_weight(c)
    codewords.append(c)

    u_str = "".join(map(str, u))
    c_str = "".join(map(str, c))
    print(f"{u_str} -> {c_str}   {wt}")

weights = [hamming_weight(c) for c in codewords]
weight_distribution = Counter(weights)

distances = []
for i in range(len(codewords)):
    for j in range(i + 1, len(codewords)):
        distances.append(hamming_distance(codewords[i], codewords[j]))

d_min = min(distances)

print()
print("Параметры кода:")
print("n =", n)
print("k =", k)
print("Количество кодовых слов =", len(codewords))

print()
print("Весовое распределение:")
for w in sorted(weight_distribution):
    print(f"A_{w} = {weight_distribution[w]}")

print()
print("Минимальное расстояние:")
print("d_min =", d_min)

print()
print("Матрица расстояний:")
headers = ["".join(map(str, u)) for u in messages]
print("     " + " ".join(headers))
for u_label, c1 in zip(headers, codewords):
    row = []
    for c2 in codewords:
        row.append(hamming_distance(c1, c2))
    print(f"{u_label}: " + " ".join(f"{x:2}" for x in row))

# Автоматические проверки (доказательная часть):
assert n == 7
assert k == 3
assert len(codewords) == 2 ** k
assert len({tuple(c) for c in codewords}) == 2 ** k

assert weight_distribution[0] == 1
assert weight_distribution[4] == 7
assert all(w == 4 for w in weights if w != 0)

assert d_min == 4

print()
print("Проверка пройдена.")
print("Дуальный код Хэмминга является симплекс-кодом [7,3,4].")
```

---

### Ожидаемый результат (сокращенно)

Ключевые итоги запуска программы:

- построено $8$ кодовых слов;
- распределение весов:
  - $A_0=1$,
  - $A_4=7$;
- минимальное расстояние:
$$
d_{\min}=4.
$$

Это совпадает с параметрами симплекс-кода при $m=3$: $[7,3,4]$.

---

### Вывод

Программная проверка подтверждает:

1. $G^\perp = H$ действительно порождает дуальный код коду Хэмминга;
2. дуальный код имеет параметры $[7,3,4]$;
3. все ненулевые кодовые слова имеют одинаковый вес 4.

Следовательно, дуальный коду Хэмминга код действительно является двоичным симплекс-кодом.

