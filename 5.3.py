def main():
    S = input()
    arr = []
    c = 0
    ps = ''
    for s in S:
        if ps == s:
            c += 1
        else:
            ps = s
            arr.append(c)
            c = 1
    arr.append(c)
    ans = 0
    for i in range(1, len(arr) - 2, 2):
        ans = max(ans, arr[i] + arr[i + 2] + 1)
    print(ans)


main()
