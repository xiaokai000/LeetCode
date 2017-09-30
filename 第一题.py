'''
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    for i in nums:
        if target - i in nums:
            if target - i != i:
                return [nums.index(target - i), nums.index(i)]
            elif nums.count(i) == 2:
                first_index = nums.index(i)
                nums[nums.index(i)] = ''
                second_index = nums.index(i)
                return [first_index, second_index]