class Solution:
    
    def caseSort(self, s):
        lower = sorted([ch for ch in s if ch.islower()])
        upper = sorted([ch for ch in s if ch.isupper()])
        
        result = []
        i = j = 0  # pointers for lower and upper
        
        for ch in s:
            if ch.islower():
                result.append(lower[i])
                i += 1
            else:
                result.append(upper[j])
                j += 1
        
        print("".join(result))
string = Solution()
string.caseSort("GEekS")
    