from ..enums import InverterStatus, InverterWarning, InverterFault
from . import BluettiDevice
from ..fields import field, FieldType
from ..fields.field_extras import FieldCategory, FieldStateClass, DeviceClass


class BaseDeviceBalco(BluettiDevice):
    d_num_inverters = field(FieldType.UINT16, 50001, unit="pcs")
    ac_o_p_total = field(FieldType.UINT16, 50002, unit="W")
    pv_i_p_total = field(FieldType.UINT16, 50004, unit="W")
    g_i_p_total = field(FieldType.UINT16, 50006, unit="W")
    d_inverter_total = field(FieldType.UINT16, 50008, unit="W")
    pv_ac_p = field(FieldType.UINT16, 50010, unit="W")
    ac_o_e_total = field(FieldType.UINT16, 50012, unit="kWh", scale=0.1)
    pv_i_e_total = field(FieldType.UINT16, 50014, unit="kWh", scale=0.1)
    g_i_e_total = field(FieldType.UINT16, 50016, unit="kWh", scale=0.1)
    g_o_e_total = field(FieldType.UINT16, 50018, unit="kWh", scale=0.1)
    pv_ac_e = field(FieldType.UINT16, 50020, unit="kWh", scale=0.1)
    d_inverter_status = field(FieldType.ENUM, 50022, enum_type=InverterStatus)
    d_inverter_warning = field(
        FieldType.ENUM, 50023, enum_type=InverterWarning, count=4
    )
    d_inverter_fault = field(FieldType.ENUM, 50027, enum_type=InverterFault, count=5)
    d_inverter_type = field(FieldType.STRING, 50200, length=6)
    # TODO
    g_i_f = field(FieldType.UINT16, 50214, unit="Hz", scale=0.1)
    # TODO
    pv_1_i_p = field(FieldType.UINT16, 50269, unit="W")
    pv_1_i_v = field(FieldType.UINT16, 50270, unit="V", scale=0.1)
    pv_1_i_c = field(FieldType.UINT16, 50271, unit="A", scale=0.1)
    pv_2_i_p = field(FieldType.UINT16, 50273, unit="W")
    pv_2_i_v = field(FieldType.UINT16, 50274, unit="V", scale=0.1)
    pv_2_i_c = field(FieldType.UINT16, 50275, unit="A", scale=0.1)
    pv_3_i_p = field(FieldType.UINT16, 50277, unit="W")
    pv_3_i_v = field(FieldType.UINT16, 50278, unit="V", scale=0.1)
    pv_3_i_c = field(FieldType.UINT16, 50279, unit="A", scale=0.1)
    pv_4_i_p = field(FieldType.UINT16, 50281, unit="W")
    pv_4_i_v = field(FieldType.UINT16, 50282, unit="V", scale=0.1)
    pv_4_i_c = field(FieldType.UINT16, 50283, unit="A", scale=0.1)
    # TODO PV 5 if needed
    ac_o_switch = field(FieldType.UINT16, 57001, writable=True)
    g_i_switch = field(FieldType.UINT16, 57009, writable=True)
    g_o_switch = field(FieldType.UINT16, 57010, writable=True)
    b_soc_low = field(FieldType.UINT16, 57016, writable=True, unit="%")
    b_soc_high = field(FieldType.UINT16, 57017, writable=True, unit="%")
    d_num_battery_packs = field(FieldType.UINT16, 51001, unit="pcs")
    b_v_total = field(FieldType.UINT16, 51002, unit="V", scale=0.1)
    b_c_total = field(FieldType.UINT16, 51003, unit="A", scale=0.1)
    b_soc_total = field(FieldType.UINT16, 51004, unit="%")
    b_soh_total = field(FieldType.UINT16, 51005, unit="%")
    # TODO
    d_battery_type = field(FieldType.STRING, 51200, length=6)
    # TODO
    b_v = field(FieldType.UINT16, 51219, unit="V", scale=0.1)
    b_c = field(FieldType.UINT16, 51220, unit="A", scale=0.1)
    b_soc = field(FieldType.UINT16, 51221, unit="%")
    b_soh = field(FieldType.UINT16, 51222, unit="%")
    b_cycle_count = field(FieldType.UINT16, 51223)
    b_t_avg = field(FieldType.INT16, 51224, unit="°C")
    b_cell_count = field(FieldType.UINT16, 51234, unit="pcs")
    b_ntc_count = field(FieldType.UINT16, 51235, unit="pcs")
    b_i_e = field(FieldType.UINT32, 51236, unit="Wh")
    b_o_e = field(
        FieldType.UINT32,
        51238,
        unit="Wh",
        category=FieldCategory.DIAGNOSTIC,
        state_class=FieldStateClass.TOTAL_INCREASING,
        device_class=DeviceClass.ENERGY,
    )
    # TODO
