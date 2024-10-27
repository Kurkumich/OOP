# --*-- encoding: cp1251 --*--
import json
from decimal import Decimal
from datetime import date


class BriefProduct:
    def __init__(self, product_id: int, name: str, price: Decimal):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, BriefProduct):
            return False
        return (self.product_id == other.product_id and
                self.name == other.name and
                self.price == other.price)

    def __hash__(self):
        return hash((self.product_id, self.name, self.price))


class Product(BriefProduct):
    def __init__(self, product_id: int = 0, name: str = "", description: str = "", price: Decimal = Decimal(0), stock_quantity: int = 0, material: str = ""):
        super().__init__(product_id, name, price)
        self.description = description
        self.stock_quantity = stock_quantity
        self.material = material

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
    def update_existing_product(cls, product_id: int, name: str, description: str, price: Decimal, stock_quantity: int, material: str):
        return cls(product_id=product_id, name=name, description=description, price=price, stock_quantity=stock_quantity, material=material)

    @classmethod
    def create_from_string(cls, product_string: str):
        parts = product_string.split(",")
        if len(parts) != 6:
            raise ValueError("Invalid product string format. Expected 6 comma-separated values.")
        try:
            return cls(
                product_id=int(parts[0].strip()),
                name=parts[1].strip(),
                description=parts[2].strip(),
                price=Decimal(parts[3].strip()),
                stock_quantity=int(parts[4].strip()),
                material=parts[5].strip()
            )
        except ValueError as e:
            raise ValueError("Invalid number format in product string.") from e

    @classmethod
    def create_from_json(cls, json_string: str):
        data = json.loads(json_string)
        return cls(
            product_id=data['product_id'],
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
            'price': str(self.price),
            'stock_quantity': self.stock_quantity,
            'material': self.material
        }, ensure_ascii=False)

    def __str__(self):
        return f"Product(productId={self.product_id}, name='{self.name}', description='{self.description}', price={self.price}, stockQuantity={self.stock_quantity}, material='{self.material}')"


class Client:
    def __init__(self, first_name: str, last_name: str, middle_name: str, passport_number: str, address: str):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.passport_number = passport_number
        self.address = address

    def __str__(self):
        return f"Client(firstName='{self.first_name}', lastName='{self.last_name}', middleName='{self.middle_name}', passportNumber='{self.passport_number}', address='{self.address}')"


class Loan:
    def __init__(self, client: Client, product: Product, loan_amount: Decimal, commission: Decimal, return_date: date):
        self.client = client
        self.product = product
        self.loan_amount = loan_amount
        self.commission = commission
        self.return_date = return_date
        self.is_repaid = False

    def __str__(self):
        return (f"Loan(client={self.client}, product={self.product}, loanAmount={self.loan_amount}, "
                f"commission={self.commission}, returnDate={self.return_date}, isRepaid={self.is_repaid})")


if __name__ == "__main__":
    try:
        product = Product.create_new_product(
            name="Золотое кольцо",
            description="Кольцо с изумрудом",
            price=Decimal("15000.00"),
            stock_quantity=5,
            material="Золото"
        )
        client = Client(
            first_name="Иван",
            last_name="Иванов",
            middle_name="Иванович",
            passport_number="1234 567890",
            address="ул. Пушкина, дом Колотушкина"
        )

        loan = Loan(
            client=client,
            product=product,
            loan_amount=Decimal("12000.00"),
            commission=Decimal("500.00"),
            return_date=date(2023, 12, 31)
        )
        # print(client)
        print(product)
        # print(loan)

    except ValueError as e:
        print("Error:", e)
