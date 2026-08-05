from typing import Any

from pymodbus.client import ModbusTcpClient

from . import DeviceField, FieldName


class UIntField(DeviceField):
    def __init__(
        self,
        name: FieldName,
        address: int,
        unit: str,
        multiplier: float = 1,
        min: int | None = None,
        max: int | None = None,
    ):
        super().__init__(name, address, unit, 1)
        self.multiplier = multiplier
        self.min = min
        self.max = max

    def parse(self, client: ModbusTcpClient, data: bytes) -> Any:
        return (
            client.convert_from_registers(
                data,
                client.DATATYPE.UINT16,
                word_order="little",
            )
            * self.multiplier
        )

    def in_range(self, value: int) -> bool:
        if self.min is not None and self.min > value:
            return False
        if self.max is not None and self.max < value:
            return False
        return value >= 0
