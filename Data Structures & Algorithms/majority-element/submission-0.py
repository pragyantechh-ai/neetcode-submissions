class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        max_Count = res = 0
        for num in nums:
            count[num] +=1
            if max_Count< count[num]:
                max_Count= count[num]
                res= num
        return res