#!/usr/bin/env python3
import dash
import dash_bootstrap_components as dbc
from dash import Output, html, dcc, Input
from dash.exceptions import PreventUpdate



class PlotlyDash():
    app: dash;
    logData: str = ""
    textOnSite : str = ""

    def __init__(self):
        pass

    def initPlotly(self):
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

        self.app.layout = dbc.Container([html.Div(id='liveupdate'),
                                    dcc.Interval(interval=1000, n_intervals=0, id="trigger"),
                                    dbc.Alert(
                                        "Hello, Bootstrap!", className="m-5"
                                    )], id="page-content")

        @self.app.callback(Output('liveupdate', 'children'),
                      Input('trigger', 'n_intervals'))
        def updateLog(n_intervals):
            if self.textOnSite == self.logData:
                raise PreventUpdate
            self.textOnSite = self.logData
            return html.Plaintext(self.logData)


    def runBackend(self):
        self.initPlotly()
        self.app.run_server(debug=False)


    def addLog(self, to_append: str):
        self.logData += to_append
