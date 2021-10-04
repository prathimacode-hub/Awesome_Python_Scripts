# Empty Folder Cleaner

## Aim/Purpose

Clear Empty Directories/Folders present in system

## Short description of package/script

- this script is menu driven program
- libraries imported are 
  - time
  - os
  - platform
- external modules -`None`

## Setup instructions
This script doesn't need any additional modules.
So you can run directly without any requirements other than Python itself(Duh.)
```cmd
cd Empty Folder Cleaner
python empty_folder_cleaner.py
```

## Detailed explanation of script

### This script has 3 options:   

- 1 Check the empty folders in curent path
- 2 Check the empty folder in given path by user
- 3 **This is important** See **NOTE**
    > it is used to change the text color. but on some computers dosen't works.
- Or write "exit" at any input for exiting.
- After using opt. 1 or 2 you will be asked to enter (Y/N) if you want to delete the Folders
- At end it would display 
     - `the no. of folder deleted`
     - `the no. of folders scanned`
     - `the no. of files and folders present.`
     - `Scanned dir path` 

## NOTE 

> **If getting any code like `03m[` on terminal then choose OPTION 3 in starting**

## Output 

<table >
  <tr>
    <td colspan=2 align=center>Starting Screen<img src= "Images/startScreen.jpg" alt="startScreen.jpg">↙↘ </td>
  </tr>
  <tr>
    <td rowspan=2>Option 1<img src= "Images/Option1.jpg" alt="Option1.jpg"></td>
    <td>Option 2<img src= "Images/Option2.jpg" alt="Option2.jpg"></td>
  </tr>
  <tr>
    <td>Process<img src= "Images/Option2process.jpg" alt="Option2process.jpg"></td>
  </tr>
  <tr>
    <td colspan=2 align=center>↙if↘</td>
  </tr>
  <tr>
    <td>Found Empty Folders<img src= "Images/foundEmpty.jpg" alt="foundEmpty.jpg"></td>
    <td>Not Found Empty Folders<img src= "Images/noEmpty.jpg" alt="noEmpty.jpg"></td>
  </tr>
  <tr>
    <td colspan=2 align=center>↘↙</td>
  </tr>
  <tr>
    <td colspan=2 align=center>End Screen<img src="Images/endScreen.jpg" alt="endScreen.jpg"></td>
  </tr>
</table>

## Author

[Dark Coder Cat | Vansh](https://github.com/dark-coder-cat)
