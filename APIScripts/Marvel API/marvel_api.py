from marvel import  Marvel
m=Marvel("","")#write public and private keys here
characters=m.characters
#for getting all info from id
all_characters=characters.all()
#getting information of consecutive six characters by id
x=1011334
for n in range(0,6):
    all_characters=characters.comics(x)
    x=x+1
    #for getting output in proper format
    for i in range(1,12):
        print(all_characters['data']['results'][int(i)]['title'])



