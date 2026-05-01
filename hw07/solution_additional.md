# ДЗ 7 — дополнительная задача

## Задача 2

Для кода с порождающей матрицей

$$
G=
\begin{pmatrix}
1&0&1&1&0&1\\
0&0&1&1&1&0\\
0&1&0&1&1&1
\end{pmatrix}
$$

построить три решетки:

- по кодовым словам (без использования линейности),
- по порождающей матрице,
- по проверочной матрице.

---

### 1) Параметры и кодовые слова

Размер матрицы $G$: $3\times 6$, значит

$$
k=3,\qquad n=6,\qquad |C|=2^k=8.
$$

Кодовые слова по формуле $c=uG$:

| $u$ | $c=uG$ |
|---|---|
| 000 | 000000 |
| 001 | 010111 |
| 010 | 001110 |
| 011 | 011001 |
| 100 | 101101 |
| 101 | 111010 |
| 110 | 100011 |
| 111 | 110100 |

Итак,

$$
C=\{000000,\ 010111,\ 001110,\ 011001,\ 101101,\ 111010,\ 100011,\ 110100\}.
$$

---

### 2) Решетка по кодовым словам

Строим треллис по префиксам (без использования линейности). После объединения состояний с одинаковыми множествами продолжений получаем профиль:

$$
\boxed{1,\ 2,\ 4,\ 8,\ 4,\ 2,\ 1}.
$$

---

### 3) Решетка по порождающей матрице

Переходим к минимальной спэновой форме (эквивалентная матрица):

$$
\widetilde G=
\begin{pmatrix}
1&1&0&1&0&0\\
0&1&0&1&1&1\\
0&0&1&1&1&0
\end{pmatrix}.
$$

Ее строки имеют спэны:

$$
[1,4],\quad [2,6],\quad [3,5].
$$

Число активных строк на ярусах $j=0,\dots,6$:

$$
0,\ 1,\ 2,\ 3,\ 2,\ 1,\ 0.
$$

Значит, профиль решетки:

$$
\boxed{1,\ 2,\ 4,\ 8,\ 4,\ 2,\ 1}.
$$

---

### 4) Решетка по проверочной матрице

Из систематического вида получаем проверочную матрицу:

$$
H=
\begin{pmatrix}
0&1&1&1&0&0\\
1&1&1&0&1&0\\
1&1&0&0&0&1
\end{pmatrix},
\qquad GH^T=0.
$$

Состояние на ярусе $i$ — частичный синдром:

$$
s_i=\sum_{j=1}^{i} c_j h_j \pmod 2.
$$

Для всех путей, ведущих к кодовым словам, профиль синдромной решетки:

$$
\boxed{1,\ 2,\ 4,\ 8,\ 4,\ 2,\ 1}.
$$

---

### Вывод по задаче 2

Все три способа дают одинаковый профиль:

$$
\boxed{1,\ 2,\ 4,\ 8,\ 4,\ 2,\ 1}.
$$

Следовательно, решетки, построенные:

- по кодовым словам,
- по порождающей матрице,
- по проверочной матрице,

совпадают с точностью до переобозначения узлов на ярусах.

---

## Программа для проверки (дополнительная задача)

```python
import itertools
import numpy as np


G = np.array([
    [1, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 1],
], dtype=int)


H = np.array([
    [0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0, 1],
], dtype=int)


def bits_to_str(v):
    return "".join(map(str, v))


def all_codewords_from_G(G):
    k = G.shape[0]
    codewords = []
    for u in itertools.product([0, 1], repeat=k):
        u_vec = np.array(u, dtype=int)
        c = tuple((u_vec @ G) % 2)
        codewords.append((u, c))
    return codewords


codewords = all_codewords_from_G(G)
print("Задача 2")
print("Кодовые слова:")
for u, c in codewords:
    print(bits_to_str(u), "->", bits_to_str(c))

assert np.all((G @ H.T) % 2 == 0)

# Решетка по кодовым словам
C = [c for _, c in codewords]
n = 6
word_trellis_profile = []
for i in range(n + 1):
    residual_sets = set()
    prefixes = sorted(set(c[:i] for c in C))
    for p in prefixes:
        residual = tuple(sorted(c[i:] for c in C if c[:i] == p))
        residual_sets.add(residual)
    word_trellis_profile.append(len(residual_sets))

print()
print("Профиль решетки по кодовым словам:")
print(word_trellis_profile)

# Решетка по порождающей матрице
G_min_span = np.array([
    [1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0],
], dtype=int)

spans = []
for row in G_min_span:
    nonzero_positions = [i + 1 for i, x in enumerate(row) if x == 1]
    spans.append((min(nonzero_positions), max(nonzero_positions)))

generator_profile = []
for j in range(n + 1):
    active = 0
    for b, e in spans:
        if b <= j < e:
            active += 1
    generator_profile.append(2 ** active)

print()
print("Спэны строк минимальной спэновой формы:")
for i, span in enumerate(spans, start=1):
    print(f"g_{i}: {span}")
print("Профиль решетки по порождающей матрице:")
print(generator_profile)

# Решетка по проверочной матрице
syndrome_profile = []
syndrome_levels = []
for i in range(n + 1):
    states = set()
    for c in C:
        s = np.zeros(H.shape[0], dtype=int)
        for j in range(i):
            if c[j] == 1:
                s = (s + H[:, j]) % 2
        states.add(tuple(s))
    syndrome_levels.append(states)
    syndrome_profile.append(len(states))

print()
print("Состояния синдромной решетки:")
for i, states in enumerate(syndrome_levels):
    states_str = sorted(bits_to_str(s) for s in states)
    print(f"S_{i}:", states_str)
print("Профиль решетки по проверочной матрице:")
print(syndrome_profile)

assert word_trellis_profile == generator_profile == syndrome_profile

print()
print("Проверка пройдена.")
print("Все три решетки совпадают с точностью до нумерации узлов.")
```

