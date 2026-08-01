from . import BluettiDevice
from ..fields import UIntField

# TODO Strings, Versions, Enums, SN

class BaseDeviceBalco(BluettiDevice):
    def __init__(self):
        super().__init__(
            [
                # Inverter summmary
                UIntField("num_inverters", 50001, "pcs", min=1, max=10),
                UIntField("ac_load_power_total", 50002, "W"),
                UIntField("pv_power_total", 50004, "W"),
                UIntField("grid_power_total", 50006, "W"),
                UIntField("inverter_out_power_total", 50008, "W"),
                UIntField("pv_to_ac_power", 50010, "W"),

                UIntField("ac_load_energy_total", 50012, "kWh", multiplier=0.1),
                UIntField("pc_charging_energy_total", 50014, "kWh", multiplier=0.1),
                UIntField("grid_charging_energy_total", 50016, "kWh", multiplier=0.1),
                UIntField("grid_export_energy_total", 50018, "kWh", multiplier=0.1),
                UIntField("pv_to_ac_load_energy_total", 50012, "kWh", multiplier=0.1),

                # MPPT details
                UIntField("input_power_pv1", 50269, "W"),
                UIntField("input_voltage_pv1", 50270, "V", multiplier=0.1),
                UIntField("input_current_pv1", 50271, "A", multiplier=0.1),

                UIntField("input_power_pv2", 50273, "W"),
                UIntField("input_voltage_pv2", 50274, "V", multiplier=0.1),
                UIntField("input_current_pv2", 50275, "A", multiplier=0.1),

                UIntField("input_power_pv3", 50277, "W"),
                UIntField("input_voltage_pv3", 50278, "V", multiplier=0.1),
                UIntField("input_current_pv3", 50279, "A", multiplier=0.1),

                UIntField("input_power_pv4", 50281, "W"),
                UIntField("input_voltage_pv4", 50282, "V", multiplier=0.1),
                UIntField("input_current_pv4", 50283, "A", multiplier=0.1),

                # Pack Summary
                UIntField("num_packs", 51001, "pcs", min=1, max=16),
                UIntField("total_bat_voltage", 51002, "V", multiplier=0.1),
                UIntField("total_bat_current", 51003, "A", multiplier=0.1),
                UIntField("total_bat_soc", 51004, "%", min=0, max=100),
                UIntField("total_bat_soh", 51005, "%", min=0, max=100),

                UIntField("total_bat_charge_time", 51007, "Min"),
                UIntField("total_bat_discharge_time", 51008, "Min"),

                # Single pack details
                UIntField("pack_voltage", 51219, "V", multiplier=0.1),
                UIntField("pack_current", 51220, "A", multiplier=0.1),
                UIntField("pack_soc", 51221, "%", min=0, max=100),
                UIntField("pack_soh", 51222, "%", min=0, max=100),
                UIntField("pack_cycles", 51223, "times"),
                UIntField("pack_temp_avg", 51224, "°C"),
                UIntField("pack_cell_count", 51234, "pcs"),
                UIntField("pack_ntc_count", 51235, "pcs"),
                UIntField("pack_energy_charged", 51236, "Wh"),
                UIntField("pack_energy_discharged", 51238, "Wh"),
            ],
        )
