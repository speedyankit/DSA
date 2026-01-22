class Solution:
	def maxProduct(self,arr):
		# code here
		curr_max = arr[0]
		curr_min = arr[0]
		max_result = arr[0]
		
		for i in range(1, len(arr)):
		    temp = max(arr[i] , arr[i]*curr_max, arr[i]*curr_min)
		    curr_min = min(arr[i] , arr[i]*curr_max, arr[i]*curr_min)
		    curr_max = temp
		    max_result = max(curr_max, max_result)
		   
		return max_result
