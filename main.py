if __name__ == '__main__':
    dict_value = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dict_value[name] = score

    marks = sorted(set([i for i in dict_value.values()]))[1]

    names = sorted([i for i,j in dict_value.items() if j == marks])

    for i in names:
        print(i)

    