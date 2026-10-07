class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        j = 0
        for i in range(min(len(word1), len(word2))):
            mergedWord += word1[i] + word2[i]
            j = i + 1
        
        mergedWord += word1[j:]
        mergedWord += word2[j:]
        return mergedWord


