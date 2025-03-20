<template>
  <CollapsibleSection title="Trailing Stop">
    <NumberInput 
      label="Activation Threshold (%)" 
      v-model="config.order_types.stop_orders.stop_loss.activation_threshold_percent"
      :min="0.1" :max="10" step="0.1"
    />
    <NumberInput
      label="Trailing Step (%)"
      v-model="config.order_types.stop_orders.stop_loss.trailing_step_percent"
      :min="0.1" :max="5" step="0.1"
    />
  </CollapsibleSection>
