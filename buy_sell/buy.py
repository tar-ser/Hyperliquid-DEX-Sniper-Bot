def buy_limit_order(
    self,
    symbol: str,
    amount: float,
    limit_price: float,
    slippage: float = 0.5,
    stop_loss: Optional[float] = None,
    take_profit: Optional[float] = None
) -> Dict:
    
    # 1. Safety checks
    if not self._validate_balance("USDT", amount * limit_price):
        raise ValueError("Insufficient balance")
        
    if not self._check_liquidity(symbol, amount):
        raise LiquidityError(f"Not enough liquidity for {amount} {symbol}")
    
    # 2. Slip calculation
    calculated_slippage = self._calculate_slippage(symbol, amount)
    if calculated_slippage > slippage:
        raise SlippageExceededError(calculated_slippage)
    
    # 3. Creating an order
    order_payload = {
        "symbol": symbol,
        "side": "BUY",
        "type": "LIMIT",
        "amount": amount,
        "price": limit_price,
        "stopLoss": stop_loss,
        "takeProfit": take_profit
    }
    
    # 4. Signing and sending
    headers = self._sign_request(order_payload)
    response = self.session.post(
        f"{self.base_url}/order",
        json=order_payload,
        headers=headers
    )
    
    # 5. Logging and returns
    if response.status_code == 200:
        self._log_order(order_payload)
        return response.json()
    else:
        raise OrderFailedError(response.text)
