def main():
    S = input()
    if len(S) > 128:
        return False
    L = [False] * 128
    for s in S:
        if L[chr(s)] is True:
            return False
        L[chr(s)] = True
    return True


main()
