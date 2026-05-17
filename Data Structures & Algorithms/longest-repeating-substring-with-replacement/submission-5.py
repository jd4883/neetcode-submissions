class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        if not s or length==1:
            return length
        d = dict()
        L = R = res = max_freq_char = 0

        while L <= R < length:
            char = s[R]
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
            
            max_freq_char = max(max_freq_char, d[char])

            while R - L + 1 - max_freq_char > k:
                d[s[L]] -= 1
                L = L + 1
            
            res = max(res, R - L + 1)
            R = R + 1
        return res