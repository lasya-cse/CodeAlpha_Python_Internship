stock_prices={"AAPL":180,"TSLA":250,"GOOGL":150,"AMZN":185,"MSFT":420}
portfolio={}
def display_stocks():
    print("\n"+"="*55)
    print("             AVAILABLE STOCKS")
    print("="*55)
    for stock,price in stock_prices.items():
        print(f"{stock:<10} : ${price}")
    print("="*55)
def add_stock():
    while True:
        stock=input("\nEnter stock symbol: ").upper().strip()
        if stock not in stock_prices:
            print("Stock not available. Please choose from the listed stocks.")
            continue
        try:
            quantity=int(input("Enter quantity: "))
            if quantity<=0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        portfolio[stock]=portfolio.get(stock,0)+quantity
        print(f"{quantity} share(s) of {stock} added successfully.")
        break
def calculate_total():
    total=0
    for stock,quantity in portfolio.items():
        total+=stock_prices[stock]*quantity
    return total
def display_portfolio():
    print("\n"+"="*65)
    print("                 STOCK PORTFOLIO")
    print("="*65)
    if not portfolio:
        print("Your portfolio is empty.")
        print("="*65)
        return
    print(f"{'Stock':<12}{'Quantity':<12}{'Price':<15}{'Investment':<15}")
    print("-"*65)
    for stock,quantity in portfolio.items():
        price=stock_prices[stock]
        investment=price*quantity
        print(f"{stock:<12}{quantity:<12}${price:<14}${investment:<14}")
    print("-"*65)
    print(f"{'TOTAL INVESTMENT':<39}${calculate_total()}")
    print("="*65)
def save_report():
    if not portfolio:
        print("\nPortfolio is empty. Add stocks before saving.")
        return
    filename="portfolio_report.txt"
    with open(filename,"w") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("="*50+"\n")
        for stock,quantity in portfolio.items():
            price=stock_prices[stock]
            investment=price*quantity
            file.write(f"Stock: {stock}\n")
            file.write(f"Quantity: {quantity}\n")
            file.write(f"Price: ${price}\n")
            file.write(f"Investment: ${investment}\n")
            file.write("-"*50+"\n")
        file.write(f"Total Investment: ${calculate_total()}\n")
    print(f"\nPortfolio report saved successfully as '{filename}'.")
def main():
    print("="*55)
    print("          STOCK PORTFOLIO TRACKER")
    print("="*55)
    print("Track your stock investments using predefined prices.")
    while True:
        print("\n1. View Available Stocks")
        print("2. Add Stock to Portfolio")
        print("3. View Portfolio")
        print("4. Save Portfolio Report")
        print("5. Exit")
        choice=input("\nEnter your choice: ").strip()
        if choice=="1":
            display_stocks()
        elif choice=="2":
            display_stocks()
            add_stock()
        elif choice=="3":
            display_portfolio()
        elif choice=="4":
            save_report()
        elif choice=="5":
            print("\nThank you for using Stock Portfolio Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
if __name__=="__main__":
    main()
