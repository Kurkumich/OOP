# --*-- encoding: cp1251 --*--
import json
import yaml
from decimal import Decimal
from datetime import date
import random
from BriefProduct import BriefProduct


class Product(BriefProduct):
    def __init__(self, product_id: int = None, name: str = "", description: str = "", price: Decimal = Decimal(0), 
                 stock_quantity: int = 0, material: str = "", product_code: str = None):
        self.product_id = product_id or self.generate_product_id()
        super().__init__(name, price, product_code or self.generate_product_code(material))
        self.description = description
        self.stock_quantity = stock_quantity
        self.material = material

    @staticmethod
    def generate_product_id():
        """Генерация уникального идентификатора продукта."""
        return random.randint(100000, 999999)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("Description must be a non-empty string.")
        self._description = value

    @property
    def stock_quantity(self):
        return self._stock_quantity

    @stock_quantity.setter
    def stock_quantity(self, value: int):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Stock quantity must be a non-negative integer.")
        self._stock_quantity = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value: str):
        if not isinstance(value, str) or not value:
            raise ValueError("Material must be a non-empty string.")
        self._material = value

    @classmethod
    def create_new_product(cls, name: str, description: str, price: Decimal, stock_quantity: int, material: str):
        return cls(name=name, description=description, price=price, stock_quantity=stock_quantity, material=material)

    @classmethod
    def create_from_string(cls, product_string: str):
        parts = product_string.split(",")
        if len(parts) != 5:
            raise ValueError("Invalid product string format. Expected 5 comma-separated values.")
        try:
            return cls(
                name=parts[0].strip(),
                description=parts[1].strip(),
                price=Decimal(parts[2].strip()),
                stock_quantity=int(parts[3].strip()),
                material=parts[4].strip()
            )
        except ValueError as e:
            raise ValueError("Invalid number format in product string.") from e

    @classmethod
    def create_from_json(cls, json_string: str):
        data = json.loads(json_string)
        return cls(
            product_id=data.get('product_id'),
            name=data['name'],
            description=data['description'],
            price=Decimal(data['price']),
            stock_quantity=data['stock_quantity'],
            material=data['material']
        )

    def to_json(self) -> str:
        return json.dumps({
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),  # Преобразуем Decimal в строку для сериализации
            'stock_quantity': self.stock_quantity,
            'material': self.material,
            'product_code': self.product_code
        }, ensure_ascii=False, indent=4)
    
    @classmethod
    def create_from_yaml(cls, yaml_string: str):
        data = yaml.safe_load(yaml_string)  # Загружаем данные из YAML
        return cls(
            product_id=data.get('product_id'),
            name=data['name'],
            description=data['description'],
            price=Decimal(data['price']),
            stock_quantity=data['stock_quantity'],
            material=data['material']
        )
    
    def to_yaml(self) -> str:
        return yaml.dump({
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': str(self.price),
            'stock_quantity': self.stock_quantity,
            'material': self.material,
            'product_code': self.product_code
        }, allow_unicode=True)

    def __str__(self):
        return f"Product(productId={self.product_id}, name='{self.name}', description='{self.description}', price={self.price}, stockQuantity={self.stock_quantity}, material='{self.material}', productCode='{self.product_code}')"


if __name__ == "__main__":
    try:
        product = Product(
            product_id = 1,
            name="Kolco",
            description="Krasivoe",
            price=Decimal("15000.00"),
            stock_quantity=1,
            material="Zoloto"
        )
        print(product)

        yaml_data = """
            product_id: 1
            name: Kolco
            description: Krasivoe
            price: "15000.00"
            stock_quantity: 1
            material: Zoloto
             """
        product = Product.create_from_yaml(yaml_data)
        print(product)
    except ValueError as e:
        print("Error:", e)
