import numpy as np
from .utilities import Orbit
from .plotting import Plotter
from .bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune

# Plotting a Planet
# Earth_Plot = Plotter(Earth)
# Earth_Plot.Plot()

# Plotting an Orbit with Orbital State Vectors, Position(r) & Velocity(v)
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
Earth_LEO = Orbit(Earth, r_vec, v_vec, time_span, dt)
Earth_LEO_ = Earth_LEO.Propagate_Orbit()

Earth_Plot.Plot(Earth_LEO_)
