class Solution:
    def isHappy(self, n: int) -> bool:
        history = []
        ans = None
        number = n
        while True:
            total = 0

            for i in range(len(str(number))):
                total += int(str(number)[i])**2

            if total == 1:
                ans = True

            for h in history:
                if total == h:
                    ans = False

            if ans is not None:
                break

            number = total
            history.append(total)

        return ans
