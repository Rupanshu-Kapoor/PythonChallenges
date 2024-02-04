"""
Next Permutation: https://leetcode.com/problems/next-permutation/description/
Medium

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Optimal solution with some extra space
            1. we will start from the back end and find the smaller term then the ith term (so that
                                if we swap the smaller with the large one, we get next big permutation)
            2. Once we find the smaller element, we will find the next big element from this small element
                    in the part of arr[smaller_element : end]
            3. After we find the next big, we swap the small and big element to get the minimum possible
                    big number than the current one
            4. Now we need to sort the arr[ smaller_element : end] so that no other smaller possible permutation exists.

        :param nums:
        :return:
        """
        # initializing j to second last element so that we have atleast two elements that can be swapped
        j = len(nums) - 2

        # looping to find the smaller element from the back so that it can be swapped with immediate bigger element
        while j >= 0:
            temp = nums[j:]
            # if we find current element bigger than all the remaining elements we skip this and reduces to j to check for next element
            if temp[0] > max(temp[1:]):
                j -= 1
                continue

            # once we find the smaller elementm, we allot a temp space to store the next big numbers
            temp2 = []
            # also sort the array so that we can easily find the immediate bigger number
            temp_sorted = sorted(temp)

            # checking for immediate big number
            for i in range(len(temp_sorted)):
                if temp_sorted[i] > temp[0]:
                    # storing that big number at the start of temp array
                    temp2.append(temp_sorted[i])
                    temp_sorted.pop(i)
                    break

            # storing rest of number in ascending order
            for i in temp_sorted:
                temp2.append(i)

            # just making sure this number is bigger than old one(no need, it will always be big)
            if temp2 > nums[j:]:
                nums[j:] = temp2
                return

            j -= 1

        # if there exist a array in reverse order, we need to give the smallest number, so we sort the whole array
        nums.sort()

    def nextPermutationOP(self, nums: list[int]) -> None:
        """
        Optimal approach, without extra memory
        Same 3 steps
        4. Instead of sorting, we just reverse the last array, as we are sure that last array is in descending order
        :param nums:
        :return:
        :TC: O(3n)
        :SC: O(1)
        """
        size = len(nums) - 1
        ind = size - 1
        while ind >= 0:
            # looping till we find the smaller elemnt from the back
            if nums[ind] >= nums[ind + 1]:
                ind -= 1
                continue

            # swapping lower number with next immediate number
            for i in range(size, ind, -1):
                if nums[i] > nums[ind]:
                    nums[i], nums[ind] = nums[ind], nums[i]
                    break

            # reversing the last part of array
            start = ind + 1
            end = size
            while start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return
        start = 0
        end = size
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


arr = [1, 3, 2]
print(arr)
obj = Solution()
obj.nextPermutationOP(arr)
print(arr)
