from modbus_connection.model import Component


class BluettiDevice(Component):
    max_gap = 5
    max_span = 50

    def field_names(self):
        return self._register_fields.keys()

    def get_field(self, field_name: str):
        return self._register_fields.get(field_name)

    def get_sensors(self):
        return self.field_names()
