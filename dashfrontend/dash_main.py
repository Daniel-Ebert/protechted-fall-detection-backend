#!/usr/bin/env python3
import dash
import dash_bootstrap_components as dbc
from dash import Output, html, dcc, Input
from dash.exceptions import PreventUpdate
from dashfrontend.dashsubcomponents import *


class PlotlyDash():
    app: dash;
    logData: str = ""
    textOnSite : str = ""

    def __init__(self):
        pass

    def initPlotly(self):
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

        CONTENT_STYLE = {
            "margin-left": "18rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
        }

        content = dbc.Container([dcc.Textarea(id='liveupdate', value="This will contain the log", style={'width': '100%', 'height': '100%'}),
                                    dcc.Interval(interval=1000, n_intervals=0, id="trigger"),
                                    ], id="page-content", style=CONTENT_STYLE)

        self.app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

        @self.app.callback(Output('liveupdate', 'value'),
                      Input('trigger', 'n_intervals'))
        def updateLog(n_intervals):
            if self.textOnSite == self.logData:
                raise PreventUpdate
            self.textOnSite = self.logData
            return self.logData


    def runBackend(self):
        self.initPlotly()
        self.app.run_server(debug=False, host='0.0.0.0')


    def addLog(self, to_append: str):
        self.logData += to_append
