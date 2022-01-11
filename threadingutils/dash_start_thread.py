#!/usr/bin/env python3
"""
desc: Main is used to run the backend server for accepting BLE information and starting the streamlit visualizer
author: Daniel Ebert
date: 2022-01-10
"""

import threading
import sys
from dashfrontend.dash_main import PlotlyDash


class DashStart(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.dash = None
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def getDashClass(self):
        return self.dash
    def run(self):
        print("Starting Plotly Dash Thread " + self.name)

        self.dash = PlotlyDash()
        self.dash.runBackend()
        print("Exiting Plotly Dash Thread" + self.name)

    def addLog(self, to_append: str):
        self.dash.addLog(to_append=to_append)