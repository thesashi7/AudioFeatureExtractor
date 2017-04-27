# AudioFeatureExtractor
  This is an Audio Feature Extractor that uses pyAudioAnalysis library to extract audio features.
  
  This pacakge includes pyAudioAnalysis. So, you can just clone this repository to get pyAudioAnalysis.
  However, if you intend to setup pyAudioAnalysis separately then you will need to clone this pyAudioAnalysis library locally.    As, it is not available as a python package yet.

Dependecies: numpy, matplotlib, scipy, sklearn, hmmlearn, simplejson, eyed3, pydub

*Sample Data presented in data and data1 folders*

**TO RUN**

  *extractor script --> fextractor.py*
  
  Enter in terminal: 
 
  python fextractor.py "full path to your directory containing wav files"
  ```
  python fextractor.py
 
/home/sashi/Documents/Spring2017/CS599/project/fex/data/
('wavFiles:', ['/home/sashi/Documents/Spring2017/CS599/project/fex/data/21013_44k.wav', '/home/sashi/Documents/Spring2017/CS599/project/fex/data/21621_44k.wav', '/home/sashi/Documents/Spring2017/CS599/project/fex/data/cat0.wav', '/home/sashi/Documents/Spring2017/CS599/project/fex/data/cat1.wav'])
Analyzing file 1 of 4: /home/sashi/Documents/Spring2017/CS599/project/fex/data/21013_44k.wav
Analyzing file 2 of 4: /home/sashi/Documents/Spring2017/CS599/project/fex/data/21621_44k.wav
Analyzing file 3 of 4: /home/sashi/Documents/Spring2017/CS599/project/fex/data/cat0.wav
Analyzing file 4 of 4: /home/sashi/Documents/Spring2017/CS599/project/fex/data/cat1.wav
Feature extraction complexity ratio: 9.1 x realtime

Do you want to write this to a CSV file?(Enter y for Yes or any key for NO):
y
Enter the name for your CSV file: test
```
  
**Please visit the following links for more details about pyAudioAnalysis:**

	https://github.com/tyiannak/pyAudioAnalysis
	http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144610

