class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c =set()
        for i in range(len(nums)):
            if nums[i] in c:
                return True
            c.add(nums[i])
        return False
        