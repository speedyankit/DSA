class Solution:
    def reverseWords(self, s):
        # code here
        word = [word for word in s.split(".") if word]
        
        word.reverse()
        
        return ".".join(word)
