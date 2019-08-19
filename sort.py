class Sort:
    def __init__(self, list_):
        self.list_ = list_

    # 冒泡排序
    def bubble(self):
        # 　外层循环表示比较多少轮
        for i in range(len(self.list_) - 1):
            # 　内层循环表示每轮比较的次数
            for j in range(len(self.list_) - i - 1):
                # 前一个数比后一个数大则交换位置
                if self.list_[j] > self.list_[j + 1]:
                    self.list_[j], self.list_[j + 1] = \
                        self.list_[j + 1], self.list_[j]

    # 选择排序
    def select(self):
        # 　比较多少轮
        for i in range(len(self.list_) - 1):
            min = i  # 假定i号位置数字最小   (原擂主)
            for j in range(i + 1, len(self.list_)):
                if self.list_[min] > self.list_[j]:
                    min = j  # 产生新擂主
            if i != min:  # 判断 i不是最小的(不是擂主了),就交换位置(让位)
                self.list_[i], self.list_[min] = \
                    self.list_[min], self.list_[i]

    # 插入排序
    def insert(self):
        for i in range(1, len(self.list_)):
            x = self.list_[i]  # 哨兵绑定了下标为I的数  位置空出来了
            j = i  # j 表示 I 这个位置的下标
            # 满足条件:哨兵前一个数要大于哨兵绑定的数,且下表大于0
            while j > 0 and self.list_[j - 1] > x:
                self.list_[j] = self.list_[j - 1]  # 向后移一位
                j -= 1  # 递减 是为了再和前面的数依次比较
            self.list_[j] = x  # 如果不满足上面的条件,说明找到的这个数要么小于x,要么就是下标=0了 就将x 放到下标为J的位置

    # 一轮交换
    def sub_sort(self, low, high):
        key = self.list_[low]  # 基准数字
        while low < high:  # 前面的索引值小于后面的索引值时
            # 　后面的数向前甩
            while low < high and self.list_[high] >= key:
                high -= 1
            self.list_[low] = self.list_[high]
            # 　前面的数向后甩
            while low < high and self.list_[low] < key:
                low += 1
            self.list_[high] = self.list_[low]
        self.list_[low] = key  # 这里就是low=high 所以写哪一个下标都可以
        return low  # 把key的索引值返回

    # 　快排函数
    def quick(self, low, high):
        # 　low 列表开头元素索引
        # high 列表结尾元素索引
        if low < high:  # 下面是递归函数   这是终止条件
            key = self.sub_sort(low, high)
            self.quick(low, key - 1)  # 前面的分区 再调用自己完成一轮新的分区
            self.quick(key + 1, high)  # 后面的分区 再调用原函数完成一轮新的分区


if __name__ == "__main__":
    l = [4, 1, 2, 6, 7, 3, 9, 8, 6, 2]
    sr = Sort(l)
    # sr.bubble() #　冒泡
    # sr.select() #　选择
    # sr.insert() #　插入
    sr.quick(0, len(l) - 1)
    print(sr.list_)
