# 插入排序
list01 = [1, 23, 4, 5, 5, 6, 76, 7, 8, 8, 8, 9, 43, 32]

for i in range(1, len(list01)):
    x = list01[i]
    j = i

    while j > 0 and list01[j - 1] > x:
        list01[j] = list01[j - 1]
        j -= 1
    list01[j] = x
print(list01)
