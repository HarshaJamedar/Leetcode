class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = [0] * 32 
        for n in candidates:
            self.find(n,ans)
        return max(ans)
        
    def find(self, n: int, ans: list) -> None:
        j= 31
        while n>0:

            a = n & 1
            ans[j] += a
            n>>=1
            j -= 1

        