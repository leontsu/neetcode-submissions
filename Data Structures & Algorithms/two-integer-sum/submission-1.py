class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complementary = target - nums[i]
            complementary_index = hashmap.get(complementary)
            if complementary_index != None:
                if i < complementary_index:
                    return [i, complementary_index]
                else:
                    return [complementary_index, i]
            hashmap[nums[i]] = i