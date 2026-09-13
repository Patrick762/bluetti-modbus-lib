from enum import Enum, unique


@unique
class ControlMode(Enum):
    AppControl = 0
    SCM = 11
    Standby = 12
    ForceCharge = 13
    ForceDischarge = 14
