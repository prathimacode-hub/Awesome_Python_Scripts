# <p align = "center"> Website Blocker using PC Hosts files </p>
## Introduction: 
This is a script that aims to implement a website blocking utility for Windows-based systems. It makes use of the computer's hosts files and runs it as a background process, preventing access to the sites entered by the user in list format.
## Third-party libraries required:
The project requires Python's datetime library only
## Importing the Libraries:
Open Command Prompt on your computer and type the following:
On the script's console, type: <br>
`import time` <br>
`from datetime import datetime as dt`

## Running the Script:
After opening the script in your Python IDE, execute the code so that you get the UI output window. Open your browser and try to visit the websites you blocked. When the script runs successfully, you will see `This site can't be reached` error or similar 404 error's on the browser.

**Note:**
> In some systems, access to the computers's hosts files maybe denied by default to prevent malware attacks. So the script while executing may show an error while modifying the hosts files. 
> Please visit [here](https://www.technipages.com/windows-access-denied-when-modifying-hosts-or-lmhosts-file) for a brief readup on how to solve the issue.

> *Recommended:* Please revert to the original access settings after testing the script to prevent any future compromise

## Output:
#### The output UI will appear as shown below:
![Output 1](https://raw.githubusercontent.com/Rutuj-Runwal/Img/master/assets/UI1.png?token=AOFO32AFMK2ZEB3T4IKLGW3AZ6G6Q)
#### You can add new site as shown below then click on "Add Website" button.You can add as many as you want:
![Output 2](https://raw.githubusercontent.com/Rutuj-Runwal/Img/master/assets/UI2.png?token=AOFO32GHV3ZGY7QR27FDTA3AZ6HIE)
#### If you entered anything that's not a proper website.An error willshow up to guide you:
![Output 3](https://raw.githubusercontent.com/Rutuj-Runwal/Img/master/assets/UI3.png?token=AOFO32A2EMFCJ2WLIA7WCGTAZ6HNC)

#### Once you are done with adding websites, you canclick on Block-Sites button to begin blocking