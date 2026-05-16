class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair ={
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        for c in s:
            print(c)
            if c in pair:
                stack.append(pair[c])
            else:
                if len(stack) < 1 or stack.pop(-1) != c:
                    return False
        return len(stack) == 0