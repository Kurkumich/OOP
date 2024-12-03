from typing import List
from Product import Product
from ProductRepFileStrategy import ProductRepFileStrategy

class ProductRepository:
    def __init__(self, strategy: ProductRepFileStrategy):
        self.strategy = strategy

    def read_all(self) -> List[Product]:
        data = self.strategy.read()
        return [Product.create_from_dict(item) for item in data]

    def write_all(self, products: List[Product]) -> None:
        data = [product.to_dict() for product in products]
        self.strategy.write(data)

    def add_product(self, product: Product) -> None:
        products = self.read_all()
        if any(p.product_code == product.product_code for p in products):
            raise ValueError(f"Продукт с кодом {product.product_code} уже существует.")
        products = self.read_all()
        product.product_id = self.generate_new_id(products)
        products.append(product)
        self.write_all(products)

    def delete_product(self, product_id: int) -> None:
        products = [product for product in self.read_all() if product.product_id != product_id]
        self.write_all(products)

    def get_by_id(self, product_id: int) -> Product:
        for product in self.read_all():
            if product.product_id == product_id:
                return product
        raise ValueError(f"Продукт с ID {product_id} не найден.")

    def generate_new_id(self, products: List[Product]) -> int:
        existing_ids = {product.product_id for product in products}
        new_id = 1
        while new_id in existing_ids:
            new_id += 1
        return new_id


