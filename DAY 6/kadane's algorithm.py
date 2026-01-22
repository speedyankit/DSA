class Solution:
        
    def maxSubarraySum(self, arr):
        # Code here
        curr_sum = 0
        max_sum = float('-inf')
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            max_sum = max(max_sum , curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        
        return max_sum
        
