
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_num_letter = "".join(ch.lower() for ch in s if ch.isalnum())
        return str_num_letter == str_num_letter[::-1]
'''

# 注意题解中的方法
# 1. 双指针（两阶段（首先遍历一遍转换为普通字符串，再直接判断是否为回文串））
# 2. 思维要跳跃（首先有直接判断是否为回文串，再者将其从整体转化，而不是从执行细节转化）
