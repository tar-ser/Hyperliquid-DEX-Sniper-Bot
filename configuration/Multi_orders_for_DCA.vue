<DCALayersConfigurator>
  <div v-for="(layer, index) in config.advanced_strategies.DCA.layers" :key="index">
    <NumberInput 
      :label="`Layer ${index+1} Price Drop (%)`" 
      v-model="layer.price_drop_percent"
    />
    <NumberInput
      :label="`Layer ${index+1} Size (%)`"
      v-model="layer.size_percent"
    />
  </div>
  <Button @click="addDCALayer">+ Add Layer</Button>
</DCALayersConfigurator>
