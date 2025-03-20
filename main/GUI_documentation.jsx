// Context help with examples
<StrategyParameter
  name="Take Profit %"
  value={config.takeProfit}
  info={
    <>
      <p>Example: At a value of 3% and an entry price of $100:</p>
      <ul>
        <li>Цель: $103</li>
        <li>Размер ордера: {calculateOrderSize(103)}</li>
      </ul>
      <VideoTutorial url="tutorials/take-profit.mp4" />
    </>
  }
/>
