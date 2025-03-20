import time
import hashlib
import hmac

class TradingEngine:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.last_order_time = 0
        self.min_order_interval = 0.5  # 500ms cooldown
        
    def _sign_request(self, endpoint: str, data: dict) -> dict:
        nonce = str(int(time.time() * 1000))
        message = f"{nonce}{endpoint}{json.dumps(data)}"
        signature = hmac.new(
            self.api_secret.encode(),
            msg=message.encode(),
            digestmod=hashlib.sha256
        ).hexdigest()
        
        return {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature,
            "X-NONCE": nonce
        }

    def execute_order(self, order: dict) -> dict:
        # Rate limiting
        if time.time() - self.last_order_time < self.min_order_interval:
            raise Exception("Order rate limit exceeded")
            
        # Validate order schema
        required = ["symbol", "side", "type", "amount"]
        if not all(k in order for k in required):
            raise ValueError("Invalid order structure")
            
        headers = self._sign_request("/order", order)
        # ... actual API request ...
        
        self.last_order_time = time.time()
        return {"status": "success", "order_id": "12345"}
