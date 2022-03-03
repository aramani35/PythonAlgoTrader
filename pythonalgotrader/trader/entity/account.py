from __future__ import annotations
from alpaca_trade_api.entity import Account as AlpacaAccount
from pydantic.dataclasses import dataclass
from typing import Optional

@dataclass
class Account:
    account_name: str 
    account_id: str
    buying_power: float
    balance: float
    value: float
    currency: str
    daytrade_count: Optional[int] = None

    @classmethod
    def from_alpaca_account(cls, alpaca_account: AlpacaAccount) -> Account:
        return Account(
            account_name=alpaca_account.account_number, 
            account_id=alpaca_account.id, 
            buying_power=alpaca_account.buying_power, 
            balance=alpaca_account.cash, 
            value=alpaca_account.portfolio_value, 
            currency=alpaca_account.currency, 
            daytrade_count=alpaca_account.daytrade_count
        )