#Using two pointer

class Solution:
    def twoSum(self, arr, target):
        # code here
        arr.sort()
        
        l,h = 0,len(arr)-1
        while l<h:
            if target < arr[l]+arr[h]:
                h-=1
            elif target>arr[l]+arr[h]:
                l += 1
            else :
                return True
        return False

#using hasp map

class Solution:
	def twoSum(self, arr, target):
		# code here
		s = set()
		
		for num in arr:
		    complement = target - num
		    if complement in s:
		        return True
		    s.add(num)
		        
		return False
