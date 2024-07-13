def find_side_B(a: int, pp: int) -> int:
    print((pp**2 - a**2)**0.51)
    while True:
        b = (pp**2 - a**2)**0.5
        if b % 1 == 0.0:
            return b
        pp += 1


if __name__ == '__main__':
    print(find_side_B(a=5 * 10**7, pp=8*10**7))