from .bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
from .utilities import Orbit
import plotly.graph_objects as go
import plotly.offline as plt


# Plotter
class Plotter:
    def __init__(self, body):
        self.body = body

    def Plot(self, OrbitalPaths=None, names=None, Colors=None):

        if Colors == None:

            self.Colors = [
                'black',
                '#1e43ff',
                'tomato',
                'limegreen',
                'crimson',
                'indigo',
                'saddlebrown',
                'deeppink',
                'slategray',
                'gold',
                'navy'
            ]

        else:
            self.Colors = Colors

        if OrbitalPaths != None:

            self.names = names
            radius = self.body['Radius']
            color = self.body['Color']
            color_gradient = self.body['Color_Gradient']

            Body = Orbit.spheres(self, radius, color, color_gradient)

            orbits = []

            orbit_Id = 0
            color_Id = 0

            colors_iterate = len(self.Colors) - 1

            for n_orbit in OrbitalPaths:

                if color_Id <= colors_iterate:
                    pass
                else:
                    color_Id = 0

                n_rxs = n_orbit[0]
                n_rys = n_orbit[1]
                n_rzs = n_orbit[2]

                n_rs_trace = go.Scatter3d(x=n_rxs, y=n_rys, z=n_rzs,
                                          marker=dict(size=0.1),
                                          line=dict(
                                              color=self.Colors[color_Id],
                                              width=2),
                                          name=self.names[orbit_Id])
                orbits.append(n_rs_trace)

                n_rs_starting = go.Scatter3d(x=[n_rxs[0]], y=[n_rys[0]], z=[n_rzs[0]],
                                             marker=dict(
                    color=self.Colors[color_Id], size=4),
                    name="Initial Position"
                )
                orbits.append(n_rs_starting)

                orbit_Id += 1
                color_Id += 1

            self.layout = go.Layout(title='', showlegend=True, margin=dict(l=0, r=0, t=0, b=0),
                                    scene=dict(xaxis=dict(title='x (km)'),
                                               yaxis=dict(title='y (km)'),
                                               zaxis=dict(title='z (km)'),
                                               aspectmode='data',
                                               camera=dict(
                                                   up=dict(x=0, y=0, z=1),
                                                   center=dict(x=0, y=0, z=0),
                                                   eye=dict(x=1.25, y=1.25, z=1.25))),
                                    legend=dict(
                                        yanchor="top",
                                        y=0.98,
                                        xanchor="right",
                                        x=0.99)
                                    )

            plot_objects = []
            plot_objects.append(Body)

            for orbit in orbits:
                plot_objects.append(orbit)

            self.fig = go.Figure(
                data=plot_objects, layout=self.layout)

            print('Successful')

            self.fig.write_json("EllipsePy_Starlink.json")

            return self.fig.show(),

        else:
            self.names = names
            radius = self.body['Radius']
            color = self.body['Color']
            color_gradient = self.body['Color_Gradient']

            Body = Orbit.spheres(self, radius, color, color_gradient)

            layout = go.Layout(title="{} Plot".format(self.body['Name']), showlegend=True, margin=dict(l=0, r=0, t=0, b=0),
                               scene=dict(xaxis=dict(title='x (km)'),
                                          yaxis=dict(title='y (km)'),
                                          zaxis=dict(title='z (km)'),
                                          camera=dict(
                                              up=dict(x=0, y=0, z=1),
                                              center=dict(x=0, y=0, z=0),
                                              eye=dict(x=1.25, y=1.25, z=1.25))
                                          ), legend=dict(
                                              yanchor="top",
                                              y=0.98,
                                              xanchor="right",
                                              x=0.99),
                               )

            fig = go.Figure(data=[Body], layout=layout)

            return fig.show()
