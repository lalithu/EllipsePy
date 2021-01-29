from .utilities import spheres, Orbit
import plotly.graph_objects as go


# Plotter
class Plotter:
    def __init__(self, body):
        self.body = body

    def Plot(self, Orbit=None):

        if Orbit != None:
            Body = spheres(
                self.body['Radius'], self.body['Color'], self.body['Color_Gradient'])

            self.rxs = Orbit[0]
            self.rys = Orbit[1]
            self.rzs = Orbit[2]

            self.rs_trace = go.Scatter3d(x=self.rxs, y=self.rys, z=self.rzs,
                                         marker=dict(size=0.1),
                                         line=dict(color="black", width=2),
                                         name="Trajectory")

            self.rs_starting = go.Scatter3d(x=[self.rxs[0]], y=[self.rys[0]], z=[self.rzs[0]],
                                            marker=dict(color='black', size=4),
                                            name="Initial Position"
                                            )

            self.layout = go.Layout(title='Solar System', showlegend=True, margin=dict(l=0, r=0, t=0, b=0),
                                    scene=dict(xaxis=dict(title='x (km)'),
                                               yaxis=dict(title='y (km)'),
                                               zaxis=dict(title='z (km)')
                                               ))

            self.fig = go.Figure(
                data=[Body, self.rs_trace, self.rs_starting], layout=self.layout)

            return self.fig.show()

        else:
            Body = spheres(
                self.body['Radius'], self.body['Color'], self.body['Color_Gradient'])

            layout = go.Layout(title="{} Plot".format(self.body['Name']), showlegend=False, margin=dict(l=0, r=0, t=0, b=0),
                               scene=dict(xaxis=dict(title='x (km)'),
                                          yaxis=dict(title='y (km)'),
                                          zaxis=dict(title='z (km)')
                                          ))

            fig = go.Figure(data=[Body], layout=layout)

            return fig.show()
