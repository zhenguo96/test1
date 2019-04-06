class Stack:
    def __init__(self):
        self.zhan = []
    def savezhan(self,value):
        self.zhan.append(value)

    def pop_zhan(self):
        if len(self.zhan) >= 0:
            return self.zhan.pop()
        return '空栈'

    def if_zhan(self):
        return len(self.zhan) <= 0

    def zhan_first(self):
        if self.if_zhan():
            return '空栈'
        return self.zhan[-1]

if __name__ == "__main__":
    stack = Stack()
    # print(stack.if_zhan())
    # stack.savezhan(10)
    # stack.savezhan(5)
    # print(stack.pop_zhan())
    # print(stack.__dict__)
    n = 12345
    while n:
        stack.savezhan(n%10)
        n //= 10
    print(stack.__dict__)







