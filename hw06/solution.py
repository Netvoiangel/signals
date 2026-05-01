import itertools
import numpy as np


G = np.array([
    [1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0],
], dtype=int)


H = np.array([
    [1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 0, 1, 1],
], dtype=int)


def bits_to_str(v):
    return "".join(map(str, v))


def main():
    # Проверяем, что H действительно проверочная матрица.
    assert np.all((G @ H.T) % 2 == 0)

    # Все кодовые слова по G.
    codewords = []
    for u in itertools.product([0, 1], repeat=3):
        u = np.array(u, dtype=int)
        c = (u @ G) % 2
        codewords.append(tuple(c))

    print("Кодовые слова:")
    for c in sorted(codewords):
        print(bits_to_str(c))

    # Строим синдромную решетку.
    syndrome_levels = []
    for j in range(7):
        states = set()
        for c in codewords:
            s = np.zeros(3, dtype=int)
            for i in range(j):
                if c[i] == 1:
                    s = (s + H[:, i]) % 2
            states.add(tuple(s))
        syndrome_levels.append(states)

    print()
    print("Состояния синдромной решетки по ярусам:")
    for j, states in enumerate(syndrome_levels):
        states_as_str = sorted(bits_to_str(s) for s in states)
        print(f"S_{j}: {states_as_str}")

    syndrome_profile = [len(states) for states in syndrome_levels]

    print()
    print("Профиль синдромной решетки:")
    print(syndrome_profile)

    # Строим профиль решетки по проверочной матрице через спэны строк.
    spans = []
    for row in H:
        nonzero_positions = [i + 1 for i, value in enumerate(row) if value == 1]
        spans.append((min(nonzero_positions), max(nonzero_positions)))

    check_profile = []
    for j in range(7):
        active_rows = []
        for i, (b, e) in enumerate(spans):
            if b <= j < e:
                active_rows.append(i)
        check_profile.append(2 ** len(active_rows))

    print()
    print("Спэны строк H:")
    for i, span in enumerate(spans, start=1):
        print(f"h_{i}: {span}")

    print()
    print("Профиль решетки по проверочной матрице:")
    print(check_profile)

    assert check_profile == syndrome_profile

    print()
    print("Проверка пройдена.")
    print("Решетка по проверочной матрице совпадает с синдромной решеткой с точностью до нумерации узлов.")


if __name__ == "__main__":
    main()

