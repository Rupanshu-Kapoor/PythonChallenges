"""
Traffic
Moderate
Problem statement
https://www.codingninjas.com/studio/problems/traffic_6682625
The Road Department is planning to make some new traffic regulations. But to make the regulations they need to analyze the current situation of the traffic.
The traffic can be analyzed from an array 'VEHICLE' of length 'N' , which consists of ‘0’ if there is no vehicle at that point and ‘1’ if there is a vehicle at the point.

Unfortunately the array ‘VEHICLE’ got corrupted as at most 'M' '1' got flipped to ‘0’.
Traffic jam is defined as the length of consecutive vehicles on the road.
The Road Department wants to know the worst possible scenario for the traffic jam. Return the maximum possible length of the consecutive vehicles.

Example:
Input: ‘N’ = 3, ‘M’ = 1, VEHICLE’ = [0, 1, 1]
Output: 3
Explanation:
As there is at most one 1 that got flipped to 0, so for the worst-case scenario we can reflip the first(1-based ) index to 1, resulting in a length of 3.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
3 1
0 1 1
Sample Output 1:
3
Explanation Of Sample Input 1 :
As there is at most one 1 that got flipped to 0, so for the worst-case scenario we can reflip the first index (1- based) to 1, resulting in a length of 3.
Sample Input 2 :
6 3
0 1 0 0 1 0
Sample Output 2 :
5
Constraints:
1  <= N <= 10^6
1 <= M <= N
0 <= VEHICLE[i] <= 1
Time Limit: 1 sec
"""


def findMaxConsecutiveOnes(nums: list[int]) -> int:
    max_count = count = 0

    for i in nums:
        if i == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0

    if count > max_count:
        max_count = count

    return max_count


def traffic(n: int, m: int, vehicle: [int]) -> int:
    # Write your code here.
    pass
    worst_scenario = 0
    for i in range(n-m+1):

        if vehicle[i] == 0:
            j = m
            k = i
            temp = vehicle[:]
            while j >= 1 and k < n:
                if temp[k] == 0:
                    temp[k] = 1
                    j -= 1
                k += 1
            count = findMaxConsecutiveOnes(temp)
            if count > worst_scenario:
                worst_scenario = count
    return worst_scenario

N = 3
M = 1
VEHICLE = [0, 1, 1]
print(traffic(N,M,VEHICLE))