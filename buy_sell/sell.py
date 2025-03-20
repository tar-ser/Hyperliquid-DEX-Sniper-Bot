def sell_trailing_stop(
    self,
    symbol: str,
    amount: float,
    activation_price: float,
    trailing_percent: float,
    immediate_execute: bool = False
) -> Dict:
    
    # 1. Checking the availability of an item
    position = self._get_position(symbol)
    if position["size"] < amount:
        raise PositionError("Not enough coins to sell")
    
    # 2. Trailing stop parameters
    trailing_stop_payload = {
        "symbol": symbol,
        "type": "TRAILING_STOP",
        "side": "SELL",
        "amount": amount,
        "activationPrice": activation_price,
        "trailingDelta": trailing_percent * 100,  # in basis points
        "immediateExecute": immediate_execute
    }
    
    # 3. Dynamic price update
    current_price = self._get_market_price(symbol)
    if current_price >= activation_price:
        trailing_stop_payload["activationPrice"] = current_price * 0.98  # slip protection
    
    # 4. Sending of a warrant
    headers = self._sign_request(trailing_stop_payload)
    response = self.session.post(
        f"{self.base_url}/order", 
        json=trailing_stop_payload,
        headers=headers
    )
    
    # 5. Verification
    if response.json().get("status") == "FILLED":
        self._update_portfolio(symbol, -amount)
    
    return response.json()
