import tabulate

def get_ordered_sales(connection):
    with connection.cursor() as cursor:
        sql = f'''
                    SELECT seller.seller_name, item_sum.total_value, sale.customer_name, sale.item_name, sale.item_value, sale.created_at 
                    from sale
                    left join seller on seller.id = sale.seller_id
                    left join
                        (select seller_id, sum(item_value) as total_value
                        from sale
                        group by seller_id 
                        order by sum(item_value) DESC) item_sum on sale.seller_id = item_sum.seller_id
                    order by total_value desc;
                '''
        cursor.execute(sql)
        result = cursor.fetchall()

    return result

def pretty_print_sale_report(sales):
    headers = sales[0].keys()
    rows =  [sale.values() for sale in sales]
    print(tabulate.tabulate(rows, headers))