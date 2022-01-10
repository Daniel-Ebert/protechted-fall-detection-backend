#!/usr/bin/env python3
"""
desc: Main is used to run the backend server for accepting BLE information and starting the streamlit visualizer
author: Daniel Ebert
date: 2022-01-10
"""

import threading
from bluetoothbackend.bluetooth_backend_main import BluetoothBackend

class BluetoothBackendThread(threading.Thread):

    def __init__(self, threadID, name, counter,streamlit_start):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.streamlit_start = streamlit_start
        self.counter = counter

    def run(self):
        print("Starting Bluetooth Backend Thread " + self.name)
        BluetoothBackend(streamlitStart=self.streamlit_start).start()
        print("Exiting Bluetooth Backend Thread" + self.name)
