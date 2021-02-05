def main():
    num = int(input(">>"))
    r = list(map(int, input("r:").split()))
    q = list(map(int, input("q:").split()))
    lists = []
    for i in range(num):
        sum = q[i] // r[i]
        lists.append(sum)
    print(min(lists))


main()