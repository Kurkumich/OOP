import pymysql
from decimal import Decimal
from Product import Product
from Product_Rep_DB import ProductRepDB

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
