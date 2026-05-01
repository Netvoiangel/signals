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


def solve_task_1():
    print("Задача 1")
    print("Разложение:")
    print("x^7 - 1 = (x + 1)(x^3 + x + 1)(x^3 + x^2 + 1) над F2")
    print()

    results = []

    for name, poly_str, g in generators:
        n = 7
        deg_g = len(g) - 1
        k = n - deg_g

        code = generate_cyclic_code(n, g)
        weights = [hamming_weight(c) for c in code]
        nonzero_weights = [w for w in weights if w > 0]
        d_min = min(nonzero_weights)
        weight_dist = dict(sorted(Counter(weights).items()))

        results.append((name, deg_g, k, len(code), d_min))

        print(name, "=", poly_str)
        print("deg =", deg_g, "k =", k, "количество слов =", len(code), "d_min =", d_min)
        print("распределение весов:", weight_dist)
        print()

    # Базовые проверки параметров
    expected = {
        "g1": (1, 6, 64, 2),
        "g2": (3, 4, 16, 3),
        "g3": (3, 4, 16, 3),
        "g4": (4, 3, 8, 4),
        "g5": (4, 3, 8, 4),
        "g6": (6, 1, 2, 7),
    }
    for name, deg_g, k, size, d_min in results:
        assert (deg_g, k, size, d_min) == expected[name]


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


def all_codewords_from_G(generator):
    k = generator.shape[0]
    codewords = []

    for u in itertools.product([0, 1], repeat=k):
        u_vec = np.array(u, dtype=int)
        c = tuple((u_vec @ generator) % 2)
        codewords.append((u, c))

    return codewords


def solve_task_2():
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
    assert syndrome_profile == [1, 2, 4, 8, 4, 2, 1]

    print()
    print("Проверка пройдена.")
    print("Все три решетки совпадают с точностью до нумерации узлов.")


if __name__ == "__main__":
    solve_task_1()
    print("=" * 60)
    solve_task_2()

