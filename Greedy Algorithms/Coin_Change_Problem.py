def CoinChange(value, coins):
    N = value
    coins.sort()
    index = len(coins) - 1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N -= coinValue
        if N < coinValue:
            index -= 1
        if N == 0:
            break


value = 2035
coins = [1, 2, 5, 20, 50, 1000]

CoinChange(value, coins)
