from linklist import *

list01 = [1, 23, 4, 5, 5, 6, 76, 7, 8, 8, 8, 9, 43, 32]


def subsort(list01):
    for i in range(len(list01) - 1):
        for j in range(len(list01) - i - 1):
            if list01[j] > list01[j + 1]:
                list01[j], list01[j + 1] = list01[j + 1], list01[j]
    print(list01)

subsort(list01)
