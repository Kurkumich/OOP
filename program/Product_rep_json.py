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
