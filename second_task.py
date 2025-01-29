from itertools import combinations


def main():
    N, M, S = map(int, input().strip().split())

    lots = []

    while True:
        line = input().strip()
        if not line:
            break
        parts = line.split()

        if len(parts) != 4:
            continue

        day, name, price, quantity = parts
        day, price, quantity = int(day), float(price), int(quantity)
        lots.append((day, name, price, quantity))

    best_income = -float("inf")
    best_combination = []

    for i in range(1, len(lots) + 1):
        for combination in combinations(lots, i):
            spent = 0
            for _, _, price, quantity in combination:
                spent += (price / 100) * 1000 * quantity

            if spent > S:
                continue

            total_nominal = sum(q * 1000 for _, _, _, q in combination)
            total_coupons = sum(q * 30 for _, _, _, q in combination)
            total_income = total_nominal + total_coupons - spent

            if total_income > best_income:
                best_income = total_income
                best_combination = combination

    print(int(best_income))
    for purchase in sorted(best_combination, key=lambda x: (x[0], -x[2])):
        print(purchase[0], purchase[1], f"{purchase[2]:.1f}", purchase[3])
    print("")


if __name__ == "__main__":
    main()
