def FibonacciTopDown(n, memo={}):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = FibonacciTopDown(n-1, memo) + FibonacciTopDown(n-2, memo)
    return memo[n]


def FibonacciBottomUp(n):
    table = [0, 1]
    for i in range(2, n):
        table.append(table[i-1] + table[i-2])
    return table[n-1]


print(FibonacciTopDown(100))
print(FibonacciBottomUp(100))
