# ДЗ 7 — циклические коды и сравнение решеток

## Задача 1

- Разложить $x^7-1$ на множители (3 множителя) над $\mathbb F_2$
- Построить из их комбинаций 6 порождающих полиномов
- Определить характеристики полученных кодов
- Определить, что это за коды

---

### 1) Разложение $x^7-1$ над $\mathbb F_2$

Над полем $\mathbb F_2$ выполняется:

$$
-1=1,
$$

поэтому

$$
x^7-1=x^7+1.
$$

Разложение:

$$
x^7+1=(x+1)(x^3+x+1)(x^3+x^2+1).
$$

То есть получаем три неприводимых множителя:

$$
f_1(x)=x+1,\quad
f_2(x)=x^3+x+1,\quad
f_3(x)=x^3+x^2+1.
$$

---

### 2) Шесть порождающих полиномов

Нетривиальные порождающие полиномы — все комбинации множителей, кроме $1$ и самого $x^7+1$:

$$
g_1(x)=x+1,
$$
$$
g_2(x)=x^3+x+1,
$$
$$
g_3(x)=x^3+x^2+1,
$$
$$
g_4(x)=(x+1)(x^3+x+1)=x^4+x^3+x^2+1,
$$
$$
g_5(x)=(x+1)(x^3+x^2+1)=x^4+x^2+x+1,
$$
$$
g_6(x)=(x^3+x+1)(x^3+x^2+1)=x^6+x^5+x^4+x^3+x^2+x+1.
$$

---

### 3) Характеристики кодов

Для циклического кода длины $n=7$:

$$
k=n-\deg g(x)=7-\deg g(x).
$$

Минимальные расстояния $d_{\min}$ получаем перебором всех кодовых слов $c(x)=m(x)g(x)$, $\deg m<k$.

| № | $g(x)$ | $\deg g$ | $k=7-\deg g$ | Параметры | $d_{\min}$ | Тип кода |
|---:|---|---:|---:|---|---:|---|
| 1 | $x+1$ | 1 | 6 | $[7,6,2]$ | 2 | код с проверкой на четность |
| 2 | $x^3+x+1$ | 3 | 4 | $[7,4,3]$ | 3 | код Хэмминга |
| 3 | $x^3+x^2+1$ | 3 | 4 | $[7,4,3]$ | 3 | эквивалентный код Хэмминга |
| 4 | $x^4+x^3+x^2+1$ | 4 | 3 | $[7,3,4]$ | 4 | симплекс, дуальный к Хэммингу |
| 5 | $x^4+x^2+x+1$ | 4 | 3 | $[7,3,4]$ | 4 | симплекс, дуальный к Хэммингу |
| 6 | $x^6+x^5+x^4+x^3+x^2+x+1$ | 6 | 1 | $[7,1,7]$ | 7 | код повторения |

---

### Вывод по задаче 1

Разложение

$$
x^7-1=(x+1)(x^3+x+1)(x^3+x^2+1)
$$

дает 6 нетривиальных порождающих полиномов.  
Они задают коды:

- код с проверкой на четность;
- два эквивалентных кода Хэмминга $[7,4,3]$;
- два симплекс-кода $[7,3,4]$ (дуальные к Хэммингу);
- код повторения $[7,1,7]$.

---

## Задача 2 (дополнительная)

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

## Программа для проверки

```python
import itertools
import numpy as np
from collections import Counter


# =========================
# Задача 1. Циклические коды
# =========================

def poly_mul_mod2(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj:
                    result[i + j] ^= 1
    return result


def generate_cyclic_code(n, g):
    deg_g = len(g) - 1
    k = n - deg_g
    codewords = []

    for coeffs in itertools.product([0, 1], repeat=k):
        m = list(coeffs)
        c = poly_mul_mod2(m, g)
        c = c + [0] * (n - len(c))
        codewords.append(tuple(c[:n]))

    return codewords


def hamming_weight(v):
    return sum(v)


generators = [
    ("g1", "x + 1", [1, 1]),
    ("g2", "x^3 + x + 1", [1, 1, 0, 1]),
    ("g3", "x^3 + x^2 + 1", [1, 0, 1, 1]),
    ("g4", "x^4 + x^3 + x^2 + 1", [1, 0, 1, 1, 1]),
    ("g5", "x^4 + x^2 + x + 1", [1, 1, 1, 0, 1]),
    ("g6", "x^6 + x^5 + x^4 + x^3 + x^2 + x + 1", [1, 1, 1, 1, 1, 1, 1]),
]

print("Задача 1")
print("Разложение:")
print("x^7 - 1 = (x + 1)(x^3 + x + 1)(x^3 + x^2 + 1) над F2")
print()

for name, poly_str, g in generators:
    n = 7
    deg_g = len(g) - 1
    k = n - deg_g

    code = generate_cyclic_code(n, g)
    weights = [hamming_weight(c) for c in code]
    nonzero_weights = [w for w in weights if w > 0]
    d_min = min(nonzero_weights)

    print(name, "=", poly_str)
    print("deg =", deg_g, "k =", k, "количество слов =", len(code), "d_min =", d_min)
    print("распределение весов:", dict(sorted(Counter(weights).items())))
    print()


# =========================
# Задача 2. Решетки
# =========================

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

# Проверка H
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

---

## Итоговый вывод

В задаче 1 разложение

$$
x^7-1=(x+1)(x^3+x+1)(x^3+x^2+1)
$$

дает шесть нетривиальных порождающих полиномов и коды с параметрами:

$$
[7,6,2],\ [7,4,3],\ [7,4,3],\ [7,3,4],\ [7,3,4],\ [7,1,7].
$$

В задаче 2 для кода с заданной матрицей $G$ все три способа построения решетки дают один и тот же профиль:

$$
\boxed{1,\ 2,\ 4,\ 8,\ 4,\ 2,\ 1}.
$$

Следовательно, решетки совпадают с точностью до переобозначения узлов на ярусах.

