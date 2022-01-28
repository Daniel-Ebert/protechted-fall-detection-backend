# https://github.com/matti644/btmon
# https://forum.arduino.cc/t/how-to-perform-read-and-write-between-raspberry-pi-4-and-arduino-nano-ble/628029
# https://www.programcreek.com/python/example/97796/bluepy.btle.Peripheral
import binascii
import struct
import time
from bluepy.btle import UUID, Peripheral, DefaultDelegate
import time
import sys


class MyDelegate(DefaultDelegate):
    def __init__(self, plotlydash_reference):
        DefaultDelegate.__init__(self)
        self.plotlydashreference = plotlydash_reference

    def handleNotification(self, cHandle, data):
        val = binascii.b2a_hex(data)
        val = binascii.unhexlify(val)
        val = struct.unpack('f', val)[0]
        print(" Sensor value " + str(val))
        self.plotlydashreference.addLog(to_append=" Sensor value " + str(val) + "\n")
        data = bytearray(data)
        print('Developer: do what you want with the data.')
        print(data)


class BluetoothBackend:

    def __init__(self, streamlitStart):
        self.streamlit_start = streamlitStart
        pass

    def start(self):
        while True:
            print("Test")
            self.connect()

    def connect(self):
        fall_det_uuid = UUID("ee4efbdc-7536-11ec-90d6-0242ac120003")

        p = Peripheral("16:E0:EE:EC:1A:4D", "public")

        print
        "Connecting..."
        p.setDelegate(MyDelegate(self.streamlit_start))

        data_chrc = p.getCharacteristics(uuid=fall_det_uuid)[0]

        # print "Debug Services..."
        # for svc in dev.services:
        # 	print str(svc)

        # print 'Debug Characteristics...'
        # for ch in es_service.getCharacteristics():
        # 	print str(ch)

        # Enable the sensor, start notifications
        # Writing x01 is the protocol for all BLE notifications.
        data_chrc.write(bytes("\x01"))

        time.sleep(1.0)  # Allow sensor to stabilise

        # Main loop --------
        while True:
            if p.waitForNotifications(1.0):
                # handleNotification() was called
                continue
            print("Waiting...")
        # Constant Read Not Good for Batterie


"""        try:
            ch = p.getCharacteristics(uuid=fall_det_uuid)[0]
            if (ch.supportsRead()):
                while 1:
                    val = binascii.b2a_hex(ch.read())
                    val = binascii.unhexlify(val)
                    val = struct.unpack('f', val)[0]
                    print(" Sensor value " + str(val))
                    time.sleep(1)
                    self.streamlit_start.addLog(to_append=" Sensor value " + str(val) + "\n")

        finally:
            p.disconnect()"""
