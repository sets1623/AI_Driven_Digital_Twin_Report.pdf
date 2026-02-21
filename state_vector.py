"""
State Vector Definition
AI-Driven Digital Twin – Level 1
"""

import numpy as np


class StateVector:
    def __init__(self):
        # Electrical States
        self.SOC = 0.8              # Battery state of charge (0–1)
        self.V_bus = 120.0          # Bus voltage (V)

        # Thermal States
        self.T_core = 295.0         # Core temperature (K)
        self.T_radiator = 280.0     # Radiator temperature (K)

        # Life Support States
        self.O2_mass = 100.0        # Oxygen mass (kg)
        self.CO2_mass = 5.0         # CO2 mass (kg)
        self.P_cabin = 101325.0     # Cabin pressure (Pa)

        # Health State
        self.H_battery = 1.0        # Battery health index

    def to_array(self):
        return np.array([
            self.SOC,
            self.V_bus,
            self.T_core,
            self.T_radiator,
            self.O2_mass,
            self.CO2_mass,
            self.P_cabin,
            self.H_battery
        ])

    def update_from_array(self, arr):
        (
            self.SOC,
            self.V_bus,
            self.T_core,
            self.T_radiator,
            self.O2_mass,
            self.CO2_mass,
            self.P_cabin,
            self.H_battery
        ) = arr