# 选择排序
list01 = [1, 23, 4, 5, 5, 6, 76, 7, 8, 8, 8, 9, 43, 32]

for i in range(len(list01) - 1):
    min = i
    for j in range(i + 1, len(list01)):
        if list01[min] > list01[j]:
            min = j
        if i != min:
            list01[min], list01[i] = list01[i], list01[min]
