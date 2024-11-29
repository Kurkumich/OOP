# --*-- encoding: utf-8 --*--
import json
from typing import List
from decimal import Decimal
from Product import Product


class ProductRepJSON(Product):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_all(self) -> List[Product]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return [Product.create_from_json(json.dumps(item)) for item in data]
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден. Возвращается пустой список.")
            return []
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
            return []

    def write_all(self, products: List[Product]) -> None:
        try:
            data = [json.loads(product.to_json()) for product in products]
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка записи в файл {self.file_path}: {e}")

    def add_product(self, product: Product) -> None:
        products = self.read_all()
        product.product_id = self.generate_new_id(products)
        products.append(product)
        self.write_all(products)

    def delete_product(self, product_id: int) -> None:
        products = self.read_all()
        products = [product for product in products if product.product_id != product_id]
        self.write_all(products)

    def get_by_id(self, product_id: int) -> Product:
       
        products = self.read_all()
        for product in products:
            if product.product_id == product_id:
                return product
        raise ValueError(f"Продукт с ID {product_id} не найден.")

    def get_k_n_short_list(self, k: int, n: int) -> List[Product]:
        
        products = self.read_all()
        start_index = k * n
        end_index = start_index + n
        return products[start_index:end_index]

    def sort_by_field(self, field: str) -> List[Product]:
       
        products = self.read_all()
        try:
            return sorted(products, key=lambda p: getattr(p, field))
        except AttributeError:
            raise ValueError(f"Поле {field} не существует в объекте Product.")

    def update_product(self, product_id: int, updated_product: Product) -> None:
        
        products = self.read_all()
        for i, product in enumerate(products):
            if product.product_id == product_id:
                updated_product.product_id = product_id  # Сохраняем ID оригинального продукта
                products[i] = updated_product
                self.write_all(products)
                return
        raise ValueError(f"Продукт с ID {product_id} не найден.")

    def generate_new_id(self, products: List[Product]) -> int:
       
        existing_ids = {product.product_id for product in products}
        new_id = 1
        while new_id in existing_ids:
            new_id += 1
        return new_id

    def get_count(self) -> int:
            
            products = self.read_all()
            return len(products)
