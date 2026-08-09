class Solution:
    def strStr(self, s: str, sub: str) -> int:
        for i in range(len(s)-len(sub)+1):
            if s[i:i+len(sub)]==sub:
                return i
        return -1