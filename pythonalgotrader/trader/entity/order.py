from __future__ import annotations
from alpaca_trade_api.entity import Order as AlpacaOrder
from pydantic.dataclasses import dataclass
from typing import Optional

@dataclass
class Order:
    id: str
    symbol: str
    qty: float
    filled_qty: float
    filled_avg_price: Optional[float] # in USD
    asset_class: str
    side: str
    type: str

    @classmethod
    def from_alpaca_order(cls, alpaca_order: AlpacaOrder) -> Order:
        return Order(
            id=alpaca_order.id, 
            symbol=alpaca_order.symbol, 
            qty=alpaca_order.qty, 
            filled_qty=alpaca_order.filled_qty, 
            filled_avg_price=alpaca_order.filled_avg_price, 
            asset_class=alpaca_order.asset_class, 
            side=alpaca_order.side, 
            type=alpaca_order.type
        )
