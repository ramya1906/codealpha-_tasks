portfolio = {}

def add_stock(symbol, shares, price):
    portfolio[symbol] = {"Shares": shares, "Price": price}

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
    else:
        print("Stock not found.")

def view_portfolio():
    print("\nStock Portfolio:")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['Shares']} shares @ ${data['Price']} each")

while True:
    print("\n1. Add Stock\n2. Remove Stock\n3. View Portfolio\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        symbol = input("Enter stock symbol: ").upper()
        shares = int(input("Enter number of shares: "))
        price = float(input("Enter price per share: "))
        add_stock(symbol, shares, price)
    elif choice == "2":
        symbol = input("Enter stock symbol to remove: ").upper()
        remove_stock(symbol)
    elif choice == "3":
        view_portfolio()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
