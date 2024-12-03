from ProductRepository import ProductRepository
from Product import Product

class ProductRepositoryAdapter:

    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def get_k_n_short_list(self, k, n):
        return self._product_repository.get_k_n_short_list(k, n)

    def get_by_id(self, product_id):
        return self._product_repository.get_by_id(product_id)

    def delete_by_id(self, product_id):
        self._product_repository.delete_product(product_id)

    def update_by_id(self, product_id, name, description, price, stock_quantity, material, product_code):
        updated_product = Product.create_from_dict({
            "product_id": product_id,
            "name": name,
            "description": description,
            "price": str(price),
            "stock_quantity": stock_quantity,
            "material": material,
            "product_code": product_code
        })
        self._product_repository.delete_product(product_id)
        self._product_repository.add_product(updated_product)

    def add(self, name, description, price, stock_quantity, material, product_code):
        products = self._product_repository.read_all()

        if any(p.product_code == product_code for p in products):
            raise ValueError(f"Продукт с кодом {product_code} уже существует.")
        
        new_product = Product.create_from_dict({
            "name": name,
            "description": description,
            "price": str(price),
            "stock_quantity": stock_quantity,
            "material": material,
            "product_code": product_code
        })
        self._product_repository.add_product(new_product)

    def get_count(self):
        return len(self._product_repository.read_all())
