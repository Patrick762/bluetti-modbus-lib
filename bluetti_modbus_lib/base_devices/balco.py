from . import BluettiDevice
from ..fields import UIntField, FieldName

# TODO Strings, Versions, Enums, SN


class BaseDeviceBalco(BluettiDevice):
    def __init__(self):
        super().__init__(
            [
                # Inverter summmary
                UIntField(FieldName.D_NUM_INVERTERS, 50001, "pcs", min=1, max=10),
                UIntField(FieldName.AC_O_P_TOTAL, 50002, "W"),
                UIntField(FieldName.PV_I_P_TOTAL, 50004, "W"),
                UIntField(FieldName.G_I_P_TOTAL, 50006, "W"),
                # UIntField("inverter_out_power_total", 50008, "W"),
                UIntField(FieldName.PV_AC_P, 50010, "W"),  # TODO: check
                UIntField(FieldName.AC_O_E_TOTAL, 50012, "kWh", multiplier=0.1),
                UIntField(FieldName.PV_I_E_TOTAL, 50014, "kWh", multiplier=0.1),
                UIntField(FieldName.G_I_E_TOTAL, 50016, "kWh", multiplier=0.1),
                UIntField(FieldName.G_O_E_TOTAL, 50018, "kWh", multiplier=0.1),
                UIntField(FieldName.PV_AC_E, 50020, "kWh", multiplier=0.1),
                # TODO Status registers
                UIntField(FieldName.G_I_F, 50214, "Hz", multiplier=0.1),
                # MPPT details
                UIntField(FieldName.PV_1_I_P, 50269, "W"),
                UIntField(FieldName.PV_1_I_V, 50270, "V", multiplier=0.1),
                UIntField(FieldName.PV_1_I_C, 50271, "A", multiplier=0.1),
                UIntField(FieldName.PV_2_I_P, 50273, "W"),
                UIntField(FieldName.PV_2_I_V, 50274, "V", multiplier=0.1),
                UIntField(FieldName.PV_2_I_C, 50275, "A", multiplier=0.1),
                UIntField(FieldName.PV_3_I_P, 50277, "W"),
                UIntField(FieldName.PV_3_I_V, 50278, "V", multiplier=0.1),
                UIntField(FieldName.PV_3_I_C, 50279, "A", multiplier=0.1),
                UIntField(FieldName.PV_4_I_P, 50281, "W"),
                UIntField(FieldName.PV_4_I_V, 50282, "V", multiplier=0.1),
                UIntField(FieldName.PV_4_I_C, 50283, "A", multiplier=0.1),
                # Pack Summary
                UIntField(FieldName.D_NUM_PACKS, 51001, "pcs", min=1, max=16),
                UIntField(FieldName.B_V_TOTAL, 51002, "V", multiplier=0.1),
                UIntField(FieldName.B_C_TOTAL, 51003, "A", multiplier=0.1),
                UIntField(FieldName.B_SOC_TOTAL, 51004, "%", min=0, max=100),
                UIntField(FieldName.B_SOH_TOTAL, 51005, "%", min=0, max=100),
                # UIntField("total_bat_charge_time", 51007, "Min"),
                # UIntField("total_bat_discharge_time", 51008, "Min"),
                # Single pack details
                # UIntField("pack_voltage", 51219, "V", multiplier=0.1),
                # UIntField("pack_current", 51220, "A", multiplier=0.1),
                # UIntField("pack_soc", 51221, "%", min=0, max=100),
                # UIntField("pack_soh", 51222, "%", min=0, max=100),
                # UIntField("pack_cycles", 51223, "times"),
                # UIntField("pack_temp_avg", 51224, "°C"),
                # UIntField("pack_cell_count", 51234, "pcs"),
                # UIntField("pack_ntc_count", 51235, "pcs"),
                # UIntField("pack_energy_charged", 51236, "Wh"),
                # UIntField("pack_energy_discharged", 51238, "Wh"),
            ],
        )
