'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

#Solution:
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_pre = ""
        if not strs: return longest_pre
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            if all([x.startswith(shortest_str[:i+1]) for x in strs]):
                longest_pre = shortest_str[:i+1]
            else:
                break
        return longest_pre 
