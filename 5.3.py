def main():
    a = int(input(), 2)
    c = 0
    pc = 0
    ans = 0
    while a != 0:
        if a & 1 == 0:
            if a & 2 == 0:
                pc = 0
            else:
                pc = c
            c = 0
        elif a & 1 == 1:
            c += 1
        ans = max(ans, c + pc + 1)
        a >>= 1
    print(ans)


main()
