class PlatformNotFoundError(Exception):
    """Exception raise when the platform specified is not supported."""

    def __init__(self):
        self.error_message = "'CLIENT_TYPE' was not set in your environment. Check your env setup."
        super().__init__(self.error_message)

class PlatformNotSupportedError(Exception):
    """Exception raise when the platform specified is not supported."""

    def __init__(self, platform: str):
        self.error_message = f"'{platform}' is not a currently supported platform."
        super().__init__(self.error_message)