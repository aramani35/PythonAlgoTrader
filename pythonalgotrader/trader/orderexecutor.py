from abc import ABC, abstractmethod

from .entity.order import Order

class OrderExecutor(ABC):
    @abstractmethod
    def buy(self, symbol: str, qty: float, type: str = 'market', time_in_force='day') -> Order:
        pass

    @abstractmethod
    def sell(self, symbol: str, qty: float, type: str = 'market', time_in_force='day') -> Order:
        pass
