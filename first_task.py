def main():
    N = int(input().strip())

    shares = [float(input().strip()) for _ in range(N)]

    total = sum(shares)

    for share in shares:
        percentage = (share / total)
        print(f"{percentage:.3f}")


if __name__ == "__main__":
    main()
