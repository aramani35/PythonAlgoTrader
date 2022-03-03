from __future__ import annotations
from alpaca_trade_api.entity import Position as AlpacaPosition
from pydantic.dataclasses import dataclass
from typing import Optional

@dataclass
class Position():
    symbol: str
    qty: float
    avg_entry_price: float
    exchange: str
    asset_class: str
    market_value: float
    side: Optional[str] = None

    @classmethod
    def from_alpaca_position(cls, alpaca_position: AlpacaPosition) -> Position:
        return Position(
            symbol=alpaca_position.symbol, 
            qty=alpaca_position.qty, 
            avg_entry_price=alpaca_position.avg_entry_price, 
            exchange=alpaca_position.exchange, 
            asset_class=alpaca_position.asset_class, 
            market_value=alpaca_position.market_value, 
            side=alpaca_position.side
        )