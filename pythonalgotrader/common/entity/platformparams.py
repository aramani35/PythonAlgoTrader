from enum import Enum

class SupportedPlatforms(Enum):
    ALPACA = 'ALPACA'

    @classmethod
    def contains_value(cls, value: str):
        try:
            cls(value)
        except ValueError:
            return False

        return True
