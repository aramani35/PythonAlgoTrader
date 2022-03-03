import alpaca_trade_api
import pinject
import os

import common.entity.platformparams as platformparams
import trader.alpacaaccountinfoprovider as alpacaaccountinfoprovider
import trader.alpacaorderexecutor as alpacaorderexecutor

from alpaca_trade_api.common import URL
from exceptions.platformexceptions import PlatformNotFoundError, PlatformNotSupportedError

# Perform initial os environment argument validation when class is initialized
def validate_client_type():
    client_type = os.getenv('CLIENT_TYPE')
    if client_type is None:
        raise PlatformNotFoundError()

    if not platformparams.SupportedPlatforms.contains_value(client_type.upper()):
        raise PlatformNotSupportedError(client_type)

    return platformparams.SupportedPlatforms(client_type.upper())

class PlatformClientBindings(pinject.BindingSpec):

    def provide_platform_rest_client(self):
        client_type = validate_client_type()
        if client_type == platformparams.SupportedPlatforms.ALPACA:
            return alpaca_trade_api.rest.REST(
                key_id=os.getenv('API_KEY_ID'), 
                secret_key=os.getenv('API_SECRET_KEY'), 
                base_url=URL(os.getenv('API_BASE_URL'))
            )

    def provide_platform_stream_client(self):
        client_type = self.validate_client_type()
        if client_type == platformparams.SupportedPlatforms.ALPACA:
            return alpaca_trade_api.stream.Stream(
                os.getenv(key_id='API_KEY_ID', 
                secret_key='API_SECRET_KEY', 
                base_url=URL(os.getenv('API_BASE_URL')), 
                data_feed='IEX') 
            )

class ApplicationBindings(pinject.BindingSpec):

    def configure(self, bind):
        client_type = validate_client_type()
        if client_type == platformparams.SupportedPlatforms.ALPACA:
            bind('account_info_provider', to_class=alpacaaccountinfoprovider.AlpacaAccountInfoProvider)
            bind('order_executor', to_class=alpacaorderexecutor.AlpacaOrderExecutor)

    def dependencies(self):
        return [PlatformClientBindings()]

APP_BINDINGS = [ApplicationBindings()]
