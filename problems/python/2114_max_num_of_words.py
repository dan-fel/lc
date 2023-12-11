from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        def getWordsInASentence(sentence: str): 
            if len(sentence) == 0:
                return 0
                    
            count = 0            
            for i in range(0, len(sentence)):                    
                if i == len(sentence) - 1:                    
                    count += 1

                if sentence[i] == ' ':
                    count += 1

            return count
        curr_max = 0        
        for sentence in sentences:
            words = getWordsInASentence(sentence)
            if  words > curr_max:
                curr_max = words
        
        return curr_max

sol = Solution()

print(sol.mostWordsFound("hello this is a sentence"))
print(sol.mostWordsFound("asd"))


