from modbus_connection import ModbusUnit

from .balco260 import Balco260
from .ep2000 import EP2000


def get_device(d: str, unit: ModbusUnit | None = None):
    if d == "balco260":
        return Balco260(unit)
    if d == "ep2000":
        return EP2000(unit)
    else:
        return None
