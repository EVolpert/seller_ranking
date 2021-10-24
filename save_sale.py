def save_sale(connection, seller_name, customer_name, item_name, item_value):
    with connection.cursor() as cursor:
        seller_id_sql = f'''
                            SELECT `id` 
                            FROM `seller`
                            WHERE `seller_name` = "{seller_name}"
                        '''
        cursor.execute(seller_id_sql)
        result = cursor.fetchone()

        if result is None:
            raise Exception("There is no seller with that name")
                
        seller_id = result['id']

        sql = f'''INSERT INTO sale
                    (`seller_id`, `customer_name`, `item_name`, `item_value`)
                    VALUES
                    ({seller_id}, "{customer_name}", "{item_name}", {item_value})
                '''
        result = cursor.execute(sql)
    connection.commit()