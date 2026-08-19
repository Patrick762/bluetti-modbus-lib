# bluetti-modbus-lib
Inofficial Library for basic communication to bluetti powerstations via Modbus.

Based on official documentation https://github.com/bluetti-official/bluetti-modbus-tcp-slave

You have to enable Modbus TCP in the webinterface of your device first.

## Disclaimer
This library is provided without any warranty or support by Bluetti. I do not take responsibility for any problems it may cause in all cases. Use it at your own risk.

## Supported devices and data

TBD

## Installation

```bash
pip install bluetti-modbus-lib
```

## Affiliate links (Anzeige / Ad)

If you want to support this project and buy a bluetti device, you can use the following affiliate links:

- <a href="https://tidd.ly/4x4iKBJ" target="_blank" rel="sponsored">Balco 260</a>

> [!NOTE]
> DE: Bei diesem Link handelt es sich um einen Affiliate-Link. Wenn du darüber kaufst, erhalte ich eine kleine Provision. Für dich entstehen keine Zusatzkosten.
> EN: This is an affiliate link. If you make a purchase through it, I may earn a small commission at no extra cost to you.

## Commands for testing

Commands included in this library should only be used for testing.

### Read device data for supported devices

```bash
usage: bluetti-modread [-h] [-c HOST] [-p PORT] [-t TYPE]

Read bluetti devices via modbus

options:
  -h, --help            show this help message and exit
  -c HOST, --host HOST  IP-address of the device
  -p PORT, --port PORT  Port of the device
  -t TYPE, --type TYPE  Device type
```

Example:

```bash
bluetti-modread -c 10.2.1.60 -p 502 -t balco260
```

Example output:

```bash
num_inverters: 1 pcs
ac_load_power_total: 0 W
pv_power_total: 0 W
grid_power_total: 0 W
inverter_out_power_total: 0 W
pv_to_ac_power: 0 W
ac_load_energy_total: 0.1 kWh
pv_to_ac_load_energy_total: 0.1 kWh
pc_charging_energy_total: 0.0 kWh
grid_charging_energy_total: 0.0 kWh
grid_export_energy_total: 0.0 kWh
input_power_pv1: 0 W
input_voltage_pv1: 0.0 V
input_current_pv1: 0.0 A
input_power_pv2: 0 W
input_voltage_pv2: 0.0 V
input_current_pv2: 0.0 A
input_power_pv3: 0 W
input_voltage_pv3: 0.0 V
input_current_pv3: 0.0 A
input_power_pv4: 0 W
input_voltage_pv4: 0.0 V
input_current_pv4: 0.0 A
num_packs: 0 pcs
total_bat_voltage: 25.900000000000002 V
total_bat_current: 0.7000000000000001 A
total_bat_soc: 0 %
total_bat_soh: 0 %
total_bat_charge_time: 0 Min
total_bat_discharge_time: 0 Min
pack_voltage: 25.900000000000002 V
pack_current: 2999.3 A
pack_soc: 36 %
pack_soh: 100 %
pack_cycles: 0 times
pack_temp_avg: 0 °C
pack_cell_count: 8 pcs
pack_ntc_count: 4 pcs
pack_energy_charged: 2580 Wh
pack_energy_discharged: 2500 Wh
```
