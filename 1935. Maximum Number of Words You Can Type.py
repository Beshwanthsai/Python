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

    # what we are doing in this problem in leetcode is 
    # we are checking whether we can print the word with the broken letter or not
    # and we are going in creating a set adn then we are converting the sentence in to words and then 
    # we are seacrching each character if it matches the broken letter 
    # we are breaking the loop and if we can type the word we are increasing the count