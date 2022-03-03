import pinject

import appbindings

from alpaca_trade_api.stream import Stream
from dotenv import load_dotenv

import trader.alpacaaccountinfoprovider as alpacaaccountprovider
import trader.alpacaorderexecutor as alpacaorderexecutor


def main():
    load_dotenv()

    all_bindings = [
        *appbindings.APP_BINDINGS
    ]

    obj_graph = pinject.new_object_graph(modules=None, binding_specs=all_bindings)

    account_info_provider = obj_graph.provide(alpacaaccountprovider.AlpacaAccountInfoProvider)
    order_executor = obj_graph.provide(alpacaorderexecutor.AlpacaOrderExecutor)

    print(account_info_provider.get_account_info().buying_power)
    print(account_info_provider.list_open_positions())


#     # Check if our account is restricted from trading.
#     if account.trading_blocked:
#         print('Account is currently restricted from trading.')

# # Check how much money we can use to open new positions.
#     print('${} is available as buying power.'.format(account.buying_power))

if __name__ == '__main__':
    main()
