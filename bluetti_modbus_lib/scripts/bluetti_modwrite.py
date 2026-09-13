import argparse
import asyncio
from typing import Any

from ..modbus import BluettiModbusClient
from ..devices import get_device


async def async_read(host: str, port: int, type: str, field: str, value: Any):
    if get_device(type) is None:
        print("type not supported")
        return

    client = BluettiModbusClient(host, port, type)

    await client.write(field, value)

    print(f"Wrote to device field {field} value {value}")


def start():
    parser = argparse.ArgumentParser(
        description="Write to bluetti device field via modbus"
    )
    parser.add_argument("-c", "--host", type=str, help="IP-address of the device")
    parser.add_argument("-p", "--port", type=int, help="Port of the device")
    parser.add_argument("-t", "--type", type=str, help="Device type")
    parser.add_argument("-f", "--field", type=str, help="Field name")
    parser.add_argument("-v", "--value", type=str, help="Value to write")
    args = parser.parse_args()

    if (
        args.host is None
        or args.port is None
        or args.type is None
        or args.field is None
        or args.value is None
    ):
        parser.print_help()
        return

    asyncio.run(async_read(args.host, args.port, args.type, args.field, args.value))
