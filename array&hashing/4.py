#Ransom Note 383
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen={}
        
        for item in magazine:
            seen[item]=seen.get(item,0)+1
        for item in ransomNote:
            if seen.get(item,0)==0:
                return False
            seen[item]-=1
        return True

            
# there is also another method
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch not in magazine:
                return False
            magazine = magazine.replace(ch, " ", 1)
        return True
        

"""