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


def main():
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

    # Ожидаемые коэффициенты: [a^10, a^3, a^6, a^13, 1]
    expected = [powers[10], powers[3], powers[6], powers[13], 1]
    assert g == expected

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


if __name__ == "__main__":
    main()

