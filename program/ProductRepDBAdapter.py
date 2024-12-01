from typing import List
from decimal import Decimal
from Product import Product
from ProductRepository import ProductRepository
from DBconnection import DBConnection, ProductRepDB


class ProductRepDBAdapter(ProductRepository):
    def __init__(self, db_connection: DBConnection):
        self.db_repo = ProductRepDB(db_connection)

    def read_all(self) -> List[Product]:

        raise NotImplementedError("Метод read_all не реализован для ProductRepDB.")

    def write_all(self, products: List[Product]) -> None:
        raise NotImplementedError("Метод write_all не поддерживается для ProductRepDB.")

    def add_product(self, product: Product) -> None:
        self.db_repo.add(product)

    def delete_product(self, product_id: int) -> None:
        self.db_repo.delete_by_id(product_id)

    def get_by_id(self, product_id: int) -> Product:
        return self.db_repo.get_by_id(product_id)

    def get_k_n_short_list(self, k: int, n: int) -> List[Product]:
        return self.db_repo.get_k_n_short_list(k, n)

    def update_product(self, product_id: int, updated_product: Product) -> None:
        if not self.db_repo.update_by_id(product_id, updated_product):
            raise ValueError(f"Продукт с ID {product_id} не найден.")

    def get_count(self) -> int:
        return self.db_repo.get_count()
