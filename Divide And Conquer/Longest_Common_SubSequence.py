def LongestCommonSubSequence(s1, s2, index1=0, index2=0):
    if index1 >= len(s1) or index2 >= len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + LongestCommonSubSequence(s1, s2, index1+1, index2+1)
    else:
        option1 = LongestCommonSubSequence(s1, s2, index1+1, index2)
        option2 = LongestCommonSubSequence(s1, s2, index1, index2+1)
        return max(option1, option2)


print(LongestCommonSubSequence("elephant", "erepat"))
