def MinOperTopDown(s1, s2, index1=0, index2=0, memo={}):
    if index1 >= len(s1):
        return len(s2) - index2
    if index2 >= len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return MinOperTopDown(s1, s2, index1+1, index2+1, memo)
    else:
        key = str(index1) + str(index2)
        if key not in memo:
            deleteOp = 1 + MinOperTopDown(s1, s2, index1, index2 + 1, memo)
            insertOp = 1 + MinOperTopDown(s1, s2, index1 + 1, index2, memo)
            replaceOp = 1 + MinOperTopDown(s1, s2, index1 + 1, index2 + 1, memo)
            memo[key] = min(deleteOp, insertOp, replaceOp)
        return memo[key]


def MinOperBottomUp(s1, s2):
    table = {}
    for i1 in range(len(s1)+1):
        key = str(i1) + "0"
        table[key] = i1
    for i2 in range(len(s2)+1):
        key = "0" + str(i2)
        table[key] = i2
    for i1 in range(1, len(s1)+1):
        for i2 in range(1, len(s2)+1):
            if s1[i1-1] == s2[i2-1]:
                currentKey = str(i1) + str(i2)
                noChangeKey = str(i1-1) + str(i2-1)
                table[currentKey] = table[noChangeKey]
            else:
                currentKey = str(i1) + str(i2)
                deleteKey = str(i1) + str(i2-1)
                insertKey = str(i1-1) + str(i2)
                replaceKey = str(i1-1) + str(i2-1)
                table[currentKey] = 1 + min(table[deleteKey], table[insertKey], table[replaceKey])
    finalKey = str(len(s1)) + str(len(s2))
    return table[finalKey]


print(MinOperTopDown("apple", "aaplls"))
print(MinOperBottomUp("apple", "aaplls"))
