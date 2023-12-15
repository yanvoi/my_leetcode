"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
 
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:

	1 <= nums.length <= 2 * 10^4
	-1000 <= nums[i] <= 1000
	-10^7 <= k <= 10^7

"""

# O(n) time, O(n) space
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums_seen_count = Counter([0])
        cur_sum, answer = 0, 0
        for num in nums:
            cur_sum += num
            answer += sums_seen_count[cur_sum - k]
            sums_seen_count[cur_sum] += 1

        return answer
