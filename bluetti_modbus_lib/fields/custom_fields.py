from modbus_connection import WordOrder
from modbus_connection.model import WriteValidator
from modbus_connection.model.fields import NumberField


def uint16(
    address: int,
    *,
    scale: float = 1.0,
    word_order: WordOrder = "little",
    writable: bool | WriteValidator = False,
    unit: str | None = None,
):
    return NumberField(
        address,
        scale=scale,
        word_order=word_order,
        signed=False,
        writable=writable,
        unit=unit,
    )
