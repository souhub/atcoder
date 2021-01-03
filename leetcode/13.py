# Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)-1):
            if roma[s[i]] < roma[s[i+1]]:
                sum -= roma[s[i]]
            else:
                sum += roma[s[i]]
        sum += roma[s[len(s)-1]]
        return sum
