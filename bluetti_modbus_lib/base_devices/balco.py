from . import BluettiDevice
from ..fields import uint16


class BaseDeviceBalco(BluettiDevice):
    # Inverter summmary
    d_num_inverters = uint16(50001, unit="pcs")
    ac_o_p_total = uint16(50002, unit="W")
    pv_i_p_total = uint16(50004, unit="W")
    g_i_p_total = uint16(50006, unit="W")
    # TBD
    pv_ac_p = uint16(50010, unit="W")
    ac_o_e_total = uint16(50012, unit="kWh", scale=0.1)
    pv_i_e_total = uint16(50014, unit="kWh", scale=0.1)
    g_i_e_total = uint16(50016, unit="kWh", scale=0.1)
    g_o_e_total = uint16(50018, unit="kWh", scale=0.1)
    pv_ac_e = uint16(50020, unit="kWh", scale=0.1)
    # TODO Status registers
    g_i_f = uint16(50214, unit="Hz", scale=0.1)
    # MPPT details
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
