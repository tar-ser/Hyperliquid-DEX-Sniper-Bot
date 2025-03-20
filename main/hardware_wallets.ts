// Connecting Ledger via Web3
const connectLedger = async () => {
  try {
    const transport = await TransportWebUSB.create();
    const eth = new Eth(transport);
    const { address } = await eth.getAddress("44'/60'/0'/0/0");
    return {
      success: true,
      address: address,
      publicKey: await eth.getAppConfiguration()
    };
  } catch (error) {
    return {
      success: false,
      error: 'Проверьте подключение устройства',
      details: error.message
    };
  }
};
