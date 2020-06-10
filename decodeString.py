# 对列与栈 --》 解码
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi*res

            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res
'''

'''
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s, 0)
'''





# 2020.06.10 
# 对列与栈 --》 解码
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi*res

            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
        return res
'''

'''
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            res, multi = "", 0
            while i < len(s):
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += multi * tmp
                    multi = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s, 0)
'''





# 2020.06.10 
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ''
        local = ''
        times = ''
        for c in s:
            if c != ']':
                stack.append(c)
            else: # to have a local decode
                # note order
                #local = local + c 
                c = stack.pop()
                while c != '[': 
                    local = c + local
                    c = stack.pop()
                c = stack.pop()
                while c.isdigit():
                    times = c + times
                    if len(stack) > 0:
                        c = stack.pop()
                    else:
                        break
                if not c.isdigit():
                    stack.append(c)
                local = int(times) * local
                for c in local:
                    stack.append(c)
                local = ''
                times = ''
        while len(stack) > 0:
            c = stack.pop()
            result = c + result
        return result
                

                
