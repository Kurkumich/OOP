import pymysql
from decimal import Decimal
from Product import Product
from DBconnection import DBConnection

class ProductRepDB:
    def __init__(self, db_connection: DBConnection):
        self.db_connection = db_connection.get_connection()

    def get_by_id(self, product_id):
        with self.db_connection.cursor() as cursor:  
            sql = "SELECT * FROM products WHERE product_id = %s"
            cursor.execute(sql, (product_id,))
            result = cursor.fetchone()
            if result:
                return Product(
                    product_id=result['product_id'],
                    name=result['name'],
                    description=result['description'],
                    price=Decimal(result['price']),
                    stock_quantity=result['stock_quantity'],
                    material=result['material']
                )
            return None

    def get_k_n_short_list(self, k, n):
        offset = (n - 1) * k
        with self.db_connection.cursor() as cursor: 
            sql = "SELECT product_id, name, price, product_code FROM products LIMIT %s OFFSET %s"
            cursor.execute(sql, (k, offset))
            results = cursor.fetchall()
            return [
                Product(
                    product_id=row['product_id'],
                    name=row['name'],
                    price=Decimal(row['price']),
                    product_code=row['product_code']
                ) for row in results
            ]

    def add(self, product):
        with self.db_connection.cursor() as cursor: 
            sql = """
                INSERT INTO products (name, description, price, stock_quantity, material, product_code)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                product.name,
                product.description,
                str(product.price),
                product.stock_quantity,
                product.material,
                product.product_code
            ))
            self.db_connection.commit()  
            product.product_id = cursor.lastrowid
            return product.product_id

    def update_by_id(self, product_id, product):
        with self.db_connection.cursor() as cursor:  
            sql = """
                UPDATE products
                SET name = %s, description = %s, price = %s, 
                    stock_quantity = %s, material = %s, product_code = %s
                WHERE product_id = %s
            """
            cursor.execute(sql, (
                product.name,
                product.description,
                str(product.price),
                product.stock_quantity,
                product.material,
                product.product_code,
                product_id
            ))
            self.db_connection.commit()  
            return cursor.rowcount > 0

    def delete_by_id(self, product_id):
        with self.db_connection.cursor() as cursor:  
            sql = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(sql, (product_id,))
            self.db_connection.commit()  
            return cursor.rowcount > 0

    def get_count(self):
        with self.db_connection.cursor() as cursor:  
            sql = "SELECT COUNT(*) AS count FROM products"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count'] if result else 0

    def close(self):
        self.db_connection.close() 


