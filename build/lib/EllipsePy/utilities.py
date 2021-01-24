import math
import numpy as np
from scipy.integrate import ode
import plotly.graph_objects as go


# Planetary Body Initializer
def spheres(radius, clr, clr_gradient=None, dist=0):
    # Set up 100 points. First, do angles
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)

    # Set up coordinates for points on the sphere
    x_ = dist + radius * np.outer(np.cos(theta), np.sin(phi))
    y_ = radius * np.outer(np.sin(theta), np.sin(phi))
    z_ = radius * np.outer(np.ones(100), np.cos(phi))

    # Set up trace
    if clr_gradient == None:
        clr_gradient = clr
    else:
        pass

    trace = go.Surface(x=x_, y=y_, z=z_, colorscale=[
                       [0, clr], [1, clr_gradient]])
    trace.update(showscale=False)

    return trace


# Orbit Initializer
class Orbit:
    def __init__(self, body, r_vec, v_vec, time_span, dt):
        self.body = body
        self.r_vec = r_vec
        self.v_vec = v_vec
        self.time_span = time_span
        self.dt = dt

    def diffrential_q(self, t, y, mu):
        # Unpack State R-Position Vector V-Velocity Vector, Inputs(Position & Velocity)
        rx, ry, rz, vx, vy, vz = y
        r = np.array([rx, ry, rz])

        # Norm of Radius Vector
        norm_r = np.linalg.norm(r)

        # Two Body Acceleration
        ax, ay, az = -r * self.body['Mu']/norm_r**3

        # Outputs-The Derivatives of Input, Outputs(Velocity, Acceleration)
        return [vx, vy, vz, ax, ay, az]

    def Propagate_Orbit(self):
        n_steps = int(np.ceil(self.time_span/self.dt))  # Total number of steps

        # Initializing arrays - Preallocating Memory
        ys = np.zeros((n_steps, 6))
        ts = np.zeros((n_steps, 1))

        # Initial Conditions
        y0 = self.r_vec + self.v_vec
        ys[0] = np.array(y0)
        step = 1

        # Initializing Solver
        solver = ode(self.diffrential_q)
        solver.set_integrator('lsoda')
        solver.set_initial_value(y0, 0)
        solver.set_f_params(self.body['Mu'])

        # Propagate Orbit
        while solver.successful() and step < n_steps:
            solver.integrate(solver.t + self.dt)
            ts[step] = solver.t
            ys[step] = solver.y
            step += 1

        rs = ys[:, :3]
        # vs = ys[:, 3:]

        print(rs)

        # Parsing
        rxs = []
        rys = []
        rzs = []
        for r in rs:
            rxs.append(r[0])
            rys.append(r[1])
            rzs.append(r[2])

        return [rxs, rys, rzs]
