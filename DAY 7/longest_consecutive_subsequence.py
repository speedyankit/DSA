 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        s = set()
        for ele in arr:
            s.add(ele)
            
        ans = 0
        
        for i in range(len(arr)):
            if(arr[i]-1) not in s:
                j = arr[i]
                while j in s:
                    j+=1
                ans = max(ans, j-arr[i])
        return ans
