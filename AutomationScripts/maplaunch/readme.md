# maplauncher
python script utilising pyperclip,sys and webbrowser module script.

This code can read commandline arguments from sys.argv and read clipboard contents

webbrowser.open() function is used here to open the browser.

when you run it if you dont enter arguments into he command line it will automatically read from the clipboard.

 tip:<br>
    by doing the stuff below you can launch the program just by entering "maps new delhi" or "maps wall st new york NY USA" and it will load the location.<br>
    write the following into a notepad and save it with .bat extention:<br>
              @py.exe c:/enter the location of your python script here> %*                           
              @pause<br>
  add the location of the folder in which you saved the bat file to your environment variable.<br>
  now you can either copy a location and enter map into cmd or enter location in to the cmd after maps to load your map<br>
  

