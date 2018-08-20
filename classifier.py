import numpy as np
import matplotlib.pyplot as plt
import csv
import tensorflow as tf
from featureExtractor import featureExtractor
from tensorflow.contrib import learn


class classifier:
    sensorData = []
    soundData = []
    labels = []
    linearClassifier = NotImplemented

    def loadData(self):
        with open('sensorData.csv', 'r') as readFile:
            newFileReader = csv.reader(readFile)
            for row in readFile:
                line = []
                for x in row.split(','):
                    line1 = []
                    for y in x.split(' '):
                        try:
                            line1.append(int(y))
                        except Exception:
                            pass
                    if len(line1) == 7:
                        line.append(line1)
                if len(line) == 250:
                    self.sensorData.append(line)
        with open('sounds.csv', 'r') as readFile:
            newFileReader = csv.reader(readFile)
            for row in readFile:
                empty = []
                for i in row.split(','):
                    empty.append(float(i))
                self.soundData.append(empty)
        with open('labels.csv', 'r') as readFile:
            newFileReader = csv.reader(readFile)
            for row in readFile:
                self.labels.append(int(row))

    def randomize(dataset, labels):
        permutation = np.random.permutation(labels.shape[0])
        shuffled_dataset = dataset[permutation]
        shuffled_labels = labels[permutation]
        return shuffled_dataset, shuffled_labels

    def trainClassifier(self):
        features = []
        featureExtraction = featureExtractor
        self.sensorData = np.array(self.sensorData)
        self.sensorData = self.sensorData[0:, 0:, 1:]
        self.soundData = np.array(self.soundData)
        self.labels = np.array(self.labels)

        for x in range(len(self.sensorData)):
            features.append(featureExtraction.extract(featureExtraction, self.sensorData[x], self.soundData[x, 0:]))
        features = np.array(features)
        training = features[:600]
        test = features[500:550]
        validation = features[550:]
        training_labels = self.labels[:600]
        test_labels = self.labels[500:550]
        validaton_labels = self.labels[550:]
        train_dataset, train_labels = self.randomize(training, training_labels)
        test_dataset, test_labels = self.randomize(test, test_labels)
        validation_dataset, validation_labels = self.randomize(validation, validaton_labels)
        feature_columns = learn.infer_real_valued_columns_from_input(train_dataset)
        print("loading...")
        classifier = learn.LinearClassifier(n_classes=5, feature_columns=feature_columns,
                                            optimizer=tf.train.FtrlOptimizer(
                                                learning_rate_power=-0.69,
                                                learning_rate=0.00001,
                                                l1_regularization_strength=0.1))
        classifier.fit(train_dataset, train_labels, steps=30000)
        print("done")
        self.linearClassifier = classifier
