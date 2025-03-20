// Frontend: Encrypting keys before sending them to the server
import { encrypt } from 'crypto-js';

const handleSaveAPIKey = (key: string, secret: string) => {
  const encrypted = {
    key: encrypt(key, process.env.REACT_APP_CRYPTO_SECRET).toString(),
    secret: encrypt(secret, process.env.REACT_APP_CRYPTO_SECRET).toString()
  };
  localStorage.setItem('apiKeys', JSON.stringify(encrypted));
};
