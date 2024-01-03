"""
2125. Number of Laser Beams in a Bank
Medium
Topics
Companies
Hint
Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.

Input: bank = ["011001","000000","010100","001000"]
Output: 8
Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
Note that there is no beam between any device on the 0th row with any on the 3rd row.
This is because the 2nd row contains security devices, which breaks the second condition.
"""


def numberOfBeams(bank: list[str])-> int:

    result = count1 = count2 = 0
    for i in range(len(bank)):
        index = i

        if "1" in bank[index]:
            count1 = sum([1 for x in range(len(bank[index])) if bank[index][x] == "1"])
            count1 = bank[index].count("1")
        else:
            continue

        while index < len(bank)-1:
            index += 1
            if "1" in bank[index]:
                count2 = sum([1 for x in range(len(bank[index])) if bank[index][x] == "1"])
                count2 = bank[index].count("1")
                break

        result += (count1*count2)
        count1 = count2 = 0
    return result


def numBeams(bank):

    total = prev_row_count = 0

    for row in bank:
        cur_row_count = row.count("1")
        if cur_row_count == 0:
            continue

        total += cur_row_count * prev_row_count
        prev_row_count = cur_row_count

    return total




print(numberOfBeams(["011001","000000","010100","001000"]))
print(numBeams(["011001","000000","010100","001000"]))
numberOfBeams(["000","111","000"])
numberOfBeams(["000","111","000"])
