def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    nums = nums1 + nums2
    nums.sort()
    length = len(nums)

    if length % 2 == 1:
        return nums[int((length - 1) / 2)]
    else:
        a = int(length / 2)
        b = a - 1
        return (nums[a] + nums[b]) / 2
