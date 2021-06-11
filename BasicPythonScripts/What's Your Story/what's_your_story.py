import random
# random module comes pre-installed with python

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
went = ['cinema', 'university','seminar', 'school', 'laundry', 'asylum', 'cave', 'mall', 'disneyland']
happened = ['made a lot of friends','ate a pizza', 'found a secret key', 'solved a mystery', 'wrote a book','stole ice cream','ate a lot of cakes']
who = ['Hulk', 'Iron Man', 'Batman', 'Superman', 'Captain America', 'Spiderman']
desc = ['I met a good human being named ', 'I met my friend ', 'the person I met through social media, ']
cartoon = ['Spongebob','Doraemon','Shinchan','Minions','Mickey']
action = ['played hide and seek','clicked selie','had coffee']
end = ['We rode our unicorns back home.', 'We flew back on home on our broomstick.', 'An eagle dropped us home.']
# here we declare some lists which will help us to build our story


name = [item for item in input("What is your good name ?? ").split()]
friend = [item for item in input("What is your friend's name ?? ").split()]
place = [item for item in input("Where are you from ?? ").split()]
tour = [item for item in input("Any favourite destination ?? ").split()]
# name, place, favorite destination is taken from the user

print("\n")
print('Hello, I am '+random.choice(name)+'. '+random.choice(when) + ', ' + random.choice(desc) + random.choice(friend) + ' who lives in ' + random.choice(place) + '. We made plans to go to '+random.choice(tour)+' with '+random.choice(who)+'. Then we went to the ' + random.choice(went) + ' and ' + random.choice(happened)+'. We '+random.choice(action)+' with '+random.choice(cartoon)+'. '+random.choice(end))