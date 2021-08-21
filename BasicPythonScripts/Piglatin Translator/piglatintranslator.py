# function to translate string s from english to pig latin
def englishtopiglatin(s):
    # splits string by words and passed into list
    s = s.lower().split(" ")
    result = ""

    # for every string in the list translate to pig latin through the formula before
    for string in s:
        
        if (len(string) <= 1):
            result += (string + "way")
        else:
            result += (string[1:] + string[:1] + "ay" + " ")
    
    # return new string
    return result

# print statements to run test cases
print("i love macaroni and cheese:", englishtopiglatin("i love macaroni and cheese"))
print("rudolph:", englishtopiglatin('rudolph'))
