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

## Sponsoring and Affiliate links (Anzeige / Ad)

If you want to support this project and buy a bluetti device, you can use the sponsors button on github:

> [!NOTE]
> DE: Bei diesem Link handelt es sich um einen Affiliate-Link. Wenn du darüber kaufst, erhalte ich eine kleine Provision. Für dich entstehen keine Zusatzkosten.
>
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
ac_o_e_total: 277.3 kWh (category: n/a) (state_class: FieldStateClass.TOTAL_INCREASING) (device_class: DeviceClass.ENERGY)
ac_o_p_total: 429 W (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.POWER)
ac_o_switch: 0   (category: n/a) (state_class: n/a) (device_class: n/a)
b_c: 2982.6 A (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.CURRENT)
b_c_total: 17.3 A (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.CURRENT)
b_cell_count: 8   (category: FieldCategory.DIAGNOSTIC) (state_class: n/a) (device_class: n/a)
b_cycle_count: 25   (category: FieldCategory.DIAGNOSTIC) (state_class: n/a) (device_class: n/a)
b_i_e: 67.25 kWh (category: n/a) (state_class: FieldStateClass.TOTAL_INCREASING) (device_class: DeviceClass.ENERGY)
b_ntc_count: 4   (category: FieldCategory.DIAGNOSTIC) (state_class: n/a) (device_class: n/a)
b_o_e: 61.17 kWh (category: n/a) (state_class: FieldStateClass.TOTAL_INCREASING) (device_class: DeviceClass.ENERGY)
b_soc: 71 % (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.BATTERY)
b_soc_high: 100 % (category: FieldCategory.CONFIG) (state_class: n/a) (device_class: n/a)
b_soc_low: 50 % (category: FieldCategory.CONFIG) (state_class: n/a) (device_class: n/a)
b_soc_total: 0 % (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.BATTERY)
b_soh: 99 % (category: FieldCategory.DIAGNOSTIC) (state_class: FieldStateClass.MEASUREMENT) (device_class: n/a)
b_soh_total: 0 % (category: FieldCategory.DIAGNOSTIC) (state_class: FieldStateClass.MEASUREMENT) (device_class: n/a)
b_t_avg: 0 °C (category: FieldCategory.DIAGNOSTIC) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.TEMPERATURE)
b_type: Balco260   (category: n/a) (state_class: n/a) (device_class: n/a)
b_v: 26.1 V (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.VOLTAGE)
b_v_total: 26.1 V (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.VOLTAGE)
d_inverter_fault: InverterFault.NoFault   (category: FieldCategory.DIAGNOSTIC) (state_class: n/a) (device_class: n/a)
d_inverter_status: InverterStatus.GridConnectedDischarging   (category: FieldCategory.DIAGNOSTIC) (state_class: n/a) (device_class: n/a)
d_inverter_total: 432 W (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.POWER)
d_inverter_type: Balco260   (category: FieldCategory.DIAGNOSTIC) (state_class: n/a) (device_class: n/a)
d_inverter_warning: InverterWarning.NoWarning   (category: FieldCategory.DIAGNOSTIC) (state_class: n/a) (device_class: n/a)
d_num_battery_packs: 0   (category: FieldCategory.DIAGNOSTIC) (state_class: n/a) (device_class: n/a)
d_num_inverters: 1   (category: FieldCategory.DIAGNOSTIC) (state_class: n/a) (device_class: n/a)
g_i_e_total: 258.4 kWh (category: n/a) (state_class: FieldStateClass.TOTAL_INCREASING) (device_class: DeviceClass.ENERGY)
g_i_f: 50.0 Hz (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.FREQUENCY)
g_i_p_total: 0 W (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.POWER)
g_i_switch: 1   (category: FieldCategory.CONFIG) (state_class: n/a) (device_class: n/a)
g_o_e_total: 29.5 kWh (category: n/a) (state_class: FieldStateClass.TOTAL_INCREASING) (device_class: DeviceClass.ENERGY)
g_o_switch: 1   (category: FieldCategory.CONFIG) (state_class: n/a) (device_class: n/a)
pv_1_i_c: 0.0 A (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.CURRENT)
pv_1_i_p: 0 W (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.POWER)
pv_1_i_v: 0.0 V (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.VOLTAGE)
pv_2_i_c: 0.0 A (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.CURRENT)
pv_2_i_p: 0 W (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.POWER)
pv_2_i_v: 0.0 V (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.VOLTAGE)
pv_3_i_c: 0.0 A (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.CURRENT)
pv_3_i_p: 0 W (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.POWER)
pv_3_i_v: 42.9 V (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.VOLTAGE)
pv_4_i_c: 0.0 A (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.CURRENT)
pv_4_i_p: 0 W (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.POWER)
pv_4_i_v: 43.3 V (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.VOLTAGE)
pv_ac_e: 8.6 kWh (category: n/a) (state_class: FieldStateClass.TOTAL_INCREASING) (device_class: DeviceClass.ENERGY)
pv_ac_p: 0 W (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.POWER)
pv_i_e_total: 77.4 kWh (category: n/a) (state_class: FieldStateClass.TOTAL_INCREASING) (device_class: DeviceClass.ENERGY)
pv_i_p_total: 0 W (category: n/a) (state_class: FieldStateClass.MEASUREMENT) (device_class: DeviceClass.POWER)
```


### Read device data for supported devices

```bash
usage: bluetti-modwrite [-h] [-c HOST] [-p PORT] [-t TYPE] [-f FIELD] [-v VALUE]

Write to bluetti device field via modbus

options:
  -h, --help         show this help message and exit
  -c, --host HOST    IP-address of the device
  -p, --port PORT    Port of the device
  -t, --type TYPE    Device type
  -f, --field FIELD  Field name
  -v, --value VALUE  Value to write
```

Example:

This turns on the AC outlet on the Balco260

```bash
bluetti-modwrite -c 10.2.1.60 -p 502 -t balco260 -f ac_o_switch -v 1
```

Example output:

```bash
Wrote to device field ac_o_switch value 1
```
