#20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #mapping = {'(':')','{':'}','[':']'}
        mapping = {'(':')','{':'}','[':']'}
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if stack:
                    top_element = stack.pop()
                else:
                    #top_element = '#'
                    return False
                if mapping[top_element] != char:
                    return False
        if stack:
            return False
        else:
            return True

