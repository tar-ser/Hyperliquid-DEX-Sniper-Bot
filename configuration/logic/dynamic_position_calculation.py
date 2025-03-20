def calculate_position_size(volatility_score: float) -> float:
    min_size = config.volatility_settings.adaptive_parameters.position_size_scaling.min_size_percent
    max_size = config.volatility_settings.adaptive_parameters.position_size_scaling.max_size_percent
    return min_size + (max_size - min_size) * (volatility_score / 100)
