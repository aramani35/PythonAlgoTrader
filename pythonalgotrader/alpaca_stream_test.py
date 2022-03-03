import os

from alpaca_trade_api.common import URL
from alpaca_trade_api.stream import Stream
from dotenv import load_dotenv

load_dotenv()

async def trade_callback(t):
    print('trade', t)


async def quote_callback(q):
    print('quote', q)


# Initiate Class Instance
stream = Stream(
    key_id=os.getenv('API_KEY_ID'), 
                secret_key=os.getenv('API_SECRET_KEY'), 
                base_url=URL(os.getenv('API_BASE_URL')), 
                data_feed='iex'
)  # <- replace to SIP if you have PRO subscription

# subscribing to event
stream.subscribe_trades(trade_callback, 'AAPL')
stream.subscribe_quotes(quote_callback, 'IBM')

print('hi')
stream.run()