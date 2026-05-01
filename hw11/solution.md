# ДЗ 11 — коды Рида-Соломона над \(GF(2^4)\)

## Задача 1

Построить порождающий многочлен для кода Рида-Соломона над полем

\[
GF(2^4)
\]

с параметрами:

\[
n=15,\qquad d=5.
\]

---

## 1) Поле \(GF(2^4)\)

Поле задается примитивным многочленом

\[
p(x)=1+x+x^4.
\]

Пусть \(\alpha\) — примитивный элемент. Тогда:

\[
\alpha^4+\alpha+1=0,\qquad \alpha^4=\alpha+1.
\]

В поле \(2^4=16\) элементов, поэтому мультипликативная группа имеет порядок

\[
2^4-1=15,
\]

то есть

\[
\alpha^{15}=1.
\]

---

## 2) Параметры RS-кода

Для кода Рида-Соломона:

\[
d=n-k+1.
\]

Следовательно:

\[
k=n-d+1=15-5+1=11.
\]

Значит, параметры:

\[
(15,11,5).
\]

Степень порождающего многочлена:

\[
\deg g(x)=n-k=4.
\]

---

## 3) Порождающий многочлен

Стандартное соглашение для RS-кода:

\[
g(x)=\prod_{i=1}^{d-1}(x-\alpha^i).
\]

Так как характеристика поля равна 2, имеем

\[
x-\alpha^i=x+\alpha^i.
\]

При \(d=5\) нужно \(d-1=4\) корня:

\[
\alpha,\alpha^2,\alpha^3,\alpha^4.
\]

Поэтому:

\[
g(x)=(x-\alpha)(x-\alpha^2)(x-\alpha^3)(x-\alpha^4)
\]
\[
=(x+\alpha)(x+\alpha^2)(x+\alpha^3)(x+\alpha^4).
\]

После перемножения в \(GF(2^4)\):

\[
\boxed{
g(x)=x^4+\alpha^{13}x^3+\alpha^6x^2+\alpha^3x+\alpha^{10}
}.
\]

---

## Задача 2

Рассмотрим РС-код

\[
(15,9)
\]

над полем \(GF(2^4)\), исправляющий 3 ошибки.

---

## 1) Параметры и синдромы

Для RS-кода:

\[
d=n-k+1=15-9+1=7.
\]

Исправляющая способность:

\[
t=\left\lfloor\frac{d-1}{2}\right\rfloor=3.
\]

Порождающий многочлен имеет корни

\[
\alpha,\alpha^2,\alpha^3,\alpha^4,\alpha^5,\alpha^6.
\]

Поэтому при декодировании вычисляем:

\[
S_i=v(\alpha^i),\qquad i=1,\dots,6.
\]

Если все синдромы нулевые, принятое слово уже кодовое.

---

## 2) Принятое слово

Дано:

\[
v(x)=
\alpha+\alpha^3x+\alpha^{10}x^2+\alpha^{12}x^3+\alpha^{13}x^4+\alpha^3x^5
\]
\[
+\alpha^9x^6+\alpha^5x^7+x^8+\alpha^{10}x^9+\alpha^8x^{10}
\]
\[
+\alpha x^{11}+\alpha x^{12}+\alpha^{13}x^{13}+\alpha^2x^{14}.
\]

Коэффициенты при \(x^0,\dots,x^{14}\):

\[
(\alpha,\alpha^3,\alpha^{10},\alpha^{12},\alpha^{13},
\alpha^3,\alpha^9,\alpha^5,1,\alpha^{10},
\alpha^8,\alpha,\alpha,\alpha^{13},\alpha^2).
\]

---

## 3) Вычисление синдромов

Считаем:

\[
S_i=v(\alpha^i),\qquad i=1,\dots,6.
\]

Получаем:

\[
S_1=0,\quad S_2=0,\quad S_3=0,\quad S_4=0,\quad S_5=0,\quad S_6=0.
\]

То есть

\[
\boxed{S=(0,0,0,0,0,0)}.
\]

---

## 4) Вывод по декодированию

Так как все синдромы нулевые, принятое слово уже принадлежит коду.

Следовательно, вектор ошибок:

\[
\boxed{e(x)=0}.
\]

В развернутом виде:

\[
\boxed{e(x)=0+0x+0x^2+\dots+0x^{14}}.
\]

Как вектор длины 15:

\[
\boxed{e=(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)}.
\]

---

## Проверка программой

```python
# GF(16) с примитивным многочленом p(x)=x^4+x+1.
# Элементы поля храним как 4-битные числа:
# a0 + a1*x + a2*x^2 + a3*x^3.

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


def gf_eval(coeffs, point):
    value = 0
    power = 1
    for coeff in coeffs:
        if coeff != 0:
            value = gf_add(value, gf_mul(coeff, power))
        power = gf_mul(power, point)
    return value


def poly_mul(p, q):
    result = [0] * (len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            if pi != 0 and qj != 0:
                result[i + j] ^= gf_mul(pi, qj)
    return result


def show_power(value, log_table):
    if value == 0:
        return "0"
    if value == 1:
        return "1"
    return f"a^{log_table[value]}"


# Таблица степеней alpha
powers = [gf_pow(ALPHA, i) for i in range(15)]
log_table = {value: i for i, value in enumerate(powers)}

# =========================
# Задача 1
# =========================
g = [1]
for i in range(1, 5):
    # множитель (x + alpha^i)
    g = poly_mul(g, [powers[i], 1])

print("Порождающий многочлен для RS-кода с d=5:")
for degree, coeff in enumerate(g):
    print(f"x^{degree}: {show_power(coeff, log_table)}")

# =========================
# Задача 2
# =========================
# v(x)=a + a^3*x + a^10*x^2 + ... + a^2*x^14
exponents = [1, 3, 10, 12, 13, 3, 9, 5, 0, 10, 8, 1, 1, 13, 2]
coeffs = [powers[e] for e in exponents]

syndromes = []
for i in range(1, 7):
    s = gf_eval(coeffs, gf_pow(ALPHA, i))
    syndromes.append(s)

print()
print("Синдромы S1..S6:")
for i, s in enumerate(syndromes, start=1):
    print(f"S_{i} = {show_power(s, log_table)}")

assert all(s == 0 for s in syndromes)

print()
print("Все синдромы равны нулю.")
print("Принятое слово является кодовым.")
print("Вектор ошибок e(x) = 0.")
```

---

## Ожидаемый вывод

```text
Порождающий многочлен для RS-кода с d=5:
x^0: a^10
x^1: a^3
x^2: a^6
x^3: a^13
x^4: 1

Синдромы S1..S6:
S_1 = 0
S_2 = 0
S_3 = 0
S_4 = 0
S_5 = 0
S_6 = 0

Все синдромы равны нулю.
Принятое слово является кодовым.
Вектор ошибок e(x) = 0.
```

---

## Итог

### Задача 1

Для RS-кода над \(GF(2^4)\) с

\[
n=15,\qquad d=5
\]

получаем:

\[
k=15-5+1=11.
\]

Порождающий многочлен:

\[
\boxed{
g(x)=(x-\alpha)(x-\alpha^2)(x-\alpha^3)(x-\alpha^4)
}.
\]

После раскрытия:

\[
\boxed{
g(x)=x^4+\alpha^{13}x^3+\alpha^6x^2+\alpha^3x+\alpha^{10}
}.
\]

### Задача 2

Для RS-кода \((15,9)\):

\[
d=15-9+1=7,\qquad t=3.
\]

Вычислено:

\[
S_1=S_2=S_3=S_4=S_5=S_6=0.
\]

Следовательно, принятое слово уже кодовое, и

\[
\boxed{e(x)=0}.
\]

