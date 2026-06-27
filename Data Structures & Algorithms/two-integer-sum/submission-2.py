class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        i = 0
        j = len(nums) - 1

        while i != j:
            two_sum = nums_sorted[i] + nums_sorted[j]
            if two_sum == target:
                index1 = nums.index(nums_sorted[i])

                if nums_sorted[i] == nums_sorted[j]:
                    nums[index1] += 1
                    print(nums)
                    index2 = nums.index(nums_sorted[j])
                
                else: 
                    index2 = nums.index(nums_sorted[j])
                indices = [index1, index2]
                indices.sort()
                return indices
            elif two_sum > target:
                j -= 1
            else: # two_sum < target:
                i += 1