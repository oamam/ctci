def main():
    N = input()
    M = input()
    i, j = map(int, input().split())
    nN = int(format(int(N[:-i], 2) << (j - i), 'b') + N[-i:], 2)
    mM = int(M, 2) << i
    print(format(nN ^ mM, 'b'))


main()
