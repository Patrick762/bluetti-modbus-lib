from typing import Any

from modbus_connection import WordOrder
from modbus_connection.model import RegisterField, WriteValidator
from modbus_connection.model.fields import NumberField


class BluettiStringField(RegisterField[str]):
    def decode(self, words: list[int], scale_exponent: int | None = None) -> str:
        raw = b"".join((w & 0xFFFF).to_bytes(2, "little") for w in words)
        return raw.decode("ascii", errors="ignore").rstrip("\x00")

    def encode(self, value: Any, scale_exponent: int | None = None) -> list[int]:
        length = self.count
        raw = str(value).encode("ascii", errors="ignore")[: length * 2]
        raw = raw.ljust(length * 2, b"\x00")
        return [int.from_bytes(raw[i : i + 2], "little") for i in range(0, len(raw), 2)]


def uint16(
    address: int,
    *,
    scale: float = 1.0,
    writable: bool | WriteValidator = False,
    unit: str | None = None,
):
    return NumberField(
        address,
        scale=scale,
        word_order="little",
        signed=False,
        writable=writable,
        unit=unit,
    )


def int16(
    address: int,
    *,
    scale: float = 1.0,
    writable: bool | WriteValidator = False,
    unit: str | None = None,
):
    return NumberField(
        address,
        scale=scale,
        word_order="little",
        signed=True,
        writable=writable,
        unit=unit,
    )


def bluetti_string(
    address: int,
    length: int,
):
    return BluettiStringField(
        address,
        count=length,
        stride=0,
        writable=False,
        force_fc16=False,
    )
