'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for char in tokens:
            if char not in operators:
                stack.append(char)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if char == operators[0]:
                    stack.append(str(a+b))
                elif char == operators[1]:
                    stack.append(str(a-b))
                elif char == operators[2]:
                    stack.append(str(a*b))
                elif char == operators[3]:
                    #stack.append(str(a//b))
                    stack.append(str(int(a/b)))
        return stack.pop()
'''  

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])
        for char in tokens:
            if char not in operators:
                stack.append(char)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if char == "+":
                    stack.append(str(a+b))
                elif char == "-":
                    stack.append(str(a-b))
                elif char == "*":
                    stack.append(str(a*b))
                elif char == "/":
                    #stack.append(str(a//b))
                    stack.append(str(int(a/b)))
        return stack.pop()

        