import requests

url = "https://patrick762.github.io/bluetti-registers/devices.json"

output = "bluetti_modbus_lib/devices/"

print("Loading devices list")

devices_json = requests.get(url).json()


def to_camel_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


def get_type(t: str, name: str):
    upper = t.upper()

    if upper == "BOOL":
        return "UINT16"

    if upper == "SWSTRING":
        return "STRING"

    if upper != "UINT" and upper != "INT":
        return upper

    if upper == "INT":
        return "INT16"

    if name in ["b_i_e", "b_o_e"]:  # Could be checked using field size == 2
        return "UINT32"

    return "UINT16"


for d in devices_json:
    if d["comm_type"] != "modbus":
        continue

    name = d["name"]
    file_name = str(name).lower() + ".py"
    fields = ""

    for f in d["fields"]:
        fields += f"""
    {f["name"]} = field(
        t=FieldType.{get_type(str(f["datatype"]), f["name"])},
        address={f["start"]},"""

        if "unit" in f:
            fields += f'\n\t\tunit="{f["unit"]}",'

        if "scaling" in f:
            fields += f"\n\t\tscale={f["scaling"]},"

        if "category" in f:
            fields += f"\n\t\tcategory=FieldCategory.{str(f["category"]).upper()},"

        if "state_type" in f:
            fields += (
                f"\n\t\tstate_class=FieldStateClass.{str(f["state_type"]).upper()},"
            )

        if "writable" in f:
            fields += f"\n\t\twritable={str(f["writable"])},"

        if "sensor" in f:
            fields += f"\n\t\tdevice_class=DeviceClass.{str(f["sensor"]).upper()},"

        if "length" in f and f["datatype"] in ["string", "swstring"]:
            fields += f"\n\t\tlength={f["length"]},"

        if "length" in f and f["datatype"] not in ["string", "swstring"]:
            fields += f"\n\t\tcount={f["length"]},"

        if f["name"] == "d_control_mode":
            fields += f"\n\t\tenum_type=ControlMode,"

        if f["name"] == "d_inverter_fault":
            fields += f"\n\t\tenum_type=InverterFault,"

        if f["name"] == "d_inverter_status":
            fields += f"\n\t\tenum_type=InverterStatus,"

        if f["name"] == "d_inverter_warning":
            fields += f"\n\t\tenum_type=InverterWarning,"

        # TODO enum building

        fields += "\n\t)"

    content = f"""from ..base_devices import BluettiDevice
from ..fields import field, FieldType
from ..fields.field_extras import FieldCategory, FieldStateClass, DeviceClass
from ..enums import *

# GENERATED FILE! DO NOT EDIT!


class {name}(BluettiDevice):{fields}
"""

    with open(output + file_name, "w") as f:
        f.write(content.replace("\t", "    "))
