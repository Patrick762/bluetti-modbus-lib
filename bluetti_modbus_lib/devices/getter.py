from modbus_connection import ModbusUnit

from .balco260 import Balco260


def get_device(d: str, unit: ModbusUnit | None = None):
    if d == "balco260":
        return Balco260(unit)
    else:
        return None
