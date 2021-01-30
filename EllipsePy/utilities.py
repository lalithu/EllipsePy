import math as m
import numpy as np
from scipy.integrate import ode
import plotly.graph_objects as go
import datetime


# Planetary Body & Orbit Initializer
class Orbit:
    def __init__(self, body, state, time_span, dt, TLES=False):

        if len(state) == 2:
            self.body = body
            self.r_vec = state[0]
            self.v_vec = state[1]
            self.time_span = time_span
            self.dt = dt

        elif TLES:
            self.filename = state

            with open(self.filename, 'r') as t:
                lines = t.readlines()

            line_Id = 0
            tle = []
            self.tles = []

            for line in lines:
                line_Id += 1
                tle.append(line)
                if line_Id == 3:
                    self.tles.append(tle)
                    tle = []
                    line_Id = 0
                else:
                    pass

            self.body = body
            self.filename = state
            self.time_span = time_span
            self.dt = dt

            self.r_vecs = []
            self.v_vecs = []

            self.tle_sat_names = []

            for tle_ in self.tles:
                TLE_into_COES = self.TLE_coes(tle_)

                TLECOES_into_rv = self.COES_rv(TLE_into_COES[0], TLE=True)

                tle_r_vec_ = []
                tle_v_vec_ = []

                TLE_r_vec = TLECOES_into_rv[0]
                TLE_v_vec = TLECOES_into_rv[1]

                for n in TLE_r_vec:
                    tle_r_vec_.append(n)

                for n in TLE_v_vec:
                    tle_v_vec_.append(n)

                self.r_vecs.append(tle_r_vec_)
                self.v_vecs.append(tle_v_vec_)

                self.tle_sat_names.append(TLE_into_COES[1])

            tle_v_vec_Id = 0
            self.tle_rv_vecs = []

            for tle_r_vec in self.r_vecs:
                self.tle_rv_vecs.append([tle_r_vec, self.v_vecs[tle_v_vec_Id]])
                tle_v_vec_Id += 1

        else:
            self.body = body
            self.time_span = time_span
            self.dt = dt

            COES_ = self.COES_rv(state)

            COES_r_vec = COES_[0]
            COES_v_vec = COES_[1]

            self.r_vec = []
            self.v_vec = []

            for n in COES_r_vec:
                self.r_vec.append(n)

            for n in COES_v_vec:
                self.v_vec.append(n)

    def diffrential_q(self, t, y, mu):
        rx, ry, rz, vx, vy, vz = y
        r = np.array([rx, ry, rz])

        norm_r = np.linalg.norm(r)

        ax, ay, az = -r * self.body['Mu']/norm_r**3

        return [vx, vy, vz, ax, ay, az]

    def Propagate_Orbit(self, TLES=False):
        if TLES:

            self.tle_orbits = []

            for tle_rv_vec in self.tle_rv_vecs:

                self.r_vec = tle_rv_vec[0]
                self.v_vec = tle_rv_vec[1]

                n_steps = int(np.ceil(self.time_span/self.dt))

                ys = np.zeros((n_steps, 6))
                ts = np.zeros((n_steps, 1))

                y0 = self.r_vec + self.v_vec
                ys[0] = np.array(y0)
                step = 1

                solver = ode(self.diffrential_q)
                solver.set_integrator('lsoda')
                solver.set_initial_value(y0, 0)
                solver.set_f_params(self.body['Mu'])

                while solver.successful() and step < n_steps:
                    solver.integrate(solver.t + self.dt)
                    ts[step] = solver.t
                    ys[step] = solver.y
                    step += 1

                rs = ys[:, :3]
                vs = ys[:, 3:]

                print(rs)

                rxs = []
                rys = []
                rzs = []
                for r in rs:
                    rxs.append(r[0])
                    rys.append(r[1])
                    rzs.append(r[2])

                self.tle_orbits.append([rxs, rys, rzs])

            return self.tle_orbits

        else:
            n_steps = int(np.ceil(self.time_span/self.dt))

            ys = np.zeros((n_steps, 6))
            ts = np.zeros((n_steps, 1))

            y0 = self.r_vec + self.v_vec
            ys[0] = np.array(y0)
            step = 1

            solver = ode(self.diffrential_q)
            solver.set_integrator('lsoda')
            solver.set_initial_value(y0, 0)
            solver.set_f_params(self.body['Mu'])

            while solver.successful() and step < n_steps:
                solver.integrate(solver.t + self.dt)
                ts[step] = solver.t
                ys[step] = solver.y
                step += 1

            rs = ys[:, :3]
            vs = ys[:, 3:]

            print(rs)

            rxs = []
            rys = []
            rzs = []
            for r in rs:
                rxs.append(r[0])
                rys.append(r[1])
                rzs.append(r[2])
            return [rxs, rys, rzs]

    def COES_rv(self, COES, deg=False, TLE=False):
        if deg:
            self.A, self.Ecc, self.I, self.T, self.P, self.R = COES
            self.I = self.I * (np.pi / 180)
            self.T = self.T * (np.pi / 180)
            self.P = self.P * (np.pi / 180)
            self.R = self.R * (np.pi / 180)
        else:
            self.A, self.Ecc, self.I, self.T, self.P, self.R = COES

        self.E = self.ecc_anomaly([self.T, self.Ecc], 'T&E')

        norm_r = self.A * (1 - self.Ecc ** 2) / (1 + self.Ecc * np.cos(self.T))

        r_perif = norm_r * np.array([m.cos(self.T), m.sin(self.T), 0])
        v_perif = m.sqrt(self.body['Mu'] * self.A) / norm_r * \
            np.array([-m.sin(self.E), m.cos(self.E)
                      * m.sqrt(1 - self.Ecc ** 2), 0])

        perif_eci = np.transpose(self.eci_perif(self.R, self.P, self.I))

        COES_r_vec = np.dot(perif_eci, r_perif)
        COES_v_vec = np.dot(perif_eci, v_perif)

        return [COES_r_vec, COES_v_vec]

    def eci_perif(self, R, P, I):
        row0 = [-m.sin(R) * m.cos(I) * m.sin(P) + m.cos(R) * m.cos(P), m.cos(R)
                * m.cos(I) * m.sin(P) + m.sin(R) * m.cos(P), m.sin(I) * m.sin(P)]
        row1 = [-m.sin(R) * m.cos(I) * m.cos(P) - m.cos(R) * m.sin(P), m.cos(R)
                * m.cos(I) * m.cos(P) - m.sin(R) * m.sin(P), m.sin(I) * m.cos(P)]
        row2 = [m.sin(R) * m.sin(I), -m.cos(R) * m.sin(I), m.cos(I)]
        return np.array([row0, row1, row2])

    def ecc_anomaly(self, vars_, method, tol=1e-8):
        if method == 'Newton':
            M, E = vars_
            if M < np.pi / 2.0:
                E0 = M + E / 2.0
            else:
                E0 = M - E
            for n in range(200):
                ratio = (E0 - E * np.sin(E0) - M) / (1 - E * np.cos(E0))
                if abs(ratio) < tol:
                    if n == 0:
                        return E0
                    else:
                        return E1
                else:
                    E1 = E0 - ratio
                    E0 = E1
            return False

        elif method == 'T&E':
            T, E = vars_
            return 2 * m.atan(m.sqrt((1-E) / (1+E)) * m.tan(T/2.0))

    def TLE_coes(self, tle):
        tle_sat = tle[0].strip()
        line1 = tle[1].strip().split()
        line2 = tle[2].strip().split()

        Epoch = line1[3]
        yy, mm, dd, h = self.calc_Epoch(Epoch)

        I = float(line2[2]) * (np.pi / 180)
        R = float(line2[3]) * (np.pi / 180)
        E_ = line2[4]
        Ecc = float('0.' + E_)
        P = float(line2[5]) * (np.pi / 180)
        M = float(line2[6]) * (np.pi / 180)
        M_motion = float(line2[7])
        T_P = 1 / M_motion * 24 * 3600
        A = (T_P ** 2 * self.body['Mu'] / 4.0 /
             np.pi ** 2) ** (1.0 / 3.0)

        self.E_A = self.ecc_anomaly(
            [M, Ecc], 'Newton')

        T = self.true_anomaly([self.E_A, Ecc])

        r_mag = A * (1 - Ecc * np.cos(self.E_A))

        return [A, Ecc, I, T, P, R], tle_sat

    def calc_Epoch(self, Epoch):
        YY = int('20' + Epoch[:2])

        Epoch = Epoch[2:].split('.')

        dd = int(Epoch[0]) - 1

        h = float('0.' + Epoch[1]) * 24.0

        date = datetime.date(YY, 1, 1) + datetime.timedelta(dd)

        MM = float(date.month)
        DD = float(date.day)

        return YY, MM, DD, h

    def true_anomaly(self, EccEA):
        E_A, Ecc = EccEA
        return 2 * np.arctan(np.sqrt((1 + Ecc) / (1 - Ecc)) * np.tan(E_A / 2.0))

    def Names(self):
        return self.tle_sat_names

    def spheres(self, radius, clr, clr_gradient=None, dist=0):
        theta = np.linspace(0, 2 * np.pi, 100)
        phi = np.linspace(0, np.pi, 100)

        x_ = dist + radius * np.outer(np.cos(theta), np.sin(phi))
        y_ = radius * np.outer(np.sin(theta), np.sin(phi))
        z_ = radius * np.outer(np.ones(100), np.cos(phi))

        if clr_gradient == None:
            clr_gradient = clr
        else:
            pass

        trace = go.Surface(x=x_, y=y_, z=z_,
                           colorscale=[
                               [0, clr], [1, clr_gradient]],
                           showlegend=True,
                           name=self.body['Name']
                           )
        trace.update(showscale=False)

        return trace
