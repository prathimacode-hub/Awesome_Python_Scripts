def main():
    print(" Enter the marks of English Hindi Math Science S.St Computer ")  # subject name
    subjects = ["English ", "Hindi", "Math ", " Science", " S.St ", " Computer "]
    marks = []  # defining the marks variable
    total = 0  # initializing the variable

    # Taking inputs one by one
    for i in range(6):  # Iteration of loop
        j = i
        print(" Enter the Marks of ", subjects[j], end=" ")
        marks.insert(i, input())  # Taking inputs marks one by one
        
    # Adding the markks
    for i in range(6):
        total = total + int(marks[i])
    print(" Total marks Marks = ", total, " and ", end=" ")
    average = total / len(subjects)
    # Condition checking for grade

    if average >= 91 and average <= 100:
        print(" Grade is A1")
    elif average >= 81 and average <= 90:
        print(" Grade is A2")
    elif average >= 71 and average <= 80:
        print(" Grade is B1")
    elif average >= 61 and average <= 70:
        print(" Grade is B2")
    elif average >= 51 and average <= 60:
        print(" Grade is C1")
    elif average >= 41 and average <= 50:
        print(" Grade is C2")
    elif average >= 33 and average <= 40:
        print(" Grade is D")
    elif average >= 21 and average <= 32:
        print(" Grade is E1")
    elif average >= 0 and average <= 20:
        print(" Grade is E2")
    else:
        print("Inputs are not valid Kindly Give Correct Input")

    choice = int(input(" Enter 1 to continue and else to exit "))
    if choice == 1:
        main()
    else:
        exit()


main()
