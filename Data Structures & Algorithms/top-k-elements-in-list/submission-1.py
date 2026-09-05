class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for i in range(len(nums)):
            if nums[i] not in group:
                group[nums[i]]= 1
            else:
                group[nums[i]] +=  1
        return sorted(group, key=group.get, reverse=True)[:k]

        