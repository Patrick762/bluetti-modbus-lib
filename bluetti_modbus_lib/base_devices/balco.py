from . import BluettiDevice
from ..fields import UIntField

class BaseDeviceBalco(BluettiDevice):
    def __init__(self):
        super().__init__(
            [
                UIntField("num_packs", 51001, "pcs", min=1, max=16),
                UIntField("total_bat_voltage", 51002, "V", multiplier=0.1),
                UIntField("total_bat_current", 51003, "A", multiplier=0.1),
                UIntField("total_bat_soc", 51004, "%", min=0, max=100),
                UIntField("total_bat_soh", 51005, "%", min=0, max=100),

                UIntField("total_bat_charge_time", 51007, "Min"),
                UIntField("total_bat_discharge_time", 51008, "Min"),

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
