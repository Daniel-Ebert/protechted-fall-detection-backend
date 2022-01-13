#https://github.com/matti644/btmon
import bluetooth
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


    def serverStartup(self):
        s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        server_address = '00:1A:7D:DA:71:06'
        server_port = 1
        backlog = 1
        size = 1024

        s.bind((server_address, server_port))
        s.listen(backlog)
        try:
            print("Awaiting connection")
            client, clientInfo = s.accept()
            print("Connection established")

            while 1:
                j = 0
                msg = ""
                for i in range(1, 100):
                    j += 0.1
                    msg += str(i) + "," + str(j) + ";"
                    time.sleep(0.01)
                    if (i % 10 == 0):
                        print(msg)
                        msg += "\n"
                        client.send(msg)
                        msg = ""

                    if (i == 100):
                        i = 0
                        if (j == 100):
                            j = 0

        except:
            print("Closing socket" + str(sys.exc_info()[1]))
            s.close()


