import yaml
from ProductRepFileStrategy import ProductRepFileStrategy
from typing import List
import os

class YAMLFileStrategy(ProductRepFileStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> List[dict]:
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return yaml.safe_load(file) or []
        except yaml.YAMLError as e:
            print(f"Ошибка декодирования YAML: {e}")
            return []

    def write(self, data: List[dict]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

