from abc import ABC, abstractmethod
from typing import List
from decimal import Decimal
from Product import Product


class ProductRepository(ABC):
    def __init__(self, file_path: str):
        self.file_path = file_path

    @abstractmethod
    def read_all(self) -> List[Product]:
        """Прочитать все продукты из хранилища."""
        pass

    @abstractmethod
    def write_all(self, products: List[Product]) -> None:
        """Записать все продукты в хранилище."""
        pass

    def add_product(self, product: Product) -> None:
        """Добавить продукт в хранилище."""
        products = self.read_all()
        product.product_id = self.generate_new_id(products)
        products.append(product)
        self.write_all(products)

    def delete_product(self, product_id: int) -> None:
        """Удалить продукт по ID."""
        products = self.read_all()
        products = [product for product in products if product.product_id != product_id]
        self.write_all(products)

    def get_by_id(self, product_id: int) -> Product:
        """Получить продукт по ID."""
        products = self.read_all()
        for product in products:
            if product.product_id == product_id:
                return product
        raise ValueError(f"Продукт с ID {product_id} не найден.")

    def get_k_n_short_list(self, k: int, n: int) -> List[Product]:
        """Получить страницу продуктов (k-номер страницы, n-количество на странице)."""
        products = self.read_all()
        start_index = k * n
        end_index = start_index + n
        return products[start_index:end_index]

    def sort_by_field(self, field: str) -> List[Product]:
        """Отсортировать продукты по указанному полю."""
        products = self.read_all()
        try:
            return sorted(products, key=lambda p: getattr(p, field))
        except AttributeError:
            raise ValueError(f"Поле {field} не существует в объекте Product.")

    def update_product(self, product_id: int, updated_product: Product) -> None:
        """Обновить информацию о продукте."""
        products = self.read_all()
        for i, product in enumerate(products):
            if product.product_id == product_id:
                updated_product.product_id = product_id
                products[i] = updated_product
                self.write_all(products)
                return
        raise ValueError(f"Продукт с ID {product_id} не найден.")

    def generate_new_id(self, products: List[Product]) -> int:
        """Сгенерировать новый уникальный ID для продукта."""
        existing_ids = {product.product_id for product in products}
        new_id = 1
        while new_id in existing_ids:
            new_id += 1
        return new_id

    def get_count(self) -> int:
        """Получить количество продуктов в хранилище."""
        return len(self.read_all())

