from . import BluettiDevice
from ..fields import UIntField

class BaseDeviceBalco(BluettiDevice):
    def __init__(self):
        super().__init__(
            [
                UIntField("soc", 50217, "W", min=0, max=100),   # TODO wrong register
            ],
        )
