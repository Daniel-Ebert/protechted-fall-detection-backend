#!/usr/bin/env python3
"""
desc: Main is used to run the backend server for accepting BLE information and starting the streamlit visualizer
author: Daniel Ebert
date: 2022-01-10
"""

import threading
from threadingutils.dash_start_thread import DashStart
from threadingutils.bluetooth_backend_start_thread import BluetoothBackendThread

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    dash_thread = DashStart(1, "Thread-1", 1)
    dash_thread.start()
    bluetooth_backend_thread = BluetoothBackendThread(1, "Thread-1", 1, dash_thread)
    bluetooth_backend_thread.start()
