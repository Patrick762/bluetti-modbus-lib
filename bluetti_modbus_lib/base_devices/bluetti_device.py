from typing import List

from ..fields import DeviceField


class BluettiDevice:
    def __init__(
        self,
        fields: List[DeviceField],
    ):
        self.fields = fields

        self.fields.sort(key=lambda f: f.address)
