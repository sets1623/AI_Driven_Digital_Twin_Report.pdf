"""
System Dynamics
AI-Driven Digital Twin – Level 1
"""

import numpy as np


def system_dynamics(t, X, U, D):
    """
    Computes dX/dt = f(X, U, D)

    X: state vector array
    U: control inputs
    D: disturbances
    """

    # ----------------------------
    # Unpack state
    # ----------------------------
    SOC, V_bus, T_core, T_radiator, O2_mass, CO2_mass, P_cabin, H_battery = X

    # ----------------------------
    # Unpack controls
    # ----------------------------
    P_solar_util, Pump_speed, O2_gen_rate, CO2_scrub_rate = U

    # ----------------------------
    # Unpack disturbances
    # ----------------------------
    Sunlight, Crew_load, External_temp = D

    # ==========================================================
    # 1️⃣ BATTERY DYNAMICS (REALISTIC UPGRADE)
    # ==========================================================

    P_solar = Sunlight * P_solar_util
    P_load = Crew_load * 2.0

    # Battery physical parameters
    C_battery = 50000.0      # Effective energy capacity
    charge_eff = 0.95
    discharge_eff = 0.90

    net_power = P_solar - P_load

    if net_power >= 0:
        dSOC_dt = charge_eff * net_power / C_battery
    else:
        dSOC_dt = net_power / (discharge_eff * C_battery)

    # ==========================================================
    # 2️⃣ THERMAL DYNAMICS
    # ==========================================================

    sigma = 5.67e-8
    epsilon = 0.85
    A = 10.0
    C_th = 500.0

    Q_rad = sigma * epsilon * A * (T_radiator**4 - External_temp**4)

    dT_core_dt = (P_load - Q_rad) / C_th
    dT_radiator_dt = (Pump_speed * (T_core - T_radiator) - Q_rad) / C_th

    # ==========================================================
    # 3️⃣ LIFE SUPPORT DYNAMICS
    # ==========================================================

    dO2_dt = O2_gen_rate - 0.1 * Crew_load
    dCO2_dt = 0.1 * Crew_load - CO2_scrub_rate

    dP_cabin_dt = 0.01 * (dO2_dt - dCO2_dt)

    # ==========================================================
    # 4️⃣ BATTERY HEALTH DEGRADATION
    # ==========================================================

    dH_battery_dt = -0.00001 * abs(dSOC_dt)

    # ==========================================================
    # Return State Derivative
    # ==========================================================

    return np.array([
        dSOC_dt,
        0.0,  # V_bus simplified constant for now
        dT_core_dt,
        dT_radiator_dt,
        dO2_dt,
        dCO2_dt,
        dP_cabin_dt,
        dH_battery_dt
    ])