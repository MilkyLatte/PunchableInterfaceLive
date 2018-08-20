# PunchableInterfaceLive


# Overview:

The aim of the project is to build an interactive training set that supports martial arts training at home. This requires (i) augmenting martial arts equipment with sensors to collect training data, (ii) developing a machine learning algorithm able to distinguish between different punching/striking techniques, and (iii) ensuring the system can recognise and classify punches.

The data that was used to train the classifier was measured using the sensor GY-521. This device provides a gyroscope and accelerometre. Additionally, the sound was also used to differentiate the punches. 


The controller used for this sensor was the Arduino nano which gathered the data and sent it trough the Serial Port to the computer. In order to do all the data analysis, Python was my language of choice thanks to the support there is for machine learning. The sensors were put on the wrist with a 3D printed case and covered with a silicon layer to ensure comfort and stability. The last piece of hardware used was the microphone and pre-amp in order to capture the sound of the impact.
# Method

The punches used in this project were, front punch, front slap, hook, back fist and uppercut.

Using Python's serial library, the data was read and stored into a csv file if it is recognised as a punch. At this stage, there is no machine learning involved, since the training was gathered systematically, a movement will be recognised as a punch if certain values exceed an specific threshold. Setting this threshold was a big challenge since it needs to be as general as possible. To achieve this, the time-frame of a punch had to be adjusted multiple times. Initially the classifier was confusing certain types of punches since the time-frame was not capturing the previous instances of the punch and after adjusting this, making the time-frames longer, the accuracy rose.

# Data Collection:

The data collection was the most important stage of the project. It had to be done 3 times since the fist to attempts encountered inconsistencies with the data. All the 3 attempts were done in the same format, 25 seconds to do 25 punches, 5 of each type of punch. This was also done in the same sequence; Jab, Palm Strike, Hook, Back Fist and Uppercut.

After gathering data for the first time, it was noticed that the values of the microphone were clipping, therefore, the microphone data ended up not being very useful.  To solve this, a hardware change had to be made. This change was both the inclusion of the pre-amp and the use of a more sophisticated microphone. The pre-amp allowed adjusting the gain to the point it does not clip any more and provides accurate data.

The second attempt, as mentioned previously, used short time-frames when segmenting the data. This was a good attempt to increase performance but it raised tow different new issues. Firstly, the time-frame was not enough to capture the entirety of the punch, since it would only capture data from a peak on, ignoring the instances before the big impact of the punch and just relying on the movement after. The second, issue was that some noise was being included as a punch. Since the time-frames were smaller, this meant there were more chances for a peak to be considered a punch. This meant that the data was not reliable and a third attempt had to be done.

The final, successful, attempt corrected the problems encountered in the two previous ones. After the hardware change, the time-frames were increased. Now, when segmenting the data, if a peak is found, 50 instances of data before the peak will be captured and 200 instances after. This captures the whole essence of the punch and eliminates unnecessary noise in the data. This algorithm is also used in the live version were the user will get live feedback from the program.

# Features

Choosing the features was also a big challenge since plotting the data was not the most helpful tool when trying to find clusters of punches. Looking back to certain papers on human motion recognition helped solve this problem. Even though there is not much written about the specific motion that was measured in this project, multiple studies have taken place regarding other types of human activities, therefore, some of those features where used. In then end, 47 different features where used:

    Mean, variance and standard deviation of each axis in both the accelerometre and the gyroscope
    Maximum and minimum value of each axis in both the accelerometre and the gyroscope
    The amount of zero crossing in each axis of both the accelerometre and the gyroscope
    Standard deviation of the mean values for each sensor
    Phase of the fast fourier transform of the sound
    Amplitude of the 3 highest peaks of the fft of the sound

# Classifier

The library of choice for the classifier was Tensor Flow since it offers a big range of classifiers that were suitable for the task in hand. After exploring some of the different classifiers that this library offers, the Linear Classifier was the chosen one since it provided the best results. The main technique used to train the classifier was cross validation. After rigorous attempts with different values of the optimizer, including learning rate and l1 regularization strength, the classifier achieved an accuracy of 93% in both the testing and validation datasets.

# Live Version

A live version was developed as the final stage of this project. This live version uses the classifier to provide feedback to the user in real time. The user has a choice of 3 different modes. The first one is "Free Mode" and it allows the user to perform any sequence during 7 seconds and it will classify all the punches given by the user. The second one is "Sequence Mode", were the program generates a random sequence of punches that the user has to do, after, the program will classify the punches and output the accuracy of the sequence done by the user in comparison to the one randomly generated. Finally, the "Data Gathering Mode" allows the user to add more data to the classifier to make it smarter and less over-fitted (this will be discussed in the improvements section), in this mode, the user will perform the same 25 punch sequence mentioned in the data collection section. This live version was the last part of the project and it marked the end of the internship.

# Possible Improvements

Over-fitting

During the two initial data gathering attempts, more people were used to do the sequence of punches. However, for the third attempt, due to time shortage, all the punches were done by the same two people. While the model still classifies the punches from other individuals accurately most of the time, adding more data from other people would make the classifier much more universal adjusting to the punches of different individuals and techniques.

Hardware improvements

Although the model that is being used at the moment works well, it is too big and can be uncomfortable when wore for an extended period of time. In addition to using a smaller model, making it wireless would make it a more interesting product, for research purposes the wired version performs well but making it wireless would not only make it more comfortable but more attractive. The inclusion of the microphone was a decision mainly taken to differentiate the palm-strike and the jab, because they both have a very similar motion but the sound they both produce is different, it also serves now as a way of confirming a punch, hence a punch will only be considered as a punch if both motion and sound were detected. For now, the microphone is included as a separate element, but immersing inside the model would create a more complete product.

Classifier

Exporting the classifier was something that could not be done, or at least I could not do. Retraining the model every time a program is run is not the most efficient thing to do, and most libraries provide a way around this by letting the user export the classifier. However, after many attempts, the classifier used could not be exported. The classifier can be found here https://www.tensorflow.org/api_docs/python/tf/contrib/learn/LinearClassifier#properties.
