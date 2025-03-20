# Strategy Simulator
class BacktestRunner:
    def run(self, config: BacktestConfig):
        try:
            self.validate_config(config)
            results = self.execute_simulation()
            return {
                "success": True,
                "metrics": self.calculate_metrics(results),
                "chart_data": self.generate_chart_data(results)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "stack_trace": traceback.format_exc()  # Full debugging
            }
