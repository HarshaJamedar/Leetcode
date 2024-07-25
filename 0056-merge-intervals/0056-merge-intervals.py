class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n <= 1:
            return intervals
        #sorting the intervals, just in case if the intervals are jumbled
        intervals.sort()
        #pointing start and end pointers at first interval
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for i in range(1,n):
            if end >= intervals[i][0]:
                end = max(end,intervals[i][1])
                continue
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start,end])
        return res
        
        