# PDF to Audio Book Converter

This script works on converting the text in a PDF into audio. It allows the text to be read out.

### Libraries used :

- PyPDF2 -- Used for basic operations on PDFs.
- pyttsx3 -- Used for text to speech conversion.

### Work flow :

1. The program opens the PDF whose path is entered in the code.
2. PyPDF2 library performs operations on the PDF such as counting number of pages in the PDF and reading it.
3. pyttsx3 library converts the text into audio format.
4. A message 'Playing audio..' is displayed on the terminal.
5. An audio starts reading the text.

### How to compile?

1. Get the content you want to be read in a PDF format.
2. Write the correct location of the PDF inside the brackets of 'open()' in the code.
   For example, here I have used sample.pdf so in the code it should be 'infile = open('Related/sample.pdf', 'rb')'.
3. Run the program.

### Use : 

* There are many recognized benefits of audiobooks that make them suitable for many situations.
* For instance, one can listen to audiobooks while driving, cleaning, walking, etc. and save a good amount of time.
* Many people love listening to audiobooks while multitasking.

### Conclusion :
This program helps the users to listen to PDFs rather than reading them and save time.

### Screenshots :
![running](https://user-images.githubusercontent.com/71630760/121780586-a8bb3d00-cbbe-11eb-9cf6-ebd9fa86f4aa.PNG)

### Author : Sonali Bedade


