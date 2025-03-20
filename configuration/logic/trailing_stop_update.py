def update_trailing_stop(current_price: float, entry_price: float):
    activation_threshold = entry_price * (1 + config.stop_orders.activation_threshold_percent/100)
    if current_price > activation_threshold:
        new_stop = current_price * (1 - config.stop_orders.trailing_step_percent/100)
        update_order(new_stop)
