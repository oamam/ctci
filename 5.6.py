def main():
    a = int(input())
    b = int(input())
    c = a ^ b
    ans = 0
    while c != 0:
        c &= c - 1
        ans += 1
    print(ans)


main()
