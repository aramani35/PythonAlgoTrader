from alpaca_trade_api.rest import REST
from .orderexecutor import OrderExecutor
from .entity.order import Order


class AlpacaOrderExecutor(OrderExecutor):
    def __init__(self, platform_rest_client: REST) -> None:
        self.alpaca_client = platform_rest_client
        
    def buy(self, symbol: str, qty: float, type: str = 'market', time_in_force='day') -> Order:
        return Order.from_alpaca_order(self.alpaca_client.submit_order(
            symbol=symbol, 
            qty=qty, 
            side='buy', 
            type=type, 
            time_in_force=time_in_force
        ))


    def sell(self, symbol: str, qty: float, type: str = 'market', time_in_force='day') -> Order:
        return Order.from_alpaca_order(self.alpaca_client.submit_order(
            symbol=symbol, 
            qty=qty, 
            side='sell', 
            type=type, 
            time_in_force=time_in_force
        ))
