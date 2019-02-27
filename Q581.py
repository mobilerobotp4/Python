#Leetcode problem 581 - Shortest Unsorted Continuous Subarray
'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
'''

#Solution:
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        sort=sorted(nums)
        
        if nums==sort:
            return 0
        while i < len(nums)-1:
            if nums[i]==sort[i]:
                i+=1
            else:
                break
        while j >0:
            if nums[j]==sort[j]:
                j-=1
            else:
                break
        return j-i+1  
