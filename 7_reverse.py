# 算法 --》 字符串
class Solution:
    def reverse(self, x: int) -> int:
        stack = []
        stack1 = []
        flag = 0
        if x == 0:
            return 0
        if x < 0:
            x = -1*x
            flag = 1
        while x != 0:
            num = x % 10
            x = x // 10
            stack.append(num)
        while len(stack) > 0:
            stack1.append(stack.pop())
        x = stack1.pop()
        while len(stack1) > 0:
            num = stack1.pop()
            x = 10*x
            x += num
        if flag:
            if abs(x) > 2147483648:
                return 0
            return -1*x
        else:
            if x > 2147483647:
                return 0
            return x


