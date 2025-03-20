from cryptography.fernet import Fernet
import json
import os

class ConfigManager:
    def __init__(self, config_path="config.json", key_path="secret.key"):
        self.config_path = config_path
        self.key_path = key_path
        self._ensure_keys_exist()
        
    def _ensure_keys_exist(self):
        if not os.path.exists(self.key_path):
            key = Fernet.generate_key()
            with open(self.key_path, 'wb') as f:
                f.write(key)
                
    def _get_cipher(self):
        with open(self.key_path, 'rb') as f:
            return Fernet(f.read())

    def save_config(self, config: dict):
        cipher = self._get_cipher()
        encrypted = cipher.encrypt(json.dumps(config).encode())
        with open(self.config_path, 'wb') as f:
            f.write(encrypted)

    def load_config(self) -> dict:
        try:
            cipher = self._get_cipher()
            with open(self.config_path, 'rb') as f:
                return json.loads(cipher.decrypt(f.read()).decode())
        except FileNotFoundError:
            return {}
