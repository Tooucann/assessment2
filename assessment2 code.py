class Product:
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.monthly_units_manufactured = monthly_units_manufactured

    def display_product_info(self):
        print("Product Code:", self.code)
        print("Product Name:", self.name)
        print("Product Sale Price:", self.sale_price)
        print("Product Manufacture Cost:", self.manufacture_cost)
        print("Stock Level:", self.stock_level)
        print("Estimated Monthly Units Manufactured:", self.monthly_units_manufactured)


def get_user_input():
    code = int(input("Enter Product Code (100 to 1000): "))
    name = input("Enter Product Name: ")
    sale_price = float(input("Enter Product Sale Price: "))
    manufacture_cost = float(input("Enter Product Manufacture Cost: "))
    stock_level = int(input("Enter Stock Level: "))
    monthly_units_manufactured = int(input("Enter Estimated Monthly Units Manufactured: "))

    return code, name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured


def calculate_monthly_data(product, month):
    units_sold = min(product.monthly_units_manufactured, product.stock_level)
    product.stock_level += product.monthly_units_manufactured  
    product.stock_level -= units_sold
    earnings = units_sold * product.sale_price
    return units_sold, product.stock_level, earnings


def main():
    code, name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured = get_user_input()

   
    if 100 <= code <= 1000:
        product = Product(code, name, sale_price, manufacture_cost, stock_level, monthly_units_manufactured)
        product.display_product_info()
        total_earnings = 0

        for month in range(1, 13):
            print(f"\nMonth {month} Data:")
            units_sold, stock_level, earnings = calculate_monthly_data(product, month)
            total_earnings += earnings

            print("Units Sold:", units_sold)
            print("Units in Stock:", max(0, stock_level))
            print("Total Money Earned:", earnings)

        print("\nTotal Money Earned in 12 Months:", total_earnings)

    else:
        print("Invalid Product Code. Please enter a code between 100 and 1000.")


if __name__ == "__main__":
    main()