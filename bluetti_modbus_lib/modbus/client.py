import logging
from typing import Any, List

import async_timeout
from pymodbus.client import ModbusTcpClient
from dataclasses import dataclass

from ..base_devices.bluetti_device import BluettiDevice

LOGGER = logging.getLogger(__name__)

@dataclass
class ClientReturnValue:
    name: str
    unit: str
    value: Any

    def __str__(self):
        return f"{self.name}: {self.value} {self.unit}"

class BluettiModbusClient:
    def __init__(self, host: str, port: int, device: BluettiDevice):
        self.client = ModbusTcpClient(host, port=port)
        self.device = device

    async def read(self) -> List[ClientReturnValue]:
        buffer = []

        try:
            async with async_timeout.timeout(5):
                LOGGER.debug("Connecting to device ...")

                # Connect to device
                retries_left = 5
                while retries_left > 0:
                    LOGGER.debug(f"{retries_left} retries remaining")
                    if not self.client.connected:
                        self.client.connect()
                        retries_left = retries_left - 1
                    else:
                        break
                
                LOGGER.debug("Connected to device")

                # Read registers
                for register in self.device.fields:
                    LOGGER.debug(f"Reading register at address {register.address}")

                    result = self.client.read_holding_registers(
                        address=register.address,
                    )

                    if len(result.registers) == 1:
                        parsed = register.parse(self.client, result.registers)
                        buffer.append(ClientReturnValue(register.name, register.unit, parsed))

        except TimeoutError:
            LOGGER.error("Timeout")
        finally:
            self.client.close()

        return buffer
