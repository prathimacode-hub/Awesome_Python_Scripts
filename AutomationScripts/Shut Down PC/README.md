## Description:
- Firstly, you have to input your voice command whether you want to shutdown your computer or not.
- If "yes", it will shut down your computer; otherwise, it will not. 

## Procedure: 
```python
import os
import pyttsx3
import speech_recognition as sr
```
- Then we will define one class, which have three functions namely **takecommands()**, **Speak()**, and **quiteSelf()**.
- **takecommands()**: 
  - Using **sr.Recognizer()** it will recognise your voice and **sr.Microphone()** for input voice commands.
  - Using **r.recognize_google()** it recognizes the language of the user, and check whether the language is **en-in** or not.
- **Speak()**: 
  - Using **pyttsx3.init('sapi5')** for voice recognition and synthesis.
  - Using **engine.getProperty('voices')** for setting voice type and id.
  - **runAndWait()** speech recognition Code Answer's. engine. say("I am the text spoken after changing the speech rate.")
- **quitSelf**:
  - Method to self shut down system.

## Sample Output:
![LGM](https://github.com/AmitGupta700/Awesome_Python_Scripts/blob/main/AutomationScripts/Shut%20Down%20PC/Images/output.png)
