import pymysql
from list_sales import get_ordered_sales, pretty_print_sale_report
from save_sale import save_sale

connection = pymysql.connect(host='localhost',
                             user='shopee_user',
                             password='shopee_pass',
                             database='shopee_test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


print("Welcome to the sale system")
print("Type 'L' for Listing seller rank")
print("Type 'S' to enter a new sale")
print("Type anything else to exit")

mode_input = input("Type desired mode: ")

if mode_input == 'L' or  mode_input == 'l':
    result = get_ordered_sales(connection)
    pretty_print_sale_report(result)
    connection.close()

elif mode_input == 'S' or mode_input == 's':
    print("To enter a new sale please follow the promts request")

    seller_name = input("Type seller name: ")
    customer_name = input("Type customer name: ")
    item_name = input("Type item_name: ")
    item_value = float(input("Type item_value: "))

    save_sale(connection, seller_name, customer_name, item_name, item_value)

    ordered_sales = get_ordered_sales(connection)
    pretty_print_sale_report(ordered_sales)

    connection.close()
    
