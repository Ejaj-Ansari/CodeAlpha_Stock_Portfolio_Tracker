# CodeAlpha - Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 200
}

total_investment = 0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter your stock details.")
print("Type 'done' when you are finished.\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        print(f"✅ {stock_name}: {quantity} shares × ${price} = ${investment}\n")

    except ValueError:
        print("❌ Please enter a valid number for quantity.\n")

print("\n" + "=" * 45)
print(f"TOTAL INVESTMENT VALUE: ${total_investment}")
print("=" * 45)

print("\nThank you for using Stock Portfolio Tracker!")