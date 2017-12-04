#!/usr/local/bin/python2

# References:
#   * https://github.com/tyiannak/pyAudioAnalysis
#   * https://github.com/tyiannak/pyAudioAnalysis/wiki/4.-Classification-and-Regression
#   * http://rwx.io/blog/2016/04/08/bp-pyaudioanalysis/


import os
import numpy as np
from sys import argv
from pyAudioAnalysis import audioTrainTest as aT

test_dir="testing_data"
training_dir=[
		"training_data/bp-belly_pain"
		,"training_data/bu-needs_burping"
		,"training_data/ch-cold_hot"
		,"training_data/dc-discomfort"
		,"training_data/hu-hungry"
		,"training_data/la-laughter"
		,"training_data/ti-tired"
	]

print("********************")
print("TRAINING")
print("********************")
aT.featureAndTrain(training_dir, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)

print("********************")
print("RESULT")
print("********************")
fileout = open("result.txt","w") 
for filename in os.listdir(test_dir):
	filename=test_dir+"/"+filename
	Result, P, classNames = aT.fileClassification(filename, "svmSMtemp", "svm")
	winner = np.argmax(P) #pick the result with the highest probability value.
	print("File: " +filename + "; Category: " + classNames[winner] + "; Probability: " + str(P[winner]))
 	fileout.write("File: " +filename + "; Category: " + classNames[winner] + "; Probability: " + str(P[winner]) + "\n") 
fileout.close() 
