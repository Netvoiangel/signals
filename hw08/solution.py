from math import gcd


def solve_task_1():
    group_order = 5**2 - 1

    print("Задача 1")
    print("Порядок мультипликативной группы GF(5^2)*:", group_order)
    print()

    orders = {}
    for k in range(group_order):
        if k == 0:
            order = 1
        else:
            order = group_order // gcd(group_order, k)
        orders[k] = order

    print("Порядки элементов x^k:")
    for k, order in orders.items():
        if k == 0:
            print(f"x^{k} = 1: порядок {order}")
        else:
            print(f"x^{k}: порядок {order}")

    print()
    print("Группировка по порядкам:")
    by_order = {}
    for k, order in orders.items():
        by_order.setdefault(order, []).append(k)

    for order in sorted(by_order):
        elements = []
        for k in by_order[order]:
            if k == 0:
                elements.append("1")
            elif k == 1:
                elements.append("x")
            else:
                elements.append(f"x^{k}")
        print(f"Порядок {order}: {', '.join(elements)}")

    expected_orders = {1, 2, 3, 4, 6, 8, 12, 24}
    assert set(by_order.keys()) == expected_orders


def solve_task_2():
    print()
    print("Задача 2")

    state = [0, 0, 1, 1]
    seen = [tuple(state)]

    print("Смена состояний регистра:")
    for _ in range(15):
        print("".join(map(str, state)))
        # h(x) = 1 + x + x^4 => a_{i+4} = a_i + a_{i+1} (mod 2)
        new_bit = state[0] ^ state[1]
        state = [state[1], state[2], state[3], new_bit]
        seen.append(tuple(state))

    print("".join(map(str, state)))

    unique_nonzero_states = set(seen[:-1])

    print()
    print("Количество различных ненулевых состояний:", len(unique_nonzero_states))
    print("Вернулись к начальному состоянию:", seen[0] == seen[-1])
    print("Нулевое состояние встречается:", (0, 0, 0, 0) in unique_nonzero_states)

    assert len(unique_nonzero_states) == 15
    assert seen[0] == seen[-1]
    assert (0, 0, 0, 0) not in unique_nonzero_states

    print()
    print("Регистр имеет максимальный период 2^4 - 1 = 15.")
    print("Код является кодом максимальной длины.")
    print("Параметры кода: [15, 4, 8].")
    print("Минимальное расстояние d_min = 8.")


if __name__ == "__main__":
    solve_task_1()
    print("=" * 60)
    solve_task_2()

