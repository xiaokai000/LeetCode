'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''

def longestCommonPrefix(strs):
    if not strs: return ""
    s1 = min(strs)
    s2 = max(strs)
    print(s1)
    print(s2)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1


res = longestCommonPrefix(["flower","flow","flight"])

print(res)