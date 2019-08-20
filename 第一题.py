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

    if not nums:
        return None

    d = {}
    for i, item in enumerate(nums):
        tmp = target - item

        for key, value in d.items():
            if value == tmp:
                return [key, i]

        d[i] = item

    return None