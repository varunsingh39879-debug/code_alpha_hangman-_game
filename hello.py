stock_prices = {
    "TCS": 3900,
    "INFY": 1500,
    "RELIANCE": 2800,
    "HDFC": 1731,
    "TESLA": 467,
    "WIPRO": 3256,
    "ITC":314.90,
    "GROW":214.99,
    "ADANI POWER":221.85,
    "ICICI":287.09,
    
}

grand_total = 0

n = int(input("How many stocks? "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if stock in stock_prices:
        total = stock_prices[stock] * qty
        print(stock, "value =", total)

        grand_total += total
    else:
        print("Stock not found")

print("\nTOTAL PORTFOLIO =", grand_total)