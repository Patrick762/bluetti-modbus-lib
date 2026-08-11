from ..enums import InverterStatus, InverterWarning, InverterFault
from . import BluettiDevice
from ..fields import field, FieldType
from ..fields.field_extras import FieldCategory, FieldStateClass, DeviceClass


class BaseDeviceBalco(BluettiDevice):
    d_num_inverters = field(
        FieldType.UINT16,
        50001,
        category=FieldCategory.DIAGNOSTIC,
    )
    ac_o_p_total = field(
        FieldType.UINT16,
        50002,
        unit="W",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.POWER,
    )
    pv_i_p_total = field(
        FieldType.UINT16,
        50004,
        unit="W",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.POWER,
    )
    g_i_p_total = field(
        FieldType.UINT16,
        50006,
        unit="W",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.POWER,
    )
    d_inverter_total = field(
        FieldType.UINT16,
        50008,
        unit="W",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.POWER,
    )
    pv_ac_p = field(
        FieldType.UINT16,
        50010,
        unit="W",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.POWER,
    )
    ac_o_e_total = field(
        FieldType.UINT16,
        50012,
        unit="kWh",
        scale=0.1,
        state_class=FieldStateClass.TOTAL_INCREASING,
        device_class=DeviceClass.ENERGY,
    )
    pv_i_e_total = field(
        FieldType.UINT16,
        50014,
        unit="kWh",
        scale=0.1,
        state_class=FieldStateClass.TOTAL_INCREASING,
        device_class=DeviceClass.ENERGY,
    )
    g_i_e_total = field(
        FieldType.UINT16,
        50016,
        unit="kWh",
        scale=0.1,
        state_class=FieldStateClass.TOTAL_INCREASING,
        device_class=DeviceClass.ENERGY,
    )
    g_o_e_total = field(
        FieldType.UINT16,
        50018,
        unit="kWh",
        scale=0.1,
        state_class=FieldStateClass.TOTAL_INCREASING,
        device_class=DeviceClass.ENERGY,
    )
    pv_ac_e = field(
        FieldType.UINT16,
        50020,
        unit="kWh",
        scale=0.1,
        state_class=FieldStateClass.TOTAL_INCREASING,
        device_class=DeviceClass.ENERGY,
    )
    d_inverter_status = field(
        FieldType.ENUM,
        50022,
        enum_type=InverterStatus,
        category=FieldCategory.DIAGNOSTIC,
    )
    d_inverter_warning = field(
        FieldType.ENUM,
        50023,
        enum_type=InverterWarning,
        count=4,
        category=FieldCategory.DIAGNOSTIC,
    )
    d_inverter_fault = field(
        FieldType.ENUM,
        50027,
        enum_type=InverterFault,
        count=5,
        category=FieldCategory.DIAGNOSTIC,
    )
    d_inverter_type = field(
        FieldType.STRING,
        50200,
        length=6,
        category=FieldCategory.DIAGNOSTIC,
    )
    # TODO
    g_i_f = field(
        FieldType.UINT16,
        50214,
        unit="Hz",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.FREQUENCY,
    )
    # TODO
    pv_1_i_p = field(
        FieldType.UINT16,
        50269,
        unit="W",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.POWER,
    )
    pv_1_i_v = field(
        FieldType.UINT16,
        50270,
        unit="V",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.VOLTAGE,
    )
    pv_1_i_c = field(
        FieldType.UINT16,
        50271,
        unit="A",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.CURRENT,
    )
    pv_2_i_p = field(
        FieldType.UINT16,
        50273,
        unit="W",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.POWER,
    )
    pv_2_i_v = field(
        FieldType.UINT16,
        50274,
        unit="V",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.VOLTAGE,
    )
    pv_2_i_c = field(
        FieldType.UINT16,
        50275,
        unit="A",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.CURRENT,
    )
    pv_3_i_p = field(
        FieldType.UINT16,
        50277,
        unit="W",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.POWER,
    )
    pv_3_i_v = field(
        FieldType.UINT16,
        50278,
        unit="V",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.VOLTAGE,
    )
    pv_3_i_c = field(
        FieldType.UINT16,
        50279,
        unit="A",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.CURRENT,
    )
    pv_4_i_p = field(
        FieldType.UINT16,
        50281,
        unit="W",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.POWER,
    )
    pv_4_i_v = field(
        FieldType.UINT16,
        50282,
        unit="V",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.VOLTAGE,
    )
    pv_4_i_c = field(
        FieldType.UINT16,
        50283,
        unit="A",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.CURRENT,
    )
    # TODO PV 5 if needed
    ac_o_switch = field(
        FieldType.UINT16,
        57001,
        writable=True,
    )
    g_i_switch = field(
        FieldType.UINT16,
        57009,
        writable=True,
        category=FieldCategory.CONFIG,
    )
    g_o_switch = field(
        FieldType.UINT16,
        57010,
        writable=True,
        category=FieldCategory.CONFIG,
    )
    b_soc_low = field(
        FieldType.UINT16,
        57016,
        writable=True,
        unit="%",
        category=FieldCategory.CONFIG,
    )
    b_soc_high = field(
        FieldType.UINT16,
        57017,
        writable=True,
        unit="%",
        category=FieldCategory.CONFIG,
    )
    d_num_battery_packs = field(
        FieldType.UINT16,
        51001,
        category=FieldCategory.DIAGNOSTIC,
    )
    b_v_total = field(
        FieldType.UINT16,
        51002,
        unit="V",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.VOLTAGE,
    )
    b_c_total = field(
        FieldType.UINT16,
        51003,
        unit="A",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.CURRENT,
    )
    b_soc_total = field(
        FieldType.UINT16,
        51004,
        unit="%",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.BATTERY,
    )
    b_soh_total = field(
        FieldType.UINT16,
        51005,
        unit="%",
        state_class=FieldStateClass.MEASUREMENT,
        category=FieldCategory.DIAGNOSTIC,
    )
    # TODO
    d_battery_type = field(
        FieldType.STRING,
        51200,
        length=6,
        category=FieldCategory.DIAGNOSTIC,
    )
    # TODO
    b_v = field(
        FieldType.UINT16,
        51219,
        unit="V",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.VOLTAGE,
    )
    b_c = field(
        FieldType.UINT16,
        51220,
        unit="A",
        scale=0.1,
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.CURRENT,
    )
    b_soc = field(
        FieldType.UINT16,
        51221,
        unit="%",
        state_class=FieldStateClass.MEASUREMENT,
        device_class=DeviceClass.BATTERY,
    )
    b_soh = field(
        FieldType.UINT16,
        51222,
        unit="%",
        category=FieldCategory.DIAGNOSTIC,
    )
    b_cycle_count = field(
        FieldType.UINT16,
        51223,
        state_class=FieldStateClass.MEASUREMENT,
        category=FieldCategory.DIAGNOSTIC,
    )
    b_t_avg = field(
        FieldType.INT16,
        51224,
        unit="°C",
        state_class=FieldStateClass.MEASUREMENT,
        category=FieldCategory.DIAGNOSTIC,
        device_class=DeviceClass.TEMPERATURE,
    )
    b_cell_count = field(
        FieldType.UINT16,
        51234,
        category=FieldCategory.DIAGNOSTIC,
    )
    b_ntc_count = field(
        FieldType.UINT16,
        51235,
        category=FieldCategory.DIAGNOSTIC,
    )
    b_i_e = field(
        FieldType.UINT32,
        51236,
        unit="Wh",
        state_class=FieldStateClass.TOTAL_INCREASING,
        device_class=DeviceClass.ENERGY,
    )
    b_o_e = field(
        FieldType.UINT32,
        51238,
        unit="Wh",
        state_class=FieldStateClass.TOTAL_INCREASING,
        device_class=DeviceClass.ENERGY,
    )
    # TODO
