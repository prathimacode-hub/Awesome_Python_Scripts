from selenium import webdriver

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(r"Enter the path of your selenieum webdriver")
    
    def play(self,query):
        self.query = query
        self.driver.get(url = "https://www.youtube.com/results?search_query="+query)
        video = self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        video.click()

