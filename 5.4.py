def front(n):
    c = n
    c0 = 0
    c1 = 0
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    return n + (1 << c0) + (1 << (c1 - 1)) - 1


def back(n):
    c = n
    c0 = 0
    c1 = 0
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    while c & 1 == 0 and c != 0:
        c0 += 1
        c >>= 1
    return n - (1 << c1) - (1 << (c0 - 1)) + 1


def main():
    n = int(input())
    print(format(n, 'b'))
    print(format(front(n), 'b'))
    print(format(back(n), 'b'))


main()
