# 1935. Maximum Number of Words You Can Type

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)

        words = text.split()
        count = 0 
        for word in words:
            can_type = True
            for ch in word:
                 if ch in broken_set:  
                    can_type = False
                    break
            if can_type:
                count += 1
        return count

    