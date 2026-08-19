from modbus_connection import ModbusUnit

from ..base_devices.ebox import BaseDeviceEbox
from .balco260 import Balco260


def get_device(d: str, unit: ModbusUnit | None = None):
    if d == "balco260":
        return Balco260(unit)
    if d == "ebox":
        return BaseDeviceEbox(unit)
    else:
        return None
