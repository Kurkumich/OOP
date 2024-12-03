import json
from typing import List
from ProductRepFileStrategy import ProductRepFileStrategy
import os


class JSONFileStrategy(ProductRepFileStrategy):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> List[dict]:
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
            return []

    def write(self, data: List[dict]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


