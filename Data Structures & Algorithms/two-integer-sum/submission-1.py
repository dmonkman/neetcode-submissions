class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(val, idx) for idx, val in enumerate(nums)]
        indexed_nums.sort()
        i = 0
        j = len(indexed_nums) - 1
        while(i!=j):
            if(indexed_nums[i][0] + indexed_nums[j][0] > target):
                j -= 1
            elif(indexed_nums[i][0] + indexed_nums[j][0] < target):
                i += 1
            elif(indexed_nums[i][0] + indexed_nums[j][0] == target):
                idx1, idx2 = indexed_nums[i][1], indexed_nums[j][1]
                return sorted([idx1, idx2])
