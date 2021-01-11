class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        ans = -1

        # Create hash map using try & error
        for i in range(len(s)):
            try:
                d[s[i]] += 1
            except:
                d[s[i]] = 1

        # Non-repeating character satisfies the condition of d.value==1
        for k, v in d.items():
            if v == 1:
                ans = s.index(k)
                break

        return ans
