def sales_sum(sales_list):
    total = 0
    for sale in sales_list:
        total += sale
    return total
def weekly_sales():
    sales = []
    for i in range(7):
        sales_day = float(input("Enter sales for day {}: ".format(i+1)))
        sales.append(sales_day)
    return sales

def main():
    sales = weekly_sales()
    total_weekly_sales = sales_sum(sales)
    print("The total weekly sales is ${:.2f}".format(total_weekly_sales))

main()