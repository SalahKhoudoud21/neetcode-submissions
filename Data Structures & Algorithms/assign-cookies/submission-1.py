class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left = 0
        right = 0
        content = 0
        while right < len(s) and left < len(g):
            child = g[left]
            cookie = s[right]
            if child <= cookie:
                content += 1
                left += 1
            right += 1
        return content
            