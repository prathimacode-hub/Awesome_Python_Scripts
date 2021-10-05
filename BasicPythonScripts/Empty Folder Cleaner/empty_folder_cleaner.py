#code written by @dark-coder-cat at github
#to run empty_folder_cleaner.py on android use pydroid3(any others may also work)

import os
import time
import platform as pf


# data
notPermissioned = ('Android/data', 'Android/obb')
sys = pf.system()
init = ''
rem = '/storage/emulated/0/'
fNum = allNum = 0
empty, notDel = [], []
startTime = 0
rmPre= lambda s: s.replace(rem,'')

# COLORS
RED = '\033[1;31;40m'
WHITE = '\033[0;38;48m'
INVERT = '\033[3;37;40m'
BRIGHT = '\033[1;37;40m'

#----------FUNCTIONS----------#

# Clears Screen
def cls():
    if sys == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# Check The given directory and sub directories
def checkDir(path, rem):
    global fNum, allNum
    try:
    	for item in os.listdir(path):
            item = os.path.join(path, item)
            allNum += 1
            if os.path.isdir(item) and not item.endswith(notPermissioned) :
                print(rmPre(item))
                fNum += 1
                if not os.listdir(item):
                    empty.append(rmPre(item))
                else:
                    checkDir(item, rem)
                    checkBack(item,rem)
    except:
            pass
            
                                  
# Check the pervious directory
def checkBack(path,rem):
	if all(rmPre(os.path.join(path,item)) in empty for item in os.listdir(path)):
		empty.append(rmPre(path.replace(rem,'')))
		

# Starts again if error or wrong input
def startAgain(show=False):
    cls()
    if show:
        print(BRIGHT+show, '\n')
    start()


#Ending Info about files/folders.
def endInfo(string, dir, noDEL=True):
    try:
        if noDEL: noDEL=len(empty)
        s = lambda num: "s" if num > 1 else ""
        pad = lambda num: ' ' * \
            (len(str(max(noDEL, fNum, allNum))) - len(str(num)) + 1)

        showNums = lambda pad, n, pr: print('\n',BRIGHT, n, WHITE, pad(n), pr, sep='', end='')
        showNums(pad, noDEL, f'Empty folder{s(len(empty))} {string}')
        showNums(pad, fNum, f'Total folder{s(fNum)} Scanned.')
        showNums(pad, allNum, f'Total file{s(allNum)} and folder{s(allNum)}.')
        print(f'\n{BRIGHT}Scanned Folder:{WHITE}{dir}')
    except:
        input("Crashed")


# Show List
def showList(s,l):
    print(f'{BRIGHT}{s} Folders:\n{WHITE}',end='')
    listLen=len(l)
    pad = lambda n : (len(str(listLen))-len(str(n)))*' '
    for i in range(listLen):
        item = l[i]
        print(BRIGHT,i+1,')',pad(i+1),WHITE,item,sep='')
    if not l: print("None")


#Delete
def delete(dir):
	nDel=0
	print(f'\n{BRIGHT}Deleted Folders:\n{WHITE}')
	for i,e in enumerate(empty,1):
	   try:
	   	path = init+e
	   	os.rmdir(path)
	   	nDel+=1
	   	print(BRIGHT, i,') ', 
	   	    WHITE, path, RED+'-----Removed!!!'+WHITE,sep='')
	   except:
	   	notDel.append(path)
	if not nDel: print("None Deleted")
	showList('\nUnable to delete',notDel)
	endInfo('Deleted!!',dir,nDel)


# Start
def start():
    global init, startTime
    global RED, WHITE, INVERT, BRIGHT
    option = input(
        f'{BRIGHT}Empty Folder Cleaner.\n\n\
Choose Your option:\n\
1.{WHITE} Check the empty folders in curent path\n{BRIGHT}\
2.{WHITE} Check the empty folder in given path by user\n\
Or write "exit" at any input for exiting.\n\
{INVERT}After checking you will be asked to enter (Y/N) if you want to delete the Folders.{WHITE}\n\
{BRIGHT}IF GETTING ANY CODE LIKE <03m[> ON TERMINAL THEN CHOOSE OPTION 3\n\n\
{BRIGHT}Enter your option:{WHITE} ').lower()
    print()
    
    if option == 'exit': return False
    elif option == '1':
        path = os.getcwd()
    elif option == '2':
        print(f"{RED}NOTE ! - If given none then would scan the internal storage(Android).{WHITE}")
        path = input(f'{BRIGHT}Enter path to scan and delete empty folders: {WHITE}')
        if path == 'exit': return False
        if sys == 'Linux': init = rem
        if not os.path.exists(init+path):
            startAgain('The Path does not exit.\nTry again')
            return
        elif sys == 'Windows' and path.endswith('\\') and path.endswith('//'):
            path += '\\'
    elif option == '3':
        RED = WHITE = INVERT = BRIGHT = ''
        startAgain('')
        return
    else:
        startAgain('Wrong Option')
        return

    startTime = time.time()
    dirPath = init+path
    checkDir(dirPath, rem)
    
    cls()
    showList('Empty',empty)
    
    if empty:
        toDel = input(f'\n{BRIGHT}Do you want to delete these?(Y/N): {WHITE}').upper()
        if toDel=='Y':
            delete(dirPath)
    else:
        endInfo('found.',dirPath)

    return True


# Run
def main():
    cls()
    showTime=start()
    if showTime:
        _ = input(
            f'\n\n{INVERT}[Took {round(time.time()-startTime,2)}s in executing]{WHITE} \nPress Enter to Exit.')
    
if __name__=="__main__":
    main()
