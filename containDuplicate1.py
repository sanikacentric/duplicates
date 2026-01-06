from typing import List

class Solution :
    def hasdup(self, nums: List[int])-> bool:
        hashset =set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


sol = Solution()
nums=[1,2,3,1]
result =sol.hasdup(nums)   

print (result)