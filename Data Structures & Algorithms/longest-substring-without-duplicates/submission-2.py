class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        current_stack = []
        if 0 <= len(s) <= 1000:
            for c in s:
                if c in current_stack:
                    index = current_stack.index(c)
                    current_stack = current_stack[index + 1:]
                current_stack.append(c)
                length = len(current_stack)
                if max_count < length:
                    max_count = length
        return max_count


        