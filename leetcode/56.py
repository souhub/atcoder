class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        i = 0
        intervals.sort()

        while i < len(intervals):
            start = intervals[i][0]
            goal = intervals[i][1]
            for j in range(i+1, len(intervals)):
                if goal >= intervals[j][0]:
                    if intervals[j][1] >= goal:
                        goal = intervals[j][1]
                    i += 1

            ans.append([start, goal])
            i += 1
        return ans
