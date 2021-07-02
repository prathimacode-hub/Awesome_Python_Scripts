
from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("yoda.jpg", caption="biscuit eating baby")

######  follow someone #######
bot.follow("elonrmuskk")

######  send a message #######
bot.send_message("Hello from Neel", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("username")
for follower in my_followers:
    print(follower)

#### we can unfollow everyone ###
bot.unfollow_everyone()