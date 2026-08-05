from typing import Any

from pymodbus.client import ModbusTcpClient

from ..fields import FieldName


class DeviceField:
    def __init__(self, name: FieldName, address: int, unit: str, size: int):
        self.name = name
        self.address = address
        self.unit = unit
        self.size = size

    def parse(self, client: ModbusTcpClient, data: list[int]) -> Any:
        raise NotImplementedError

    def is_writeable(self) -> bool:
        return False

    def allowed_write_type(self, value: Any) -> bool:
        return False

    def in_range(self, value: Any) -> bool:
        return True
