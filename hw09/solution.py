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


def main():
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
    assert bits_to_str(corrected) == "111001100011011"

    print()
    print("Проверка пройдена: исправленное слово имеет нулевые синдромы.")


if __name__ == "__main__":
    main()

