# ДЗ 9 — БЧХ-код $(15,7,5)$, порождающая матрица и декодирование

## Задача 1

Для БЧХ-кода $(15,7)$ с минимальным расстоянием $5$:

- построить порождающую матрицу в двоичном виде;
- показать процедуру декодирования принятой последовательности
  $$
  111001100011000.
  $$

---

## 1) Параметры и исправляющая способность

Дан код:

$$
(15,7),\qquad d_{\min}=5.
$$

Исправляющая способность:

$$
t=\left\lfloor \frac{d_{\min}-1}{2}\right\rfloor
=\left\lfloor \frac{5-1}{2}\right\rfloor=2.
$$

Значит, код исправляет до 2 ошибок.

---

## 2) Построение порождающего полинома

Так как

$$
n=15=2^4-1,
$$

работаем в поле

$$
F_{16}=F_2[x]/(1+x+x^4),\qquad \alpha^4=\alpha+1.
$$

Для двоичного узкосмысленного BCH-кода с $d_{\min}\ge 5$ берем корни

$$
\alpha,\alpha^2,\alpha^3,\alpha^4.
$$

Циклотомические классы по модулю 15:

$$
C_1=\{1,2,4,8\},\qquad
C_3=\{3,6,12,9\}.
$$

Минимальные многочлены:

$$
m_1(x)=x^4+x+1,
$$
$$
m_3(x)=x^4+x^3+x^2+x+1.
$$

Порождающий полином:

$$
g(x)=\operatorname{lcm}(m_1,m_3)=m_1(x)m_3(x).
$$

Раскрываем скобки над $F_2$:

$$
g(x)=(x^4+x+1)(x^4+x^3+x^2+x+1)
=x^8+x^7+x^6+x^4+1.
$$

В возрастающем порядке степеней:

$$
g(x)=1+x^4+x^6+x^7+x^8.
$$

Проверка размерности:

$$
\deg g=8,\qquad k=n-\deg g=15-8=7.
$$

То есть действительно получен код $[15,7,5]$.

---

## 3) Порождающая матрица в двоичном виде

Полиному

$$
g(x)=1+x^4+x^6+x^7+x^8
$$

соответствует двоичный вектор длины 15:

$$
100010111000000.
$$

Строки матрицы $G$ — сдвиги:

$$
g(x),\ xg(x),\ x^2g(x),\dots,x^6g(x).
$$

Так как $k=7$, получаем 7 строк:

$$
G=
\begin{pmatrix}
1&0&0&0&1&0&1&1&1&0&0&0&0&0&0\\
0&1&0&0&0&1&0&1&1&1&0&0&0&0&0\\
0&0&1&0&0&0&1&0&1&1&1&0&0&0&0\\
0&0&0&1&0&0&0&1&0&1&1&1&0&0&0\\
0&0&0&0&1&0&0&0&1&0&1&1&1&0&0\\
0&0&0&0&0&1&0&0&0&1&0&1&1&1&0\\
0&0&0&0&0&0&1&0&0&0&1&0&1&1&1
\end{pmatrix}.
$$

---

## 4) Принятая последовательность

Из канала получено:

$$
r=111001100011000.
$$

Считаем, что первый бит — коэффициент при $x^0$. Тогда

$$
r(x)=1+x+x^2+x^5+x^6+x^{10}+x^{11}.
$$

---

## 5) Таблица степеней $\alpha$ в $F_{16}$

Для $\alpha^4=\alpha+1$:

| Степень | Двоичный вид |
|---|---|
| $\alpha^0$ | 0001 |
| $\alpha^1$ | 0010 |
| $\alpha^2$ | 0100 |
| $\alpha^3$ | 1000 |
| $\alpha^4$ | 0011 |
| $\alpha^5$ | 0110 |
| $\alpha^6$ | 1100 |
| $\alpha^7$ | 1011 |
| $\alpha^8$ | 0101 |
| $\alpha^9$ | 1010 |
| $\alpha^{10}$ | 0111 |
| $\alpha^{11}$ | 1110 |
| $\alpha^{12}$ | 1111 |
| $\alpha^{13}$ | 1101 |
| $\alpha^{14}$ | 1001 |

---

## 6) Вычисление синдромов

Для $t=2$ используем

$$
S_1=r(\alpha),\qquad S_3=r(\alpha^3).
$$

### Синдром $S_1$

$$
S_1=1+\alpha+\alpha^2+\alpha^5+\alpha^6+\alpha^{10}+\alpha^{11}.
$$

В двоичном виде:

$$
0001+0010+0100+0110+1100+0111+1110=0100=\alpha^2.
$$

Значит

$$
S_1=\alpha^2.
$$

### Синдром $S_3$

$$
S_3=r(\alpha^3)
=1+\alpha^3+\alpha^6+\alpha^{15}+\alpha^{18}+\alpha^{30}+\alpha^{33}.
$$

С учетом $\alpha^{15}=1$:

$$
\alpha^{18}=\alpha^3,\quad
\alpha^{30}=1,\quad
\alpha^{33}=\alpha^3.
$$

После упрощения получаем:

$$
S_3=\alpha^8.
$$

Итого:

$$
S_1=\alpha^2,\qquad S_3=\alpha^8.
$$

Оба синдрома ненулевые, значит ошибки есть.

---

## 7) Локаторы ошибок

Пусть локаторы:

$$
X_1=\alpha^{i_1},\qquad X_2=\alpha^{i_2}.
$$

Для двух ошибок:

$$
X_1+X_2=S_1,\qquad X_1^3+X_2^3=S_3.
$$

Используем формулу:

$$
\sigma_2=X_1X_2=\frac{S_3+S_1^3}{S_1}.
$$

Подставим:

$$
S_1^3=(\alpha^2)^3=\alpha^6.
$$

$$
S_3+S_1^3=\alpha^8+\alpha^6.
$$

$$
\alpha^8=0101,\ \alpha^6=1100,\ 0101+1100=1001=\alpha^{14}.
$$

Следовательно:

$$
\sigma_2=\frac{\alpha^{14}}{\alpha^2}=\alpha^{12}.
$$

Имеем:

$$
X_1+X_2=\alpha^2,\qquad X_1X_2=\alpha^{12}.
$$

---

## 8) Уравнение локаторов и позиции ошибок

Корни $X_1,X_2$ удовлетворяют:

$$
z^2+S_1z+\sigma_2=0,
$$
$$
z^2+\alpha^2z+\alpha^{12}=0.
$$

Подходят корни:

$$
z=\alpha^{13},\qquad z=\alpha^{14}.
$$

Проверка суммы:

$$
\alpha^{13}+\alpha^{14}=1101+1001=0100=\alpha^2.
$$

Проверка произведения:

$$
\alpha^{13}\alpha^{14}=\alpha^{27}=\alpha^{12}.
$$

Значит

$$
X_1=\alpha^{13},\qquad X_2=\alpha^{14}.
$$

Ошибки в позициях:

$$
13,\ 14
$$

(нумерация от $x^0$).

Вектор ошибки:

$$
e=000000000000011.
$$

---

## 9) Исправление принятого слова

$$
r=111001100011000.
$$

Инвертируем биты в позициях 13 и 14:

$$
111001100011000 \to 111001100011011.
$$

Исправленное кодовое слово:

$$
\boxed{c=111001100011011}.
$$

---

## 10) Проверка принадлежности коду

После исправления:

$$
c(\alpha)=0,\qquad c(\alpha^3)=0.
$$

Значит исправленное слово принадлежит БЧХ-коду.

---

## Программа для проверки

```python
from itertools import product


# Работа в GF(16) с примитивным полиномом x^4 + x + 1.
# Элемент поля: a0 + a1*x + a2*x^2 + a3*x^3 (4 бита).
MOD = 0b10011
ALPHA = 0b0010


def gf_add(a, b):
    return a ^ b


def gf_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 0b10000:
            a ^= MOD
    return result & 0b1111


def gf_pow(a, power):
    result = 1
    for _ in range(power):
        result = gf_mul(result, a)
    return result


def gf_inv(a):
    if a == 0:
        raise ZeroDivisionError("0 has no inverse in GF(16)")
    return gf_pow(a, 14)


def gf_div(a, b):
    return gf_mul(a, gf_inv(b))


def gf_eval(bits, point):
    # bits = [r0, r1, ..., r14]
    # r(point) = r0 + r1*point + ... + r14*point^14
    value = 0
    power = 1
    for bit in bits:
        if bit:
            value = gf_add(value, power)
        power = gf_mul(power, point)
    return value


def bits_to_str(bits):
    return "".join(map(str, bits))


# g(x) = 1 + x^4 + x^6 + x^7 + x^8
g = [1, 0, 0, 0, 1, 0, 1, 1, 1]

print("Порождающая матрица:")
G = []
for shift in range(7):
    row = [0] * shift + g + [0] * (15 - shift - len(g))
    G.append(row)
    print(bits_to_str(row))

# Принятое слово
r_str = "111001100011000"
r = [int(ch) for ch in r_str]

S1 = gf_eval(r, ALPHA)
S3 = gf_eval(r, gf_pow(ALPHA, 3))

# Таблица логарифмов alpha^i
powers = [gf_pow(ALPHA, i) for i in range(15)]
log = {value: i for i, value in enumerate(powers)}

print()
print("S1 =", S1, "=", f"alpha^{log[S1]}")
print("S3 =", S3, "=", f"alpha^{log[S3]}")

sigma2 = gf_div(gf_add(S3, gf_pow(S1, 3)), S1)
print("sigma2 =", sigma2, "=", f"alpha^{log[sigma2]}")

roots = []
for z in range(1, 16):
    value = gf_add(gf_add(gf_mul(z, z), gf_mul(S1, z)), sigma2)
    if value == 0:
        roots.append(z)

error_positions = [log[root] for root in roots]

print("Корни уравнения локаторов:")
for root in roots:
    print(f"alpha^{log[root]}")
print("Позиции ошибок:", error_positions)

corrected = r[:]
for pos in error_positions:
    corrected[pos] ^= 1

print("Принятое слово:     ", bits_to_str(r))
print("Исправленное слово: ", bits_to_str(corrected))

assert gf_eval(corrected, ALPHA) == 0
assert gf_eval(corrected, gf_pow(ALPHA, 3)) == 0

print()
print("Проверка пройдена: исправленное слово имеет нулевые синдромы.")
```

---

## Итог

Для БЧХ-кода $[15,7,5]$:

$$
\boxed{g(x)=1+x^4+x^6+x^7+x^8}.
$$

Порождающая матрица построена сдвигами вектора

$$
100010111000000.
$$

Для принятого слова

$$
111001100011000
$$

получены синдромы

$$
S_1=\alpha^2,\qquad S_3=\alpha^8,
$$

локаторы ошибок

$$
\alpha^{13},\ \alpha^{14},
$$

позиции ошибок $13$ и $14$, а исправленное кодовое слово:

$$
\boxed{111001100011011}.
$$

