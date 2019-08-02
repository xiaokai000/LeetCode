'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

'''



def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i in nums:
        res^=i
    return res


print(singleNumber([1,1,2,2,3,3,4,4,5]))
print(bin(20))