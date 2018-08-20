# PunchableInterfaceLive
This repository contains the classifier, data and live version of a punching classifier.
The hardware used for this project was the Arduino nano and the GY-521 sensor. Additionally,
a microphone is used connected to a preamp to avoid clipping. The initial data set
has 600 punches, 120 of each class and can be found as the default data set
of the classifier and as part of the BackUpData folder.

The system is still in early development stage. One of the big issues I could
not get around was exporting the classifier. Therefore the system retrains it
every time the program is run. Inside the classifier method, one kind find the
necessary tools to test the accuracy of this classifier. It has around 93% accuracy
in both the training and validation sets.

This is a list of the features used:

    Mean, variance and standard deviation of each axis in both the accelerometre and the gyroscope
    
    Maximum and minimum value of each axis in both the accelerometre and the gyroscope
    
    The amount of zero crossing in each axis of both the accelerometre and the gyroscope
    
    Standard deviation of the mean values for each sensor
    
    Phase of the fast fourier transform of the sound
    
    Amplitude of the 3 highest peaks of the fft of the sound

Another possible improvement could be making the data set bigger since it is most
certainly over-fitted to the punches of just 4 individuals.
