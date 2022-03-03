
from abc import ABC, abstractmethod
from typing import List

from .entity.account import Account
from .entity.position import Position
from .entity.order import Order

class AccountInfoProvider(ABC):
    @abstractmethod
    def get_account_info(self) -> Account:
        pass

    @abstractmethod
    def list_open_positions(self) -> List[Position]:
        pass

    @abstractmethod
    def get_position_for_symbol(self, symbol: str) -> Position:
        pass

    @abstractmethod
    def list_open_orders(self, timestamp: int = None) -> Order:
        pass