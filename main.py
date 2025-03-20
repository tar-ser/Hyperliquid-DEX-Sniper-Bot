if __name__ == "__main__":
    config = ConfigManager().load_config()
    
    if not config:
        print("First-time setup...")
        config = {
            "api_key": input("API Key: "),
            "api_secret": input("API Secret: "),
            "initial_balance": 100_000,
            "ws_url": "wss://api.hyperliquid.xyz/ws"
        }
        ConfigManager().save_config(config)
        
    bot = TradingBot(config)
    
    try:
        print("Starting trading bot...")
        bot.data_feed.start()
    except KeyboardInterrupt:
        print("\nGraceful shutdown...")
        bot.risk_manager.reset_daily_limits()
