238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Brut force solution - 



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        curr = 0
        
        arr = [1]*len(nums)
        res = []

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *=nums[j]
            arr[i] = prod

        return arr


# Time - O(N^2)
# Space - O(N) 

# Optimal Solution - 


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_arr = [0]*n
        r_arr = [0]*n
        l = 1
        r = 1

        for i in range(n):
            j = -i -1
            l_arr[i] = l
            r_arr[j] = r

            l *= nums[i]
            r *= nums[j]
        
        return [l*r for l,r in zip(l_arr,r_arr)]

# Time -> O(N)
# Space -> O(N)
        



   



