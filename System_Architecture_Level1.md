--------------------------------------------

FORMAL LEVEL 1 STATE VECTOR DEFINITION

--------------------------------------------



We define the complete nonlinear system state as:



X = \[

&nbsp;   SOC,              # Battery state of charge (0–1)

&nbsp;   V\_bus,            # Electrical bus voltage (Volts)

&nbsp;   T\_core,           # Internal module temperature (Kelvin)

&nbsp;   T\_radiator,       # Radiator surface temperature (Kelvin)

&nbsp;   O2\_mass,          # Oxygen mass inside cabin (kg)

&nbsp;   CO2\_mass,         # CO2 mass inside cabin (kg)

&nbsp;   P\_cabin,          # Cabin pressure (Pascal)

&nbsp;   H\_battery         # Battery health index (0–1 degradation metric)

]



Total state dimension: n = 8



--------------------------------------------

CONTROL INPUT VECTOR



U = \[

&nbsp;   P\_solar\_util,     # Solar power utilization factor

&nbsp;   Pump\_speed,       # Thermal coolant pump control

&nbsp;   O2\_gen\_rate,      # Oxygen generation rate

&nbsp;   CO2\_scrub\_rate    # CO2 scrubbing rate

]



--------------------------------------------

DISTURBANCE VECTOR



D = \[

&nbsp;   Sunlight(t),          # Orbital sunlight/eclipse cycle

&nbsp;   Crew\_metabolic\_load,  # Heat + CO2 generation from crew

&nbsp;   External\_temp         # Space temperature boundary condition

]



--------------------------------------------

MASTER NONLINEAR SYSTEM EQUATION



dX/dt = f(X, U, D, θ)



Where:

X = State vector

U = Control inputs

D = Disturbances

θ = Physical system parameters

