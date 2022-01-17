#https://github.com/matti644/btmon
#https://forum.arduino.cc/t/how-to-perform-read-and-write-between-raspberry-pi-4-and-arduino-nano-ble/628029
#https://www.programcreek.com/python/example/97796/bluepy.btle.Peripheral
import bluepy.btle as btle
import time
import sys

class BluetoothBackend:

    def __init__(self, streamlitStart):
        self.streamlit_start= streamlitStart
        pass

    def start(self):
        while True:
            """self.serverStartup()"""
            time.sleep(10)
            self.streamlit_start.addLog(to_append="Test")
            self.connect("fff")

    def connect(self, mac: str):
            """Connect to a device."""
            from bluepy.btle import Peripheral
            match_result = re.search(r'hci([\d]+)', self.adapter)
            if match_result is None:
                raise BluetoothBackendException(
                    'Invalid pattern "{}" for BLuetooth adpater. '
                    'Expetected something like "hci0".'.format(self.adapter))
            iface = int(match_result.group(1))
            self._peripheral = Peripheral(mac, iface=iface, addrType=self.address_type)
            print("Success")
            print(self._peripheral)