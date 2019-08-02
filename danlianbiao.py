# -*- coding:utf-8 -*-

'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution:
    # array 二维列表
    def Find(self, target, arr):

        row_len = len(arr)
        col_len = len(arr[0])

        for i in range(row_len):
            for j in range(col_len)[::-1]:
                if arr[i][j] == target:
                    return True
                if arr[i][j] > target:
                    j -= 1
                    continue
                else:
                    i += 1
                    break
        return False

arr = [
       [1,2,3],
       [2,3,4],
       [3,4,5]
       ]

s =Solution()

asd = s.Find(3, arr)

print(asd)