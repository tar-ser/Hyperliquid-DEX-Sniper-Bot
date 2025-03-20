from typing import Dict

class RiskManager:
    def __init__(self, initial_balance: float):
        self.balance = initial_balance
        self.max_daily_loss = 0.05  # 5%
        self.max_position_size = 0.02  # 2%
        self.daily_loss = 0.0
        
    def can_open_position(self, amount: float, price: float) -> bool:
        position_value = amount * price
        risk_checks = [
            position_value <= self.balance * self.max_position_size,
            self.daily_loss < self.balance * self.max_daily_loss,
            amount > 0
        ]
        return all(risk_checks)
        
    def update_after_trade(self, pnl: float):
        self.daily_loss += abs(min(0, pnl))
        self.balance += pnl
        
    def reset_daily_limits(self):
        self.daily_loss = 0.0
