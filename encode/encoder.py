import json
import os

class Encoder:
    def __init__(self, path):
        self.path = path
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.path):
            print(f"[INFO] Archivo no encontrado: {self.path}. Creando uno nuevo...")
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump({}, f, indent=4, ensure_ascii=False)

    def load(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save(self, data):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
