import math
import numpy as np
from scipy.integrate import ode
import plotly.graph_objects as go


# Planetary Body Initializer
def spheres(radius, clr, clr_gradient=None, dist=0):
    # Set up 100 points. First, do angles
    theta = np.linspace(0, 2*np.pi, 100)
    phi = np.linspace(0, np.pi, 100)

    # Set up coordinates for points on the sphere
    x0 = dist + radius * np.outer(np.cos(theta), np.sin(phi))
    y0 = radius * np.outer(np.sin(theta), np.sin(phi))
    z0 = radius * np.outer(np.ones(100), np.cos(phi))

    # Set up trace
    if clr_gradient == None:
        clr_gradient = clr
    else:
        pass

    trace = go.Surface(x=x0, y=y0, z=z0, colorscale=[
        [0, clr], [1, clr_gradient]])
    trace.update(showscale=False)

    return trace


# Orbit Initializer
class Orbits:
    def diffrential_eq(self, t, y, mu):
        # Unpack State R-Position Vector V-Velocity Vector, Inputs(Position & Velocity)
        rx, ry, rz, vx, vy, vz = y
        r = np.array([rx, ry, rz])

        # Norm of Radius Vector
        norm_r = np.linalg.norm(r)

        # Two Body Acceleration
        ax, ay, az = -r * mu/norm_r**3

        # Outputs-The Derivatives of Input, Outputs(Velocity, Acceleration)
        return [vx, vy, vz, ax, ay, az]
