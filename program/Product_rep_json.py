#--*-- encoding: utf-8 --*--
import json
from typing import List
from Product import Product
from decimal import Decimal
from ProductRepository import ProductRepository


class ProductRepJSON(ProductRepository):
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
