#!/usr/bin/env python3
"""
desc: Main is used to run the backend server for accepting BLE information and starting the streamlit visualizer
author: Daniel Ebert
date: 2022-01-10
"""

import threading
import sys
from streamlitfrontend.streamlit_main import PlotlyDash


class StreamlitStart(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.dash = None
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def getDashClass(self):
        return self.dash
    def run(self):
        print("Starting Streamlit Thread " + self.name)

        self.dash = PlotlyDash()
        self.dash.runBackend()
        print("Exiting Streamlit Thread" + self.name)

        
        """print(os.path.join(
             'streamlitfrontend', 'streamlit_main.py'))
        process = Popen(["streamlit", "run", os.path.join(
             'streamlitfrontend', 'streamlit_main.py')], stdout=PIPE, stderr=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()"""

    def addLog(self, to_append: str):
        self.dash.addLog(to_append=to_append)