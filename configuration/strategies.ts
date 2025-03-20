interface StrategyConfig {
  name: "DCA" | "Arbitrage" | "Sniper";
  params: {
    [key: string]: number | boolean | string[];
  };
}
