def NumberFactor(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4
    else:
        sum1 = NumberFactor(n-1)
        sum3 = NumberFactor(n-3)
        sum4 = NumberFactor(n-4)
        return sum1 + sum3 + sum4


print(NumberFactor(6))
