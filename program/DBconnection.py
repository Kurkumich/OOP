import pymysql
from decimal import Decimal
from Product import Product

class DBConnection:
    _instance = None

    def __new__(cls, host, user, password, database):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance.connection = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                cursorclass=pymysql.cursors.DictCursor
            )
        return cls._instance

    def get_connection(self):
        return self.connection

    def close(self):
        self.connection.close()

class ProductRepDB:
    def __init__(self, db_connection: DBConnection):
        self.connection = db_connection.get_connection()

    def get_by_id(self, product_id):
        with self.connection.cursor() as cursor:
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
        with self.connection.cursor() as cursor:
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
        with self.connection.cursor() as cursor:
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
            self.connection.commit()
            product.product_id = cursor.lastrowid
            return product.product_id

    def update_by_id(self, product_id, product):
        with self.connection.cursor() as cursor:
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
            self.connection.commit()
            return cursor.rowcount > 0

    def delete_by_id(self, product_id):
        with self.connection.cursor() as cursor:
            sql = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(sql, (product_id,))
            self.connection.commit()
            return cursor.rowcount > 0

    def get_count(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT COUNT(*) AS count FROM products"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count'] if result else 0

    def close(self):
        self.connection.close()


# Пример использования

db_connection = DBConnection(host="localhost", user="root", password="3redroseS%", database="lombard_db")
product_repo = ProductRepDB(db_connection)

new_product = Product(
    name="Кулон",
    description="Кулон из серебра",
    price=Decimal("12000.00"),
    stock_quantity=5,
    material="серебро"
)

new_product_id = product_repo.add(new_product)
print(f"Добавлен новый продукт с ID: {new_product_id}")

product_repo.close()
