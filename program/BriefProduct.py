# --*-- encoding: cp1251 --*--
import json
from decimal import Decimal, InvalidOperation
import random
import string

class BriefProduct:
    def __init__(self, name: str, price: Decimal, product_code: str = None):
        self.name = name
        self.price = price 
        self.product_code = product_code or self.generate_product_code()

    @staticmethod
    def generate_product_code(name: str):
        name_part = name[:3].upper()
        unique_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return f"{name_part}{unique_part}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # Преобразуем строку в Decimal, если это необходимо
        if isinstance(value, str):
            value = Decimal(value)

        if value <= Decimal(0) or value > Decimal(1_000_000):
            raise ValueError("Price must be greater than 0 and less than or equal to 1,000,000.")

        try:
            if abs(value.as_tuple().exponent) > 2:
                raise ValueError("Price can have at most two decimal places.")
        except InvalidOperation:
            raise ValueError("Invalid decimal format for price.")

        self._price = value

    def __eq__(self, other):
        if not isinstance(other, BriefProduct):
            return False
        return (self.name == other.name and
                self.price == other.price and
                self.product_code == other.product_code)
