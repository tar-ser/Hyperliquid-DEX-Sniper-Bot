# Backend: Key decryption
from cryptography.fernet import Fernet

def decrypt_key(encrypted_key: str) -> str:
    cipher_suite = Fernet(settings.CRYPTO_KEY)
    return cipher_suite.decrypt(encrypted_key.encode()).decode()
