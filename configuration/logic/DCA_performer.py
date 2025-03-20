def execute_DCA_strategy(initial_order):
    for layer in config.DCA_layers:
        target_price = initial_order.price * (1 - layer.price_drop_percent/100)
        place_limit_order(
            price=target_price,
            amount=initial_order.amount * (layer.size_percent/100)
        )
