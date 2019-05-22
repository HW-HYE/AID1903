"""
单链表学习程序
重点程序
"""

# 创建结点类
class Node(object):
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next


# 链表的操作
class LinkList(object):
    def __init__(self):
        self.head = None

    def init_list(self, data):
        self.head = Node(None)  # 链表的开头
        p = self.head  # 可移动变量ｐ

        for i in data:
            p.next = Node(i)
            p = p.next

    def show(self):
        p = self.head.next

        while p != None:
            print(p.val, end=' ')
            p = p.next
        print()


if __name__ == "__main__":
    # 　创建链表对象
    link = LinkList()

    # 　初始数据
    l = [1, 2, 3, 4, 5]
    link.init_list(l)  # 将初始数据插入链表
    link.show()  # 遍历链表
    link.append(6)
    link.show()
