from soundRecorder import soundRecorder
from sensorRecorder import sensorRecorder
from multiprocessing import Process
from segmentator import segmentator
from classifier import classifier
from featureExtractor import featureExtractor
import numpy as np
import csv

soundNew = []
sensorNew = []
recorder = soundRecorder
sensors = sensorRecorder
segmenter = segmentator
featureExtraction = featureExtractor
decisions = classifier


def runInParallel(timeSensor, timeSound):
    stream = recorder.createStream(recorder)
    Process(target=sensorHandler(sensors, timeSensor)).start()
    Process(target=soundHandler(recorder, timeSound, stream)).start()


def sensorHandler(recorder, time):
    global sensorNew
    sensorNew = recorder.record(recorder, time)


def soundHandler(recorder, time, stream):
    global soundNew
    soundNew = recorder.record(recorder, time, stream)
    print(len(soundNew))


def predict(features):
    print("Your Sequence was: ")
    for i in decisions.linearClassifier.predict(features):
        if i == 0:
            print("Jab\n")
        elif i == 1:
            print("Palm Strike\n")
        elif i == 2:
            print("Hook\n")
        elif i == 3:
            print("Back Fist")
        elif i == 4:
            print("Uppercut")
    input("Press any key to continue")


def keyboardWait():
    x = input("press C to do another round")
    if x == 'c' or x == 'C':
        pass


def game():
    while 1:
        y = np.random.randint(2)
        z = np.random.randint(5, size=y+2)
        print("The sequence to do is: ")
        for i in z:
            if i == 0:
                print("Jab\n")
            elif i == 1:
                print("Palm Strike\n")
            elif i == 2:
                print("Hook\n")
            elif i == 3:
                print("Back Fist\n")
            elif i == 4:
                print("Uppercut\n")
        input("Press enter to start!\n")
        print("recording...")
        runInParallel(7000, 7)
        print("segmenting")
        soundConfirm, soundPunch = segmenter.soundSegment(segmenter, soundNew)
        sensorConfirm, sensorPunch = segmenter.sensorSegment(segmenter, sensorNew)
        print("classifying")
        if soundConfirm and sensorConfirm:
            if len(soundPunch) == len(sensorPunch):
                features = []
                for x in range(len(sensorPunch)):
                    features.append(featureExtraction.extract(featureExtraction, sensorPunch[x], soundPunch[x]))
                features = np.array(features)
                gamePredict(features, z)
            else:
                print("the punches detected don't match")
        else:
            print("no punches where detected press any key to continue")
        input("Press any key to continue  ")


def gamePredict(features, sequence):
    predictions = []
    equals = 0
    print("Your sequence was: ")
    for i in decisions.linearClassifier.predict(features):
        predictions.append(i)
        if i == 0:
            print("Jab\n")
        elif i == 1:
            print("Palm Strike\n")
        elif i == 2:
            print("Hook\n")
        elif i == 3:
            print("Back Fist\n")
        elif i == 4:
            print("Uppercut\n")
    for i in range(len(predictions)):
        if predictions[i] == sequence[i]:
            equals += 1
    try:
        print("Accuracy = " + str(equals/len(sequence)))
    except Exception:
        pass


def freePlay():
    while 1:
        print("recording...")
        runInParallel(7000, 7)
        print("segmenting")
        soundConfirm, soundPunch = segmenter.soundSegment(segmenter, soundNew)
        sensorConfirm, sensorPunch = segmenter.sensorSegment(segmenter, sensorNew)
        print("classifying")
        if soundConfirm and sensorConfirm:
            if len(soundPunch) == len(sensorPunch):
                features = []
                for x in range(len(sensorPunch)):
                    features.append(featureExtraction.extract(featureExtraction, sensorPunch[x], soundPunch[x]))
                features = np.array(features)
                predict(features)
            else:
                print("the punches detected don't match")
        else:
            input("no punches where detected press any key to continue  ")
        keyboardWait()


def newdataGathererer():
    while 1:
        input("When you are ready please press enter, you have 25 seconds to do the sequence\n Remember the sequence is: \n Jab(x5) | Palm Strike (x5) | Hook (x5)| Back Fist (x5) | Uppercut (x5)")
        runInParallel(25000, 25)
        soundConfirm, soundPunch = segmenter.soundSegment(segmenter, soundNew)
        sensorConfirm, sensorPunch = segmenter.sensorSegment(segmenter, sensorNew)
        if len(soundPunch) == 25 and len(sensorPunch) == 25:
            confirmation = input("Success! You completed the exercise and the sensors picked up all the data\n Would you like to append this new data to make the classifier better?\n Make sure the sequence was done as instructed. Type y to record or n to discard it  ")
            if confirmation == 'y' or confirmation == 'Y':
                sensorPunch1 = np.insert(sensorPunch, obj=0, values=0, axis=2)
                sensorPunch2 = np.insert(sensorPunch1, obj=7, values=0, axis=2)
                labels = np.array([[0],[0],[0],[0],[0],[1],[1],[1],[1],[1],[2],[2],[2],[2],[2],[3],[3],[3],[3],[3],[4],[4],[4],[4],[4]])
                with open('sensorData.csv', 'a') as appendFile:
                    newFileWritter = csv.writer(appendFile)
                    for i in sensorPunch2:
                        newFileWritter.writerow(i)
                with open('labels.csv', 'a') as appendFile:
                    newFileWritter = csv.writer(appendFile)
                    newFileWritter.writerows(labels)
                with open('sounds.csv', 'a') as appendFile:
                    newFileWritter = csv.writer(appendFile)
                    newFileWritter.writerows(soundPunch)
                input("Done! Press enter to try again or restart the program to access the other features  ")
        else:
            input("That didn't work quite well, press enter to try again or restart the program to acces the other features  ")




def brain():
    global sensorNew
    global soundNew
    decisions.loadData(decisions)
    decisions.trainClassifier(decisions)
    input("done loading, press any key to start punching")
    while 1:
        x = input("Press 1 to enter free mode, 2 to enter sequence mode or 3 to gather new data for the classifier")
        if x == '1':
            freePlay()
        elif x == '2':
            game()
        elif x == '3':
            newdataGathererer()


def main():
    brain()


if __name__ == '__main__':
    main()
