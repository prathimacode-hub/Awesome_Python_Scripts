from time import time
#definig function errors which will calculate the accuracy
global correct
def Errors(prompt):

    words = prompt.split()
    errors = 0
   #splitting thw words to get error 
    for i in range(len(correct)):
        if i in (0, len(correct)-1):
            if correct[i] == words[i]:
                continue
            else:
                errors +=1
        else:
            if correct[i] == words[i]:
                if (correct[i+1] == words[i+1]) & (correct[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

#Speed function to calculate number of words written per unit time(minute)
def Speed(iprompt, starttime, endtime):
    global time
    global correct

    correct = iprompt.split()
    twords = len(correct)
    speed = twords / time

    return speed

#Time function to calculate amount of time taken by user
def timeElapsed(startime, endtime):
    time = endtime - starttime

    return time

if __name__ == '__main__':
    prompt = "Hi, my name is Neel Shah, I am a python lover."
    print("Type this:- '", prompt, "'")

    input("press ENTER when you are ready!")

   #Gathering all the data
    starttime = time()
    iprompt = input()
    endtime = time()
    time = round(timeElapsed(starttime, endtime), 2)
    speed = Speed(iprompt, starttime, endtime)
    errors = Errors(prompt)

    # printing all the required data
    print("Total Time elapsed : ", time, "s")
    print("Your Average Typing Speed was : ", speed, "words / minute")
    print("With a total of : ", errors, "errors")
