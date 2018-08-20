import serial
import numpy as np
import matplotlib as plt
from drawnow import *
import time


class sensorRecorder:
    arduinoData = serial.Serial('/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0', 1000000)

    def record(self, recordTime):
        executingTime = 0
        start = int(round(time.time()*1000))
        data = []
        while executingTime < recordTime:
            while (self.arduinoData.inWaiting() == 0):
                pass
            arduinoString = self.arduinoData.readline()
            try:
                dataArray = arduinoString.decode().split(',')
            except Exception:
                pass
            try:
                acX = int(dataArray[0])
                acY = int(dataArray[1])
                acZ = int(dataArray[2])

                gyX = int(dataArray[3])
                gyY = int(dataArray[4])
                gyZ = int(dataArray[5])
                new = [acX, acY, acZ, gyX, gyY, gyZ]
                data.append(new)
            except Exception:
                pass
            executingTime = int(round(time.time()*1000)) - start
        return data
