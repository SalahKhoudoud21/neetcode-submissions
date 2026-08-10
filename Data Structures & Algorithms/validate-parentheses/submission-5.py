class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicto = {']': '[', '}': '{', ')': '('}
        for char in s:
            if char not in {']', '}', ')'}:
                stack.append(char)
            else:
                looking_for = dicto[char]
                if not stack or stack[-1] != looking_for:
                    return False
                stack.pop()
        if stack:
            return False
        return True
                