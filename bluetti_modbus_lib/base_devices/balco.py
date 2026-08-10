from modbus_connection.model import enum, uint32

from ..enums import InverterStatus, InverterWarning, InverterFault
from . import BluettiDevice
from ..fields import uint16, int16, bluetti_string


class BaseDeviceBalco(BluettiDevice):
    d_num_inverters = uint16(50001, unit="pcs")
    ac_o_p_total = uint16(50002, unit="W")
    pv_i_p_total = uint16(50004, unit="W")
    g_i_p_total = uint16(50006, unit="W")
    d_inverter_total = uint16(50008, unit="W")
    pv_ac_p = uint16(50010, unit="W")
    ac_o_e_total = uint16(50012, unit="kWh", scale=0.1)
    pv_i_e_total = uint16(50014, unit="kWh", scale=0.1)
    g_i_e_total = uint16(50016, unit="kWh", scale=0.1)
    g_o_e_total = uint16(50018, unit="kWh", scale=0.1)
    pv_ac_e = uint16(50020, unit="kWh", scale=0.1)
    d_inverter_status = enum(50022, InverterStatus, word_order="little")
    d_inverter_warning = enum(50023, InverterWarning, count=4, word_order="little")
    d_inverter_fault = enum(50027, InverterFault, count=5, word_order="little")
    d_inverter_type = bluetti_string(50200, 6)
    # d_inverter_sn = uint32(50206, word_order="little")
    # d_mcu_1_version = bluetti_version(50210)
    # d_mcu_2_version = bluetti_version(50212)
    g_i_f = uint16(50214, unit="Hz", scale=0.1)
    # TODO
    pv_1_i_p = uint16(50269, unit="W")
    pv_1_i_v = uint16(50270, unit="V", scale=0.1)
    pv_1_i_c = uint16(50271, unit="A", scale=0.1)
    pv_2_i_p = uint16(50273, unit="W")
    pv_2_i_v = uint16(50274, unit="V", scale=0.1)
    pv_2_i_c = uint16(50275, unit="A", scale=0.1)
    pv_3_i_p = uint16(50277, unit="W")
    pv_3_i_v = uint16(50278, unit="V", scale=0.1)
    pv_3_i_c = uint16(50279, unit="A", scale=0.1)
    pv_4_i_p = uint16(50281, unit="W")
    pv_4_i_v = uint16(50282, unit="V", scale=0.1)
    pv_4_i_c = uint16(50283, unit="A", scale=0.1)
    # TODO PV 5 if needed
    ac_o_switch = uint16(57001, writable=True)
    g_i_switch = uint16(57009, writable=True)
    g_o_switch = uint16(57010, writable=True)
    b_soc_low = uint16(57016, writable=True, unit="%")
    b_soc_high = uint16(57017, writable=True, unit="%")
    d_num_battery_packs = uint16(51001, unit="pcs")
    b_v_total = uint16(51002, unit="V", scale=0.1)
    b_c_total = uint16(51003, unit="A", scale=0.1)
    b_soc_total = uint16(51004, unit="%")
    b_soh_total = uint16(51005, unit="%")
    # TODO
    d_battery_type = bluetti_string(51200, 6)
    # d_battery_sn = uint32(51206, word_order="little")
    # TODO
    b_v = uint16(51219, unit="V", scale=0.1)
    b_c = uint16(51220, unit="A", scale=0.1)
    b_soc = uint16(51221, unit="%")
    b_soh = uint16(51222, unit="%")
    b_cycle_count = uint16(51223)
    b_t_avg = int16(51224, unit="°C")
    b_cell_count = uint16(51234, unit="pcs")
    b_ntc_count = uint16(51235, unit="pcs")
    b_i_e = uint32(51236, unit="Wh", word_order="little")
    b_o_e = uint32(51238, unit="Wh", word_order="little")
    # TODO
