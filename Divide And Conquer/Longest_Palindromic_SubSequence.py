def LongestPalindromicSubSequence(string, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    if startIndex == endIndex:
        return 1
    if string[startIndex] == string[endIndex]:
        return 2 + LongestPalindromicSubSequence(string, startIndex+1, endIndex-1)
    else:
        option1 = LongestPalindromicSubSequence(string, startIndex+1, endIndex)
        option2 = LongestPalindromicSubSequence(string, startIndex, endIndex-1)
        return max(option1, option2)


S = "elephant"
print(LongestPalindromicSubSequence(S, 0, len(S)-1))
