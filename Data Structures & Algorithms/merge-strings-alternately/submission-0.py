class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        j = 0
        for i in range(min(len(word1), len(word2))):
            j = i
            mergedWord += word1[i] + word2[i]
        print(j)
        mergedWord += word1[j+1:]
        mergedWord += word2[j+1:]
        return mergedWord


