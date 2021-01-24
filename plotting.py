import poliastro.plotting.porkchop
import bodies
from utilities import spheres, Orbits
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'browser'


# Plotter
class Plotter:
    def __init__(self, body):
        self.body = body

    def Plot(self):
        Body = spheres(
            self.body['Radius'], self.body['Color'], self.body['Color_Gradient'])

        layout = go.Layout(title="{} Plot".format(self.body['Name']), showlegend=False, margin=dict(l=0, r=0, t=0, b=0),
                           scene=dict(xaxis=dict(title='x (km)'),
                                      yaxis=dict(title='y (km)'),
                                      zaxis=dict(title='z (km)')
                                      ))

        fig = go.Figure(data=[Body], layout=layout)

        return fig.show()
