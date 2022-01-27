#https://github.com/matti644/btmon
#https://forum.arduino.cc/t/how-to-perform-read-and-write-between-raspberry-pi-4-and-arduino-nano-ble/628029
#https://www.programcreek.com/python/example/97796/bluepy.btle.Peripheral
import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral
import time
import sys

class BluetoothBackend:

    def __init__(self, streamlitStart):
        self.streamlit_start= streamlitStart
        pass

    def start(self):
        while True:
            """self.serverStartup()"""
            self.connect()

    def connect(self):
        fall_det_uuid = UUID("ee4efbdc-7536-11ec-90d6-0242ac120003")

        p = Peripheral("16:E0:EE:EC:1A:4D", "public")

        try:
            ch = p.getCharacteristics(uuid=fall_det_uuid)[0]
            if (ch.supportsRead()):
                while 1:
                    val = binascii.b2a_hex(ch.read())
                    val = binascii.unhexlify(val)
                    val = struct.unpack('f', val)[0]
                    print(" Sensor value " + str(val))
                    time.sleep(1)
                    self.streamlit_start.addLog(to_append=" Sensor value " + str(val))

        finally:
            p.disconnect()