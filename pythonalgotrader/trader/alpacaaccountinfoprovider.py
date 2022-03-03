from typing import List

from .accountinfoprovider import AccountInfoProvider
from .entity.account import Account
from .entity.order import Order
from .entity.position import Position
from alpaca_trade_api.rest import REST


class AlpacaAccountInfoProvider(AccountInfoProvider):
    """Responsible for retrieving account information from alpaca"""
    
    def __init__(self, platform_rest_client: REST) -> None:
        self.alpaca_client = platform_rest_client

    def get_account_info(self) -> Account:
        return Account.from_alpaca_account(self.alpaca_client.get_account())

    def list_open_positions(self) -> List[Position]:
        return [Position.from_alpaca_position(pos) for pos in self.alpaca_client.list_positions()]

    def get_position_for_symbol(self, symbol: str) -> Position:
        return Position.from_alpaca_position(self.alpaca_client.get_position(symbol))

    def list_open_orders(self, timestamp: int = None) -> Order:
        return [Order.from_alpaca_order(ord) for ord in self.alpaca_client.list_orders(status='open', after=timestamp)]
        
