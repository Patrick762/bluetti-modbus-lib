from . import BluettiDevice
from ..fields import UIntField

# TODO Strings, Versions, Enums, SN

class BaseDeviceBalco(BluettiDevice):
    def __init__(self):
        super().__init__(
            [
                # Inverter summmary
                UIntField("d_num_inverters", 50001, "pcs", min=1, max=10),
                UIntField("ac_o_p_total",    50002, "W"),
                UIntField("pv_i_p_total",    50004, "W"),
                UIntField("g_i_p_total",     50006, "W"),
                #UIntField("inverter_out_power_total", 50008, "W"),
                UIntField("pv_ac_p",         50010, "W"),   # TODO: check

                UIntField("ac_o_e_total", 50012, "kWh", multiplier=0.1),
                UIntField("pv_i_e_total", 50014, "kWh", multiplier=0.1),
                UIntField("g_i_e_total",  50016, "kWh", multiplier=0.1),
                UIntField("g_o_e_total",  50018, "kWh", multiplier=0.1),
                UIntField("pv_ac_e",      50012, "kWh", multiplier=0.1),

                # TODO Status registers

                UIntField("g_i_f", 50214, "Hz", multiplier=0.1),

                # MPPT details
                UIntField("pv_1_i_p", 50269, "W"),
                UIntField("pv_1_i_v", 50270, "V", multiplier=0.1),
                UIntField("pv_1_i_c", 50271, "A", multiplier=0.1),

                UIntField("pv_2_i_p", 50273, "W"),
                UIntField("pv_2_i_v", 50274, "V", multiplier=0.1),
                UIntField("pv_2_i_c", 50275, "A", multiplier=0.1),

                UIntField("pv_3_i_p", 50277, "W"),
                UIntField("pv_3_i_v", 50278, "V", multiplier=0.1),
                UIntField("pv_3_i_c", 50279, "A", multiplier=0.1),

                UIntField("pv_4_i_p", 50281, "W"),
                UIntField("pv_4_i_v", 50282, "V", multiplier=0.1),
                UIntField("pv_4_i_c", 50283, "A", multiplier=0.1),

                # Pack Summary
                UIntField("d_num_packs", 51001, "pcs", min=1, max=16),
                UIntField("b_v_total", 51002, "V", multiplier=0.1),
                UIntField("b_c_total", 51003, "A", multiplier=0.1),
                UIntField("b_soc_total", 51004, "%", min=0, max=100),
                UIntField("b_soh_total", 51005, "%", min=0, max=100),

                #UIntField("total_bat_charge_time", 51007, "Min"),
                #UIntField("total_bat_discharge_time", 51008, "Min"),

                # Single pack details
                #UIntField("pack_voltage", 51219, "V", multiplier=0.1),
                #UIntField("pack_current", 51220, "A", multiplier=0.1),
                #UIntField("pack_soc", 51221, "%", min=0, max=100),
                #UIntField("pack_soh", 51222, "%", min=0, max=100),
                #UIntField("pack_cycles", 51223, "times"),
                #UIntField("pack_temp_avg", 51224, "°C"),
                #UIntField("pack_cell_count", 51234, "pcs"),
                #UIntField("pack_ntc_count", 51235, "pcs"),
                #UIntField("pack_energy_charged", 51236, "Wh"),
                #UIntField("pack_energy_discharged", 51238, "Wh"),
            ],
        )
