def NumberFactorTopDown(n, memo={}):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    if n not in memo:
        memo[n] = NumberFactorTopDown(n-1, memo) + NumberFactorTopDown(n-3, memo) + NumberFactorTopDown(n-4, memo)
    return memo[n]


def NumberFactorBottomUp(n):
    table = [0, 1, 1, 2, 4]
    for i in range(5, n+1):
        table.append(table[i-1] + table[i-3] + table[i-4])
    return table[n]


print(NumberFactorTopDown(7))
print(NumberFactorBottomUp(7))
