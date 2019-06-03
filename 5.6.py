def main():
    a = int(input())
    b = int(input())
    c = a ^ b
    ans = 0
    while c != 0:
        c >>= 1
        ans += c & 1
    print(ans)


main()
