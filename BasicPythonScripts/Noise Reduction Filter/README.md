# 📢**NOISE REDUCTION FILTER**
<p align="center">
  <img width="600" height="325" src="http://www.reactiongifs.com/r/ln1.gif">
</p>
There’s no single definition of audio noise, but in general, it’s background sounds such as fans, people talking, cars or trucks driving by, buzz from faulty audio wires, or other ambient noises that shouldn’t be in your audio.

## ❓ **WHAT IS NOISE REDUCTION**
Noise Reduction can reduce constant background sounds such as hum, whistle, whine, buzz, and "hiss", such as tape hiss, fan noise or FM/webcast carrier noise. It is not suitable for individual clicks and pops, or irregular background noise such as from traffic or an audience.
To use Noise Reduction, you need a region in the waveform that contains only the noise you want to reduce.
<p align="center">
  <img width="625" height="250" src="https://i.stack.imgur.com/W2nwb.png">
</p>

## 🔇 **Need of Noise Reduction**
Noise reduction is the process of removing noise from a signal. Noise reduction techniques exist for audio and images. 
Noise reduction algorithms may distort the signal to some degree. 
Noise rejection is the ability of a circuit to isolate an undesired signal component from the desired signal component, as with common-mode rejection ratio.

## 📗**NOISE REDUCTION USING PYTHON**
### **IMPLEMENTATION**
In this particular we will be aiming to remove noise from BIRD AUDIO SAMPLES. The focus is to start to explore some techniques of preprocessing that can be used to improve bird detection models.

The following steps will be followed-
1. Preprocessing: To read a audio file, optionally apply signal filtering techniques, and perform feature extraction (e.g. mfccs);
2. Trainning a classification model based on features (TO DO);
3. Evaluation: To test the trainned models over a split of the dataset (TO DO).

--- 

### **FILTRATION TECHNIQUES USED**
1. Traditional log mel-spectogram.
2. High-Pass Filtering: Reduces low frequencies, once bird sound are commonly present on high frequencies.

---

### ☑️**LIBRARIES USED**
**LIBROSA**- librosa is a python package for music and audio analysis. It provides the building blocks necessary to create music information retrieval systems.
https://librosa.org/doc/latest/index.html

## 📊**CODING WORKFLOW**

<p align="center">
  <img width="625" height="450" src="https://user-images.githubusercontent.com/36481036/194615115-0f7ef39d-94d8-44db-a752-f327158f1bbb.png">
</p>

## 🎯**RESULTS**
After applying and filtering low frequency filters, significant reduction in noise was observed from both the audios. The audios can be analyzed from the notebook mentioned in this repo. 
![filtering low-frequencies01](https://user-images.githubusercontent.com/36481036/194620984-3dc9f1fb-b037-4e46-ad15-cd8ae1966788.png)

![filtering low-frequencies02](https://user-images.githubusercontent.com/36481036/194620991-a818976e-7d05-4cc5-b023-108043c6487d.png)



## :page_facing_up: **CONCLUSION**
* For both audio samples, the filter helped to isolate the interesting frequencies. The first audio is in a very good quality for distincting the birds. 
* The second audio still has some noise but significant improvements in noise reduction can be observed.

## :bust_in_silhouette: **CREDITS**
* https://timsainburg.com/noise-reduction-python.html
* https://mixkit.co/free-sound-effects/bird/

**:sunglasses:** **CREATOR**- https://github.com/theshredbox
