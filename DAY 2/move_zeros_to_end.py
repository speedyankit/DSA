class Solution:
    def pushZerosToEnd(self, arr):
        l = 0
        for h in range(len(arr)):
            if arr[h] != 0:
                arr[l], arr[h] = arr[h], arr[l]
                l += 1
        return arr
