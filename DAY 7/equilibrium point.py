# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        total_sum = sum(arr)
        n = len(arr)
        l_sum = 0
        
        if n==1:
            return 0
            
        for i in range(n):
            total_sum -= arr[i]
            if l_sum == total_sum:
                return i
            l_sum += arr[i]
        return -1

