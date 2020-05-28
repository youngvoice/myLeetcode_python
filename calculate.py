# 227. Basic calculate II
'''
class Solution:
    def calculate(self, s: str) -> int:
        slist = self.get_legal_list(s)
        
        pass
    # remove whitespace and composite multible bit number 
    def get_legal_list(self, s):
        ret = []
        temp = ""
        for c in s:
            if c == " ":
                continue
            elif c.isnumeric():
                temp += c
            else:
                ret.append(int(temp))
                temp = ""
                ret.append(c)
        ret.append(int(temp))

        return ret

'''

# 224 basic calculate
'''
class Solution:
    def calculate(self, s: str) -> int:
        sufExp = []
        optStack = []
        status = False
        for c in s:

            if c == " ":
                continue
            else:
                if c.isnumeric():
                    #num += c
                    
                    if not status:
                        sufExp.append(c)
                    else:
                        word = sufExp.pop()
                        word += c 
                        sufExp.append(word)
                    status = True
                else:
                    status = False
                    if not optStack:
                        optStack.append(c)
                    else:
                        #c > optStack[-1]
                        if c == "(":
                            optStack.append(c)
                        elif c == ")":
                            while True:
                                o = optStack.pop()
                                if o != "(":
                                    sufExp.append(o)
                                else:
                                    break
                        elif optStack[-1] == "(":
                            optStack.append(c)
                        else:
                            sufExp.append(optStack.pop())
                            optStack.append(c)
        while optStack:
            sufExp.append(optStack.pop())
        print(sufExp)
        #sufExp

        res = []
        for c in sufExp:
            if c.isnumeric():
                res.append(int(c))
            elif c == "+":
                b = res.pop()
                a = res.pop()
                res.append(a + b)
            elif c == "-":
                b = res.pop()
                a = res.pop()
                res.append(a - b)
            else:
                pass
        return res.pop()
'''



#####################################################
'''
OperandType EvaluateExpression() {
    InitStack(OPTR); Push(OPTR, '#');
    InitStack(OPND);

    while 
        c = getchar()
        # operand
        if c not in OP:
            push(c)
        # operator
        else:
            switch(precede(gettop(operator), c)):
                case '<':
                case '=':
                case '>':
}
'''

'''
OperandType EvaluateExpression() {
    InitStack(OPTR); Push(OPTR, '#');
    InitStack(OPND);
    c = getchar()
    while gettop(OPTR) == # and c == #
        
        # operand
        if c not in OP:
            OPND.push(c)
        # operator
        else:
            switch(precede(gettop(OPTR), c)):
                case '<':
                    OPTR.push(c)
                case '=':
                    OPTR.pop()

                case '>':
                    opnd2 = OPND.pop()
                    optr = OPTR.pop()
                    opnd1 = OPND.pop()
                    res = calc(opnd1, optr, opnd2)
                    OPND.push(res)
                    continue
                    
    c = getchar()
}

'''


'''
class Solution:
    def calculate(self, s: str) -> int:
        def precede(opt1, opt2):
            optDic = {"+":0, "-":1, "*":2, "/":3, "(":4, ")":5, "#":6}
            orderTable = [
                [">", ">", "<", "<", "<", ">", ">"],
                [">", ">", "<", "<", "<", ">", ">"],
                [">", ">", ">", ">", "<", ">", ">"],
                [">", ">", ">", ">", "<", ">", ">"],
                ["<", "<", "<", "<", "<", "=", " "],
                [">", ">", ">", ">", " ", ">", ">"],
                ["<", "<", "<", "<", "<", " ", "="],
            ]
            return orderTable[optDic[opt1]][optDic[opt2]]
        def calc(opnd1, optr, opnd2):
            if optr == "+":
                return opnd1 + opnd2
            elif optr == "-":
                return opnd1 - opnd2
            elif optr == "*":
                return opnd1 * opnd2
            elif optr == "/":
                return opnd1 // opnd2
            else:
                pass

        OPTR = []
        OPND = []
        OPTR.append("#")
        s+="#"
        optDic = {"+":0, "-":1, "*":2, "/":3, "(":4, ")":5, "#":6}
        index = 0
        c = s[index]
        index += 1
        flag = False
    
        while OPTR[-1] != "#" or c != "#":
            if c == " ":
                c = s[index]
                index += 1
                continue
            if c not in optDic:
                if flag: # in num
                    num = 10 * num + int(c)
                else:
                    flag = True
                    num = int(c)

                
            else:
                if flag:
                    OPND.append(num)
                    flag = False
                order = precede(OPTR[-1], c)
                if order == "<":
                    OPTR.append(c)
                elif order == "=":
                    OPTR.pop()
                elif order == ">":
                    opnd2 = OPND.pop()
                    optr = OPTR.pop()
                    opnd1 = OPND.pop()
                    res = calc(opnd1, optr, opnd2)
                    OPND.append(res)
                    continue
                else:
                    pass
            c = s[index]
            index += 1
        return OPND.pop()

'''

# 实现的算符优先算法
'''
class Solution:
    def calculate(self, s: str) -> int:
        def precede(opt1, opt2):
            optDic = {"+":0, "-":1, "*":2, "/":3, "(":4, ")":5, "#":6}
            orderTable = [
                [">", ">", "<", "<", "<", ">", ">"],
                [">", ">", "<", "<", "<", ">", ">"],
                [">", ">", ">", ">", "<", ">", ">"],
                [">", ">", ">", ">", "<", ">", ">"],
                ["<", "<", "<", "<", "<", "=", " "],
                [">", ">", ">", ">", " ", ">", ">"],
                ["<", "<", "<", "<", "<", " ", "="],
            ]
            return orderTable[optDic[opt1]][optDic[opt2]]
        def calc(opnd1, optr, opnd2):
            if optr == "+":
                return opnd1 + opnd2
            elif optr == "-":
                return opnd1 - opnd2
            elif optr == "*":
                return opnd1 * opnd2
            elif optr == "/":
                return opnd1 // opnd2
            else:
                pass

        OPTR = []
        OPND = []
        OPTR.append("#")
        s+="#"
        optDic = {"+":0, "-":1, "*":2, "/":3, "(":4, ")":5, "#":6}
        index = 0
        c = s[index]
        index += 1
        flag = False
    
        while OPTR[-1] != "#" or c != "#":
            if c == " ":
                c = s[index]
                index += 1
                continue
            if c not in optDic:
                
                if flag: # in num
                    num = OPND.pop()
                    num = 10 * num + int(c)
                else:
                    flag = True
                    num = int(c)
                OPND.append(num)

                
            else:
                if flag:
                    flag = False
                order = precede(OPTR[-1], c)
                if order == "<":
                    OPTR.append(c)
                elif order == "=":
                    OPTR.pop()
                elif order == ">":
                    opnd2 = OPND.pop()
                    optr = OPTR.pop()
                    opnd1 = OPND.pop()
                    res = calc(opnd1, optr, opnd2)
                    OPND.append(res)
                    continue
                else:
                    pass
            c = s[index]
            index += 1
        return OPND.pop()

'''


# 后缀表达式算法


#####################################################################
#       +       -       *        /     --->input c
# +     >       >       <        <   
# -     >       >       <        <
# *     >       >       >        >
# /     >       >       >        >
#
# top
'''
EvaluateExpression()
{
    InitStack(OPTR)
    InitStack(OPND)
    index = 0
    while(True)
    {
        c = input[index]
        if (!In(c,OP))
        {
            Push(OPND, c)
            index += 1
        }
        else{
            if (isEmpty(OPTR))
            {
                Push(OPTR, c)
                index += 1
            }
            else if(c == '(')
            {
                Push(OPTR, c)
                index += 1
            }
            else if(c == ')')
            {
                top = Pop(OPTR)
                if (top != '(')
                {
                    Push(OPND, top)
                }
                else
                {
                    pass
                }

            }

            else {
                top = gettop(OPTR)
                if (top == '(')
                {
                    Push(OPTR, c)
                    index += 1
                }
                else 
                {
                    order = precede(gettop(OPTR), c)
                    if (order == '>'){
                        top = Pop(OPTR)
                        Push(OPND, top)

                    }
                    elif (order == '='){
                        pass
                    }
                    elif (order == '<'){
                        Push(OPTR, c)
                        index += 1
                    }
                    else pass
                }

            }            
        }

    }
}

'''


class Solution:
    def calculate(self, s: str) -> int:
        
        optList = {"+": 0, "-": 1, "*": 2, "/": 3}
        def precede(top, c):
            # + - * /
            nonlocal optList
            orderTable = [
                [">", ">", "<", "<"],
                [">", ">", "<", "<"],
                [">", ">", ">", ">"],
                [">", ">", ">", ">"],
            ]
            return orderTable[optList[top]][optList[c]]

        
        OPTR = []
        OPND = []
        index = 0
        flag = False
        while True:
            if index == len(s):
                break
            c = s[index]
            if c == " ":
                index += 1
                continue
            #if c not in optList:
            if c.isdigit():
                if flag == True: # in number
                    num = OPND.pop()
                    num = num * 10 + int(c)
                    
                else:
                    num = int(c)
                    flag = True
                print(num, "c is ",c)
                OPND.append(num)
                #OPND.append(c)
                index += 1
            else:
                flag = False
                if not OPTR or c == "(":
                    OPTR.append(c)
                    index += 1
                elif c == ")":
                    top = OPTR.pop()
                    if top != "(":
                        OPND.append(top)
                    else:
                        index += 1
                else:
                    top = OPTR[-1]
                    if top == "(":
                        OPTR.append(c)
                        index += 1
                    else:
                        order = precede(OPTR[-1], c)
                        if order == ">":
                            top = OPTR.pop()
                            OPND.append(top)
                        elif order == "=":
                            pass
                        elif order == "<":
                            OPTR.append(c)
                            index += 1
                        else:
                            pass
        while OPTR:
            OPND.append(OPTR.pop())
        print(OPND)
        # OPND is 
        def calculate(num1, opt, num2):
            if opt == "+":
                return num1 + num2
            elif opt == "-":
                return num1 - num2
            elif opt == "*":
                return num1 * num2
            elif opt == "/":
                return num1 // num2
            else:
                pass
        temp = []
        for c in OPND:
            if c in optList:
                num2 = temp.pop()
                num1 = temp.pop()
                temp.append(calculate(num1, c, num2))
            else:
                temp.append(c)
        return temp.pop()


                
                    
                

