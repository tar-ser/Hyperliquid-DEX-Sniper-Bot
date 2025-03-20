// React-component of checking before sending an order
const RiskChecklist = ({ order }) => {
  const checks = [
    {
      name: 'Liquidity',
      status: order.pool.liquidity > config.minLiquidity,
      message: `Minimum ${formatCurrency(config.minLiquidity)}`
    },
    {
      name: 'Slippage',
      status: order.slippage < config.maxSlippage,
      message: `Макс. ${config.maxSlippage}%`
    }
  ];

  return (
    <div className="risk-checklist">
      {checks.map((check, i) => (
        <div key={i} className={`check ${check.status ? 'passed' : 'failed'}`}>
          <Icon type={check.status ? 'check' : 'close'} />
          {check.name}: {check.message}
        </div>
      ))}
    </div>
  );
};
