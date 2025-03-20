from decimal import Decimal, getcontext

getcontext().prec = 8  # Для точных финансовых расчетов

class TradingBot:
    def __init__(self, config):
        self.config = config
        self.data_feed = DataFeed(config['ws_url'])
        self.risk_manager = RiskManager(config['initial_balance'])
        self.trading_engine = TradingEngine(
            config['api_key'], 
            config['api_secret']
        )
        
        self.data_feed.add_callback(self._on_market_data)
        
    async def _on_market_data(self, data: dict):
        if self._check_arbitrage(data):
            self._execute_arbitrage()
            
        if self._check_large_order(data):
            self._snipe_order()
            
    def _check_arbitrage(self, data) -> bool:
        # Простая логика арбитража
        return (
            data['price_diff'] >= self.config['min_arb_spread']
            and data['liq'] >= self.config['min_liq']
        )
        
    def _execute_arbitrage(self):
        order = {
            "symbol": "ETH/USDT",
            "side": "buy",
            "type": "limit",
            "amount": self._calc_position_size(),
            "price": self._best_ask_price()
        }
        
        if self.risk_manager.can_open_position(order['amount'], order['price']):
            try:
                result = self.trading_engine.execute_order(order)
                self._log_trade(result)
            except Exception as e:
                self._handle_error(e)
                
    def _log_trade(self, result):
        with open("trades.log", "a") as f:
            f.write(f"{time.ctime()}|{json.dumps(result)}\n")
