import sys
import csv
import json
from pyAudioAnalysis.audioFeatureExtraction import *

#######################################################################################################
#######################################################################################################
#
# FeatureExtractor uses pyAudioAnalysis library to extract audio features.
# Currently we will need to clone the library locally, it is not found as a python package yet.
# Dependecies pYAudioAnalysis, numpy, matplotlib, scipy, sklearn, hmmlearn, simplejson, eyed3, pydub
# Please visit the following links for more details about pyAudioAnalysis:
#		https://github.com/tyiannak/pyAudioAnalysis
#		http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144610
#
#    The following audio features are evaluated and collected in pyAudioAnalysis
#    1			Zero Crossing Rate
#    2 			Energy							
#    3 			Entropy of Energy
#    4 			Spectral Centroid
#    5 			Spectral Spread
#    6 			Spectral Entropy
#    7 			Spectral Flux
#    8 			Spectral Rolloff
#    9-21 	MFCCs
#    22-33 	Chroma Vector
#    34 		Chroma Deviation
#
class FeatureExtractor:

  ##Parameter Tuning for feature extraction guys
  # Default is fine for now but tune it for fun [:) 
  # 	BE A TUNER MY FRIEND
  ###################################################################
  #
  # Steps are shorter than the Window length or equal
  #@new_file_path: Full path of your data folder where wav files exist
  #@new_mtWin  : Mid-Term Window size usually between 1 to 10 seconds (In Seconds)
  #@new_mtStep :Mid-Term Step size (In Seconds)
  #@new_stWin  : Short-Term window size usually between 20 to 100 ms (In Seconds)
  #@new_stStep : Short-Term step size (In Seconds)
  #@new_computeBEAT : Boolean Value to compute BEAT of audio (This is for Music Audio)
  #
  def __init__(self, new_file_path, new_mtWin=10, new_mtStep=1, new_stWin=.02, new_stStep=.01, new_computeBEAT=False):
    self.file_path = new_file_path
    self.mtWin = new_mtWin
    self.mtStep = new_mtStep
    self.stWin = new_stWin
    self.stStep = new_stStep
    self.computeBEAT = new_computeBEAT 

  #################################################################
  #@return feature vectors
  # Multidimenstional array for more than one wave file
  #
  def extract(self):
    return dirWavFeatureExtraction(self.file_path, self.mtWin, self.mtStep, self.stWin, self.stStep, self.computeBEAT)[0]  

  ##################################################################
  #@features: feature vectors
  #@file_name: Name of the csv file that you want to write the featues to
  #
  def write_csv(self,features,file_name="test-data"):
    with open(file_name+".csv", 'w') as csvfile:
      writer = csv.writer(csvfile,delimiter=',',quoting = csv.QUOTE_NONE)
      #print(type(features[0]))
      if(isinstance(features[0],numpy.ndarray)):
        for fv in features:
          writer.writerow(fv)
      else: #only one feature vector
        writer.writerow(features)

    """with open(file_name+".csv",'r') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        print(row[0])"""

##
#(class)FeatureExtractor ENDS
##


###################################################################
#                Main
#
def main():
  #Set your default path or else this will crash and burn in default mode
  file_path = "/home/sashi/Documents/Spring2017/CS599/project/fex/data/"
  if(len(sys.argv)>1):
    file_path = sys.argv[1]
  fExt = FeatureExtractor(file_path)
  features  = fExt.extract()
  write = raw_input("Do you want to write this to a CSV file?(Enter y for Yes or any key for NO):\n")
  if(write.lower()=="y"):
    csv_file_name = raw_input("Enter the name for your CSV file: ")
    fExt.write_csv(features, csv_file_name)
  #print features

#
#Entry point of script --> Entering Main
#
if  __name__ =='__main__':main()


