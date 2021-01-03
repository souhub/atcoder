# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '[', '{']
        right = [')', ']', '}']

        tmp = []

        for i in range(len(s)):
            for k in range(len(left)):
                if s[i] == left[k]:
                    tmp.append(s[i])
                    break
                elif s[i] == right[k]:
                    try:
                        # pop() returns a removed integer
                        r = tmp.pop()
                        if r != left[k]:
                            return False
                        break
                        # when it can't do pop(), pop() returns an error.
                    except:
                        return False

        if not len(tmp) == 0:
            return False
        else:
            return True
