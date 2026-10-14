#242Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                t=t.replace(i," ",1)
            else:
                return False
        for i in t:
            if i !=' ':
                return False
        return True