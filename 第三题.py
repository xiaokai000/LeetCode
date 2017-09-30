'''
找出字符串中的最长子串的长度
'''

# 最长子字符串
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) <= 1:
        return len(s)
    a = []
    b = []
    for i in range(len(s)):
        a.append(s[i])
        for j in range(i+1, len(s)):
            if s[j] not in a:
                a.append(s[j])
            else:
                break
        b.append(a)
        a = []

    return max([len(x) for x in b])
print(lengthOfLongestSubstring('pwwkesiuhtgeirhpwijdkjdlkfnnlk2304920-35980945'))