# Full audit of each transaction
class TradeLogger:
    def log_order(self, order: Order):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "decision_reason": order.metadata.get('trigger_reason'),
            "market_data_snapshot": self.get_market_snapshot(),
            "risk_check": self.last_risk_check,
            "calculated_params": {
                "position_size": order.size,
                "slippage": order.slippage
            }
        }
        save_to_audit_db(log_entry)
