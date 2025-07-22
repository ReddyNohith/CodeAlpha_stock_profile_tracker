stock_prices={
    "infosys": 1581.00,
    "unilever":2513.00,
   "reliance":1482.00,
    "kotak mahindra":2174.90,
    "tcs":3219.80,
    "axis bank":1161.00}
def cal_portfolio():
    portfolio=[]
    total_value=0.00
    print("enter your stocks type done if finished")
    while True:
        market_name=input("enter stock market name:")
        if market_name == "done":
            break
        
        if market_name not in stock_prices:
            print(f"{market_name} not in stock_prices,sorry")
            continue
        try:
            quantity = float(input("enter the quantity:"))
            if quantity < 0:
                print("Quantity should not be negative valued")
                continue
            stock_value=stock_prices[market_name] * quantity
            portfolio.append((market_name,quantity,stock_value))
            total_value += stock_value
        except ValueError:
            print("invalid quantity enter a number")
            continue
    return portfolio,total_value
def portfolio_info(portfolio,total_value):
    print("*"*5,"YOUR STOCK PORTFOLIO","*"*5)
    print("-"*30)
    print(f"{'stock':<10} {'quantity':<10} {"value(INR)":<10}")
    print("-"*30)
    for market_name,quantity,stock_value in portfolio:
        print(f"{market_name:<10} {quantity:<10.2f} {stock_value:<10.2f}")
    print("-"*30)
    print(f"total portfolio value is:{total_value}")
def func(): 
    print("welcome to stock portfolio tracker")
    portfolio,total_value = cal_portfolio()
    if portfolio:
       portfolio_info(portfolio,total_value)
    else:
        print("no stocks entered portfolio is empty")
func()              
            