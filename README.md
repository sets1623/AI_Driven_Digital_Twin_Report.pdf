# AI-Driven Digital Twin (Level-1)

### Multi-Physics System Modeling, Estimation, and Health Monitoring

---

## Project Overview

This project implements a **Level-1 Digital Twin framework** for an **ISS-inspired space system**, focusing on **system-level modeling, estimation, control logic, and health monitoring**.

The Digital Twin combines:

* Electrical (battery) dynamics
* Thermal dynamics
* Life support (ECLSS-inspired) dynamics
* State estimation and fault detection
* Health degradation and Remaining Useful Life (RUL) estimation

The objective is to **study how Digital Twin architectures can be built for complex engineering systems**, with emphasis on **clarity, correctness, and scalability**, rather than high-fidelity mission replication.

---

## What This Project Does (Clearly Stated)

This project creates a **closed-loop simulation environment** that:

1. Models **nonlinear multi-physics system dynamics**
2. Estimates internal system states using an **Extended Kalman Filter (EKF)**
3. Applies **optimization-based control logic** (mini-MPC style)
4. Detects abnormal behavior using **statistical fault detection (NIS)**
5. Predicts **battery health degradation and Remaining Useful Life (RUL)**

All components are implemented in a **modular and extensible architecture**.

---

## System Architecture (Level-1)

### State Vector (8 States)

The system is represented using a unified nonlinear state vector:

* SOC – Battery state of charge
* V_bus – Electrical bus voltage (simplified)
* T_core – Internal system temperature
* T_radiator – Radiator temperature
* O2_mass – Cabin oxygen mass
* CO2_mass – Cabin CO₂ mass
* P_cabin – Cabin pressure
* H_battery – Battery health index

This structure enables **future expansion** while remaining computationally simple.

---

## Subsystem Modeling

### 1. Electrical (Battery) System

* Nonlinear SOC dynamics
* Charging and discharging efficiency
* Solar input disturbance (orbital sunlight)
* Load variation
* Health degradation linked to SOC stress

### 2. Thermal System

* Heat generation from electrical load
* Radiative heat rejection
* Pump-controlled heat transfer
* Core and radiator temperature dynamics

### 3. Life Support System (Simplified ECLSS)

* Oxygen generation and consumption
* CO₂ generation and scrubbing
* Cabin pressure variation
* Crew metabolic load as disturbance

---

## Estimation and Monitoring

### Extended Kalman Filter (EKF)

* Estimates SOC and battery health
* Handles nonlinear system behavior
* Includes process and measurement noise modeling

### Fault Detection

* Uses **Normalized Innovation Squared (NIS)**
* Detects degradation faults after fault injection
* Evaluates filter consistency statistically

### Health & Prognostics

* Continuous battery health degradation modeling
* Smoothed Remaining Useful Life (RUL) estimation
* Suitable for predictive maintenance studies

---

## Control Logic

* Optimization-based control using **grid search**
* Minimizes:

  * SOC deviation
  * Health degradation rate
  * Control effort
* Enforces safety constraints on SOC and health

This represents a **simplified Model Predictive Control (MPC) concept**.

---

## Numerical Integration

* System dynamics are propagated using a **Runge–Kutta 4th Order (RK4) solver**
* Ensures numerical stability and accuracy
* Clean separation between:

  * State definition
  * System dynamics
  * Integration logic

---

## Project Structure

```text
AI_Digital_Twin/
│
├── main_simulation.py          # Full closed-loop simulation
│
├── state_vector.py             # 8-state system definition
├── system_dynamics.py          # Nonlinear multi-physics model
├── rk4_solver.py               # RK4 numerical integrator
│
├── System_Architecture_Level1.md
│
├── requirements.txt
└── README.md
```

Compiled files (`*.cpython-313`) are generated artifacts and not part of core logic.

---

## Tools and Technologies

* Python
* NumPy, SciPy
* Matplotlib (visualization)
* Control systems & estimation theory

The focus is on **engineering modeling and reasoning**, not software complexity.

---

## What This Project Is

✔ A research-oriented Digital Twin framework
✔ A system-level engineering study
✔ A learning platform for estimation, control, and health monitoring
✔ Suitable for:

* Final-year projects
* Research internships
* Control systems & Digital Twin portfolios

---

## What This Project Is NOT

✘ Not a real ISS model
✘ Not connected to live space data
✘ Not a mission-certified flight system
✘ Not a black-box AI project

---

## Key Learning Outcomes

* Multi-physics system modeling
* State-space formulation
* EKF implementation
* Fault detection using statistical methods
* Health degradation & RUL estimation
* Digital Twin architecture design

---

## Future Scope

* Higher-fidelity physical models
* Coupled estimation across all states
* Advanced MPC formulations
* Integration with real open telemetry datasets
* Extension to lunar or Mars habitat systems

---

## Author

**Tamil Selvan**
Electrical & Electronics Engineering
Interests:
Digital Twins • Control Systems • Estimation • Space Systems

---

## License

MIT License – Free for educational and research use.

---

### Final Note for Reviewers

> This project emphasizes **clarity, correctness, and engineering discipline** in Digital Twin development, serving as a solid foundation for advanced research and system expansion.

---

