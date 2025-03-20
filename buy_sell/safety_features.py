def _get_balance(self, coin: str) -> float:
    response = self.session.get(
        f"{self.base_url}/balance",
        headers=self._sign_request({"coin": coin})
    )
    return float(response.json()["available"])

def _get_position(self, symbol: str) -> Dict:
    response = self.session.get(
        f"{self.base_url}/position/{symbol}",
        headers=self._sign_request({})
    )
    return response.json()

def validate_order_params(self, params: Dict) -> bool:
    required = ["symbol", "side", "type", "amount"]
    return all(k in params for k in required) and params["amount"] > 0
