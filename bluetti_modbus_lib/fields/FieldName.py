"""
Naming convention for return values:

1. Type (PV/AC/Grid/Device/Battery) (short: pv/ac/g/d/b)
2. Phase/String/Battery number if available
3. in/out (short: i/o) or destination
4. power/voltage/current/energy/frequency (short: p/v/c/e/f)
5. **total** (if total over all phases/strings)
"""

from enum import Enum, unique


@unique
class FieldName(Enum):
    D_NUM_INVERTERS = "d_num_inverters"
    AC_O_P_TOTAL = "ac_o_p_total"
    PV_I_P_TOTAL = "pv_i_p_total"
    G_I_P_TOTAL = "g_i_p_total"
    PV_AC_P = "pv_ac_p"
    AC_O_E_TOTAL = "ac_o_e_total"
    PV_I_E_TOTAL = "pv_i_e_total"
    G_I_E_TOTAL = "g_i_e_total"
    G_O_E_TOTAL = "g_o_e_total"
    PV_AC_E = "pv_ac_e"
    G_I_F = "g_i_f"
    PV_1_I_P = "pv_1_i_p"
    PV_1_I_V = "pv_1_i_v"
    PV_1_I_C = "pv_1_i_c"
    PV_2_I_P = "pv_2_i_p"
    PV_2_I_V = "pv_2_i_v"
    PV_2_I_C = "pv_2_i_c"
    PV_3_I_P = "pv_3_i_p"
    PV_3_I_V = "pv_3_i_v"
    PV_3_I_C = "pv_3_i_c"
    PV_4_I_P = "pv_4_i_p"
    PV_4_I_V = "pv_4_i_v"
    PV_4_I_C = "pv_4_i_c"
    D_NUM_PACKS = "d_num_packs"
    B_V_TOTAL = "b_v_total"
    B_C_TOTAL = "b_c_total"
    B_SOC_TOTAL = "b_soc_total"
    B_SOH_TOTAL = "b_soh_total"
