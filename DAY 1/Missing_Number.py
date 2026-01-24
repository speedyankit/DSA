class Solution:https://github.com/speedyankit/DSA
    def missingNum(self, arr):
        # code here
        
        n = len(arr) + 1
      
        total_sum = (n* (n+1))//2
        arr_sum = sum(arr)
        
        return total_sum - arr_sum
