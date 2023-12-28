# class Solution:
#
#     def getTimeList(self, cur_iter, char, color, needed_time):
#         time_list = []
#         index_list = []
#         for j in range(cur_iter, len(color)):
#             if color[j] == char:
#                 index_list.append(j)
#                 time_list.append(needed_time[j])
#             else:
#                 break
#
#         return time_list, index_list
#
#     def minCost(self, colors: str, needed_time: list[int]) -> int:
#         time = 0
#         index_list = []
#         for i in range(len(colors) - 1):
#             if colors[i] == colors[i + 1]:
#                 if i not in index_list:
#                     time_list, index_list = self.getTimeList(i, colors[i], colors, needed_time)
#                 time += min(time_list)
#                 time_list.remove(min(time_list))
#             else:
#                 time_list = []
#         return time
#
#
# obj = Solution()
# # print(obj.minCost("abaac", [1,2,3,4,5]))
# print(obj.minCost("bbbaaa", [4, 9, 3, 8, 8, 9]))
#
# n= 5
# print([-1]*n)


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        totalTime = 0
        i = 0
        j = 0

        while i < len(neededTime) and j < len(neededTime):
            currTotal = 0
            currMax = 0

            while j < len(neededTime) and colors[i] == colors[j]:
                currTotal += neededTime[j]
                currMax = max(currMax, neededTime[j])
                j += 1

            totalTime += currTotal - currMax
            i = j

        return totalTime

obj = Solution()
print(obj.minCost("abaac", [1,2,3,4,5]))
# print(obj.minCost("bbbaaa", [4, 9, 3, 8, 8, 9]))
