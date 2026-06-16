# You are given a list of a stock's daily closing prices for 30 days. 
# Build a Stock Price Tracker that computes: 
# Best day to buy and best day to sell for maximum profit (cannot sell before buying) 
# The 7-day moving average for each window of 7 consecutive days 
# The most volatile week (highest price swing = max - min within any 7-day window) 

prices = [
    100, 98, 105, 110, 107, 115, 120,
    118, 125, 130, 128, 135, 140, 138,
    145, 150, 148, 142, 155, 160, 158,
    165, 170, 168, 172, 175, 180, 178,
    185, 190
]

def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    temp_buy = 0
    buy_day = 0
    sell_day = 0
    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
            temp_buy = i

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit
            buy_day = temp_buy
            sell_day = i
    return buy_day, sell_day, max_profit

def week_prices(length, window, prices):
    weeks = []

    for i in range(length):
        week = prices[i : i+window]
        weeks.append(week)
    return weeks
    
def moving_average(prices, window):
    averages = []
    length = len(prices) - window + 1

    weeks = week_prices(length, window, prices)

    for week in weeks:
        average = sum(week)/window
        averages.append(f"{average:.2f}")

    return averages

def most_volatile_week(prices, window):
    max_diff = 0
    volatile_week = 0
    length = len(prices) - window + 1
    weeks = week_prices(length, window, prices)

    for i, week in enumerate(weeks):
        difference = max(week)-min(week)

        if difference > max_diff:
            max_diff = difference
            volatile_week = i + 1

    return volatile_week, max_diff

def main():
    buy, sell, profit = max_profit(prices)
    averages = moving_average(prices, 7)
    week, difference = most_volatile_week(prices, 7)

    print("=====STOCK REPORT======")
    print(f"Buy Day: {buy + 1}")
    print(f"Sell Day: {sell + 1}")
    print(f"Profit: {profit}")
    print()

    print("7-Day Moving Averages:")

    averages = moving_average(prices, 7)

    [print(f"Week {i+1}: {avg}") for i, avg in enumerate(averages)]
        

    print()

    print("Most Volatile Week:")
    print(f"Week Number : {week}")
    print(f"Price Swing : {difference}")


if __name__ == "__main__":
    main()