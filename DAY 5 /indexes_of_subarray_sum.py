#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        left = 0
        sum = 0

        for right in range(len(arr)):
            sum+=arr[right]
            if sum == target:
                return [left+1, right+1]
            while sum > target and left<right:
                sum -= arr[left]
                left += 1
                
            if sum == target:
                return [left+1, right+1]
               
        return [-1]
