import numpy as np
from .utilities import Orbit
from .plotting import Plotter
from .bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

'''# Planet
Earth_Plot = Plotter(Earth)
Earth_Plot.Plot()'''

'''
================================================================================================================================================================================
'''

'''# Orbit with Orbital State Vectors
h = 1500  # km - Spacecraft's Distance from the center of Earth
# Magnitude of Position Vector (Earth's Radius + Spacecraft's Height)
r_mag = Earth['Radius'] + h
# Magniitude of Velocity Vector (Tangential Velocity / Speed of a Satellite in Circular Orbit)
v_mag = np.sqrt(Earth['Mu'] / r_mag)

# Position Vector ((r_mag)i + (0)j + (0)k)
r_vec = [r_mag, r_mag*0.1, r_mag*-0.1]
# Velocity Vector ((0)i + (v_mag)j + (0)k
v_vec = [0, v_mag, v_mag*0.3]

time_span = 3600*24.0  # Timespan, 1 day
dt = 100  # Timestep, 100 seconds

Earth_Plot = Plotter(Earth)
Earth_LEO = Orbit(Earth, [r_vec, v_vec], time_span, dt)

Earth_LEO_ = Earth_LEO.Propagate_Orbit()

Orbits = [Earth_LEO_]

Sat_Names = ['LEO']

Earth_Plot.Plot(Orbits, Sat_Names)'''

'''
================================================================================================================================================================================
'''

'''# Multiple Orbits with Orbital State Vectors
h_1 = 400
r_mag_1 = Earth['Radius'] + h_1
v_mag_1 = np.sqrt(Earth['Mu'] / r_mag_1)

r_vec_1 = [r_mag_1, 0, 0]
v_vec_1 = [0, v_mag_1, 0]

h_2 = 38000
r_mag_2 = Earth['Radius'] + h_2
v_mag_2 = np.sqrt(Earth['Mu'] / r_mag_2)

r_vec_2 = [r_mag_2, 0, 0]
v_vec_2 = [0, v_mag_2, 0]

time_span = (3600*24.0) * 2
dt = 100

Earth_Plot = Plotter(Earth)

Earth_LEO = Orbit(Earth, [r_vec_1, v_vec_1], time_span, dt)
Earth_LEO_ = Earth_LEO.Propagate_Orbit()

Earth_GEO = Orbit(Earth, [r_vec_2, v_vec_2], time_span, dt)
Earth_GEO_ = Earth_GEO.Propagate_Orbit()

Orbits = [Earth_LEO_, Earth_GEO_]

Sat_Names = ['LEO', 'GEO']

Earth_Plot.Plot(Orbits, Sat_Names)'''

'''
================================================================================================================================================================================
'''

'''# Orbit with Keplerian Elements
A = Earth['Radius'] + 414.0  # Semi-Minor Axis, (Apogee + Perigee) / 2
E = 0.000169  # Eccentricity
I = 51.6393  # Inclination
T = 0.0  # True Anomaly
P = 234.1955  # Argument of Periapsis
R = 105.6372  # Right Ascention of Ascending Node

time_span = 3600*24.0
dt = 100

Earth_Plot = Plotter(Earth)

Earth_LEO = Orbit(Earth, [A, E, I, T, P, R], time_span, dt)
Earth_LEO_ = Earth_LEO.Propagate_Orbit()

Orbits = [Earth_LEO_]

Sat_Names = ['LEO']

Earth_Plot.Plot(Orbits, Sat_Names)'''

'''
================================================================================================================================================================================
'''

'''# Multiple Orbits with both State Vectors and Keplerian Elements
A = Earth['Radius'] + 414.0
E = 0.000169
I = 51.6393
T = 0.0
P = 234.1955
R = 105.6372

h = 1000
r_mag = Earth['Radius'] + h
v_mag = np.sqrt(Earth['Mu'] / r_mag)
r_vec = [r_mag, 0, 0]
v_vec = [0, v_mag, 0]

A_ = Earth['Radius'] + 35800.0
E_ = 0.0
I_ = 0.0
T_ = 0.0
P_ = 0.0
R_ = 0.0

time_span = 3600*24.0
dt = 100

Earth_Plot = Plotter(Earth)

Earth_ISS = Orbit(Earth, [A, E, I, T, P, R], time_span, dt)
Earth_ISS_ = Earth_ISS.Propagate_Orbit()

Earth_LEO = Orbit(Earth, [r_vec, v_vec], time_span, dt)
Earth_LEO_ = Earth_LEO.Propagate_Orbit()

Earth_GEO = Orbit(Earth, [A_, E_, I_, T_, P_, R_], time_span, dt)
Earth_GEO_ = Earth_GEO.Propagate_Orbit()

Orbits = [Earth_ISS_, Earth_LEO_, Earth_GEO_]

Sat_Names = ["ISS", "LEO", "GEO"]

Earth_Plot.Plot(Orbits, Sat_Names)'''

'''
================================================================================================================================================================================
'''

'''# Orbit with TLES
time_span = 3600*24.0
dt = 10

Earth_Plot = Plotter(Earth)

Starlink_TLE = Orbit(Earth, 'starlink_tles.txt', time_span, dt, TLES=True)
Starlink_TLE_ = Starlink_TLE.Propagate_Orbit(TLES=True)

Sat_names = Starlink_TLE.Names()

Earth_Plot.Plot(Starlink_TLE_, Sat_names)'''

'''
================================================================================================================================================================================
'''

'''# Multiple Orbits with TLEs
time_span = 3600*24.0
dt = 10

Earth_Plot = Plotter(Earth)

# https://celestrak.com/NORAD/elements/supplemental/starlink.txt
Starlink_TLE = Orbit(Earth, 'starlink_tles.txt', time_span, dt, TLES=True)
Starlink_TLE_ = Starlink_TLE.Propagate_Orbit(TLES=True)

print("{} Satellites".format(len(Starlink_TLE_)))

Sat_Names = Starlink_TLE.Names()

Colors = ["navy", "#1e43ff", "dodgerblue"]

Earth_Plot.Plot(Starlink_TLE_, Sat_Names, Colors)'''

'''
================================================================================================================================================================================
'''

'''# Multiple Orbits with State Vectors, Keplerian Elements, and TLES
A = Earth['Radius'] + 414.0
E = 0.000169
I = 51.6393
T = 0.0
P = 234.1955
R = 105.6372

h = 1000
r_mag = Earth['Radius'] + h
v_mag = np.sqrt(Earth['Mu'] / r_mag)
r_vec = [r_mag, 0, 0]
v_vec = [0, v_mag, 0]

time_span = 3600*24.0
dt = 100

Earth_Plot = Plotter(Earth)

Earth_ISS = Orbit(Earth, [A, E, I, T, P, R], time_span, dt)
Earth_ISS_ = Earth_ISS.Propagate_Orbit()

Earth_LEO = Orbit(Earth, [r_vec, v_vec], time_span, dt)
Earth_LEO_ = Earth_LEO.Propagate_Orbit()

Starlink_TLE = Orbit(Earth, 'starlink_tles.txt', time_span, dt, TLES=True)
Starlink_TLE_ = Starlink_TLE.Propagate_Orbit(TLES=True)

Orbits = [Earth_ISS_, Earth_LEO_]

for Orbit in Starlink_TLE_:
    Orbits.append(Orbit)

Sat_Names = ["ISS", "LEO"]

for Sat_Name in Starlink_TLE.Names():
    Sat_Names.append(Sat_Name)

Earth_Plot.Plot(Orbits, Sat_Names)'''

'''
================================================================================================================================================================================
'''

'''# Interesting Visualization
time_span = 3600 * 24.0
dt = 10

Earth_Plot = Plotter(Earth)

tles = Orbit(Earth, 'tles.txt', time_span, dt, TLES=True)
tles_ = tles.Propagate_Orbit(TLES=True)

print("{} Sats".format(len(tles_)))

Sat_names = tles.Names()

Colors = ["black", "dodgerblue"]

Earth_Plot.Plot(tles_, Sat_names)'''

'''
================================================================================================================================================================================
'''

'''# Starlink Constellation
time_span = 3600*24.0
dt = 10

Earth_Plot = Plotter(Earth)

# https://www.celestrak.com/NORAD/elements/swarm.txt
Testing_TLE = Orbit(Earth, 'testing.txt', time_span, dt, TLES=True)
Testing_TLE_ = Testing_TLE.Propagate_Orbit(TLES=True)

print("{} Sats".format(len(Testing_TLE_)))

Sat_Names = Testing_TLE.Names()

Colors = ["navy", "#1e43ff", 'dodgerblue']

Earth_Plot.Plot(Testing_TLE_, Sat_Names, Colors)'''
