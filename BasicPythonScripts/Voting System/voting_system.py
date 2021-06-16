#two nominees for election
nominee_1 = input("Enter the name of Nominee_1 : ")
nominee_2 = input("Enter the name of Nominee_2 : ")

nom_1_votes = 0
nom_2_votes = 0

#assigning voting ids
votes_id = [1,2,3,4,5,6,7,8,9,10]

num_of_voter = len(votes_id)

#checking voting id if it is correct then allowing voter to vote and if already voted it will show already done
while True:
    if votes_id==[]:
        print("voting session is over")
        if nom_1_votes>nom_2_votes:
            percent=(nom_1_votes/num_of_voter)*100
            print(nominee_1," has won with ",percent,"% votes")
            break
        elif nom_2_votes>nom_1_votes:
            percent=(nom_2_votes/num_of_voter)*100
            print(nominee_2," has won with ",percent,"% votes")
            break
    else:
        voter = int(input("Enter your voter id no. : "))
        if voter in votes_id:
          print("You are a voter!!!")
          votes_id.remove(voter)
          vote = int(input("Enter your vote 1 or 2 : "))
          if vote ==1:
            nom_1_votes+=1
            print("Thank You for casting your vote")
          elif  vote ==2:
            nom_2_votes+=1
            print("Thank You for casting your vote")
        else:
         print("You are not a voter here or else you have already voted")