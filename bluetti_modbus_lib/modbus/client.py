import logging
from typing import Any, List

import async_timeout
from dataclasses import dataclass

from modbus_connection.pymodbus import ModbusConnection, ModbusTcpParams

from ..devices import get_device

LOGGER = logging.getLogger(__name__)


@dataclass
class ClientReturnValue:
    name: str
    unit: str
    value: Any

    def __str__(self):
        return f"{self.name}: {self.value} {self.unit or ""}"


class BluettiModbusClient:
    def __init__(self, host: str, port: int, device_type: str):
        self.conn = ModbusConnection(ModbusTcpParams(host=host, port=port))
        self.device = get_device(device_type, self.conn.for_unit(1))

    async def read(self):
        try:
            await self.conn.connect()

            async with async_timeout.timeout(5):
                LOGGER.debug("Reading device data")

                await self.device.async_update()

        except TimeoutError:
            LOGGER.error("Timeout")
        finally:
            await self.conn.close()

        return [
            ClientReturnValue(name=n, unit=self.device.get_field(n).unit, value=v)
            for (n, v) in self.device._values.items()
        ]
