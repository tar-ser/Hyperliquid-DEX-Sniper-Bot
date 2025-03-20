<VolatilityAdjustmentCard>
  <IndicatorSelector 
    :options="['ATR', 'Standard Deviation', 'Bollinger Bands']"
    v-model="config.volatility_settings.metrics.primary_indicator"
  />
  <RangeSlider
    label="Position Size Range"
    :min="0.5" :max="5" 
    v-model:lower="config.volatility_settings.adaptive_parameters.position_size_scaling.min_size_percent"
    v-model:upper="config.volatility_settings.adaptive_parameters.position_size_scaling.max_size_percent"
  />
</VolatilityAdjustmentCard>
