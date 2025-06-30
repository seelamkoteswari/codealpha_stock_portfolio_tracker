# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 310,
    "AMZN": 125
}

# Dictionary to store user's portfolio
portfolio = {}

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks: ", ", ".join(stock_prices.keys()))

# Step 1: Take user input
while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Invalid stock symbol. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock} shares: "))
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Step 2: Calculate total investment
print("\n📊 Portfolio Summary:")
total_value = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock}: {qty} shares × ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Step 3 (Optional): Save to file
save = input("\nDo you want to save this report? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("----------------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            file.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_value}")
    print("✅ Report saved as 'portfolio_report.txt'")
