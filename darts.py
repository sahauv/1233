def kadane_max_sum(scores):
    mx = scores[0]
    cr = scores[0]

    for i in range(1, len(scores)):
        cr = scores[i] + max(cr, 0)
        mx = max(mx, cr)

    return mx


def circular_max_sum(scores):
    non_circ_sum = kadane_max_sum(scores)
    total_sum = 0
    for i, el in enumerate(scores):
        total_sum += el
        scores[i] *= -1
    circ_sum = total_sum + kadane_max_sum(scores)

    return max(circ_sum, non_circ_sum)


def darts(black_idx: int, scores):
    if black_idx < 0:
        return circular_max_sum(scores)

    scores = scores[black_idx:] + scores[:black_idx]
    scores[0] = 0
    return kadane_max_sum(scores)


def should_eq(expected, got):
    if expected != got:
        print(f"WRONG: expected={expected} got={got}")


def test():
    should_eq(12, darts(2, [2, 3, 4, 5, -30, 6, -1, 2]))
    should_eq(8, darts(-1, [1, -3, 2, -2, 3, 4]))


def main():
    n_lines = int(input())
    for i in range(n_lines):
        n, k = map(lambda el: int(el), input().split(' '))
        scores = map(lambda el: int(el), input().split(' '))
        out = darts(int(k), list(scores))
        print(out)


if __name__ == "__main__":
    # test()
    main()
