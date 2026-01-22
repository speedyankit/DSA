class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        sum_map = {}
        max_length = 0
        current_sum = 0
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            if current_sum == k:
                max_length = i+1
                
            if (current_sum - k) in sum_map:
                previous_index = sum_map[current_sum - k]
                current_len = i - previous_index
                max_length= max(max_length, current_len)
                
            if current_sum not in sum_map:
                sum_map[current_sum] = i
            
        return max_length
