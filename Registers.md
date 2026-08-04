# Modbus Registers

## Naming convention for return values

1. Type (PV/AC/Grid/Device/Battery) (short: pv/ac/g/d/b)

2. Phase/String/Battery number if available

3. in/out (short: i/o) or destination

4. power/voltage/current/energy/frequency (short: p/v/c/e/f)

5. **total** (if total over all phases/strings)


## Balco260

|Register   |Return value name      |Description                        |
|-----------|-----------------------|-----------------------------------|
|50001      |d_num_inverters        |Number of inverters                |
|50002      |ac_o_p_total           |AC output power                    |
|50004      |pv_i_p_total           |PV input power                     |
|50006      |g_i_p_total            |Power from grid                    |
|50008      |TBD                    |TBD                                |
|50010      |pv_ac_p                |AC consumption direct from PV      |
|50012      |ac_o_e_total           |AC output energy (kWh)             |
|50014      |pv_i_e_total           |PV input energy (kWh)              |
|50016      |g_i_e_total            |Energy (kWh) from grid             |
|50018      |g_o_e_total            |Energy (kWh) to grid               |
|50020      |pv_ac_e                |Energy (kWh) PV direct to AC       |
|50022      |d_status_inverter      |Inverter operating status          |
|50023      |d_warning_inverter     |Inverter warnings                  |
|50027      |d_fault_inverter       |Inverter faults                    |
|50200      |d_type_inverter        |Inverter type                      |
|50206      |d_sn_inverter          |Inverter serial number             |
|50210      |d_mcu1_version         |MCU 1 firmware version             |
|50212      |d_mcu2_version         |MCU 2 firmware version             |
|50214      |g_i_f                  |Grid freqency                      |

TBD


### Enums

TBD
