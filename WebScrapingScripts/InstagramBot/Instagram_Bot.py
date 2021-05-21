from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
from cred import username as usr, password as psw


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return True

    return False


def random_comment():
    with open(r'comments.txt', 'r') as f:
        commentsl = [line.strip() for line in f]
    comments = commentsl
    comment = random.choice(comments)
    return comment


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        with open(r'tags.txt', 'r') as f:
            tags1 = [line.strip() for line in f]
        self.tags = tags1
        self.urls = []

    def exit(self):
        bot = self.bot
        bot.quit()

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com/')
        time.sleep(3)

        username_f = WebDriverWait(bot, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password_f = WebDriverWait(bot, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        username_f.clear()
        username_f.send_keys(self.username)
        password_f.clear()
        password_f.send_keys(self.password)
        login_button = WebDriverWait(bot, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()
        time.sleep(4)
        try:
            not_now = WebDriverWait(bot, 6).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')))
            not_now.click()
            time.sleep(2)
        except:
            print("no pop up 1")

        try:
            not_now2 = WebDriverWait(bot, 6).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.aOOlW:nth-child(2)')))
            not_now2.click()
            time.sleep(2)
        except:
            print("no pop up 2")
        time.sleep(4)

    def get_post(self):
        print("Searching posts by tags....")
        bot = self.bot
        tags = self.tags
        tag = tags.pop()

        # generating the link
        link = 'https://www.instagram.com/explore/tags/' + tag
        bot.get(link)

        time.sleep(4)
        for i in range(4):
            ActionChains(bot).send_keys(Keys.END).perform()
            time.sleep(2)

        divs = bot.find_elements_by_xpath("//a[@href]")

        first_urls = []

        for i in divs:
            if i.get_attribute('href') is not None:
                first_urls.append(i.get_attribute('href'))
            else:
                continue

        for url in first_urls:
            if url.startswith('https://www.instagram.com/p/'):
                self.urls.append(url)
        return go.comment(random_comment())

    def comment(self, comment):

        if len(self.urls) == 0:
            print('Finished tag jumping to next one...')
            return go.get_post()

        bot = self.bot
        url = self.urls.pop()
        print('commenting...')
        bot.get(url)
        bot.implicitly_wait(1)

        bot.execute_script("window.scrollTo(0, window.scrollY + 300)")
        time.sleep(2)

        bot.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()
        time.sleep(2)

        bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button').click()

        if check_exists_by_xpath(bot, '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div'):
            print("skiped")
            return go.comment(random_comment())

        #find_comment_box = WebDriverWait(bot, 6).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')))
        print("yes")
        #find_comment_box.click()
        #find_comment_box.clear()
        c = bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").click()
        #commentb = WebDriverWait(bot, 6).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')))
        print("yes2")
        c2 = bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
        c2.send_keys(comment)

        post_btn = WebDriverWait(bot, 6).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]')))
        post_btn.click()
        # edit this line to make bot faster
        time.sleep(5)
        # ---------------------------------

        return go.comment(random_comment())






go = Bot(usr, psw)
go.login()
if __name__ == '__main__':
    if go.tags == []:
        print("Finished")
    else:
        go.get_post()
