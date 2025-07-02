
import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 320,
    "AMZN": 125
}

def get_user_input():
    stock_data = {}
    print("Enter your stocks (type 'done' to finish):")
    while True:
        stock = input("Stock symbol: ").upper()
        if stock == 'DONE':
            break
        if stock not in stock_prices:
            print("Stock not found in database. Try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                print("Quantity must be non-negative.")
                continue
            stock_data[stock] = stock_data.get(stock, 0) + quantity
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    return stock_data

def calculate_investment(stock_data):
    total = 0
    print("\nYour Stock Summary:")
    for stock, qty in stock_data.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        print(f"{stock}: {qty} shares x ${price} = ${value}")
    print(f"\nTotal Investment: ${total}")
    return total

def save_to_txt(stock_data, total, filename="stock_summary.txt"):
    with open(filename, 'w') as f:
        f.write("Stock Summary:\n")
        for stock, qty in stock_data.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
        f.write(f"\nTotal Investment: ${total}\n")
    print(f"\nSummary saved to {filename}")

def save_to_csv(stock_data, total, filename="stock_summary.csv"):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        for stock, qty in stock_data.items():
            price = stock_prices[stock]
            value = price * qty
            writer.writerow([stock, qty, price, value])
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total])
    print(f"\nSummary saved to {filename}")

def main():
    stock_data = get_user_input()
    if not stock_data:
        print("No stocks entered.")
        return
    total = calculate_investment(stock_data)

    choice = input("Do you want to save the result to a file? (yes/no): ").lower()
    if choice in ['yes', 'y']:
        file_type = input("Choose file type - 'txt' or 'csv': ").lower()
        if file_type == 'txt':
            save_to_txt(stock_data, total)
        elif file_type == 'csv':
            save_to_csv(stock_data, total)
        else:
            print("Invalid file type. Skipping save.")

if __name__ == "__main__":
    main()

