class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sx = str(x)
        s = []
        for i in range(len(sx)):
            s.append(sx[i])
        rs = list(reversed(s))
        if rs[len(rs)-1] == '-':
            rs.remove('-')
            ans = '-'
        else:
            ans = ''
        while True:
            j = 0
            if rs[j] != '0':
                break
            rs.remove(rs[j])
        for k in range(len(rs)):
            ans += rs[k]
        if int(ans) < -2**31 or 2**31-1 < int(ans):
            ans = '0'
        return int(ans)
