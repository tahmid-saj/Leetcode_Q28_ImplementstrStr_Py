class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        
        return -1
    
        # 2 line solution
        #try: return haystack.index(needle)
		#except ValueError: return -1