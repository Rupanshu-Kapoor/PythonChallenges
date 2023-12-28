class Solution:

    def minCost(self, colors: str, neededTime: list[int]) -> int:
        time = 0
        i = 0

        while i < len(colors):
            j = i + 1
            while j < len(colors) and colors[j] == colors[i]:
                j += 1

            time += min(neededTime[i:j])
            i = j

        return time

obj = Solution()
