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
    a = matrix.copy() % 2
    rows, cols = a.shape
    rank = 0

    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if a[row, col] == 1:
                pivot = row
                break

        if pivot is None:
            continue

        a[[rank, pivot]] = a[[pivot, rank]]

        for row in range(rows):
            if row != rank and a[row, col] == 1:
                a[row] = (a[row] + a[rank]) % 2

        rank += 1

    return rank


def main():
    # Проверочная матрица кода Хэмминга (7,4,3).
    # Она же порождающая матрица дуального кода.
    g_dual = np.array([
        [0, 0, 0, 1, 1, 1, 1],
        [0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1],
    ], dtype=int)

    n = g_dual.shape[1]
    k = rank_gf2(g_dual)

    messages = list(product([0, 1], repeat=k))
    codewords = []

    print("Кодовые слова дуального кода Хэмминга:")
    print("u   -> c        вес")

    for coeffs in messages:
        u = np.array(coeffs, dtype=int)
        c = (u @ g_dual) % 2
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

    # Автоматические проверки (доказательная часть).
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


if __name__ == "__main__":
    main()

