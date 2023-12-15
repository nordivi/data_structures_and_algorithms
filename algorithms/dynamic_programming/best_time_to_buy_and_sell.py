


def buy_and_sell(prices):
    n = len(prices)
    m1 = prices[0]
    m2 = 0
    for i in range(1, n):
        if m1 > prices[i]:
            m1 = prices[i]
        if m2 < (prices[i] - m1):
            m2 = prices[i] - m1
    return m2

buy_and_sell([7,1,5,3,6,4])