# --*-- encoding: utf-8 --*--
import yaml
from typing import List
from Product import Product
from decimal import Decimal
from ProductRepository import ProductRepository


class ProductRepYAML(ProductRepository):
    def read_all(self) -> List[Product]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = yaml.safe_load(file)
            return [Product.create_from_yaml(yaml.dump(item)) for item in data]
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден. Возвращается пустой список.")
            return []
        except yaml.YAMLError as e:
            print(f"Ошибка декодирования YAML: {e}")
            return []

    def write_all(self, products: List[Product]) -> None:
        try:
            data = [yaml.safe_load(product.to_yaml()) for product in products]
            with open(self.file_path, "w", encoding="utf-8") as file:
                yaml.dump(data, file, allow_unicode=True, default_flow_style=False)
        except Exception as e:
            print(f"Ошибка записи в файл {self.file_path}: {e}")
