import numpy as np


class segmentator():
    def soundSegment(self, dataSound):
        print(max(dataSound))
        soundIncluded = 0
        punchSound = []
        punch = False
        for x in range(len(dataSound)):
            if abs(dataSound[x]) >= 500 and x > soundIncluded:
                currentPunch = []
                print("Sound")
                punch = True
                for i in range(5000):
                    try:
                        currentPunch.append(dataSound[x+i])
                    except Exception:
                        pass
                punchSound.append(currentPunch)
                soundIncluded = x + 5000
        punchSound = (np.array(punchSound))
        print(punchSound.shape)
        return punch, punchSound

    def sensorSegment(self, dataSensor):
        dataSensor = np.array(dataSensor)
        accelMean = np.mean(dataSensor[0:, :3], axis=1)
        included = 0
        punch = []
        confirm = False
        for x in range(len(accelMean)):
            if (accelMean[x]) >= 9000 and x > included:
                print("punch")
                confirm = True
                currentPunch = []
                xvalue = x - 50
                for i in range(250):
                    try:
                        currentPunch.append(dataSensor[xvalue + i])
                    except Exception:
                        pass
                punch.append(currentPunch)
                included = x+200
        punch = (np.array(punch))
        return confirm, punch

    def saveSegment():
        pass
