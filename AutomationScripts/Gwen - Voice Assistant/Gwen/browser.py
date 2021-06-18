from selenium import webdriver

class info():
    def __init__(self):
        self.driver = webdriver.Chrome(r'Enter the path of your selenieum webdriver')
    
    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://www.google.com/")
        search=self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        enter.click()

        try:
            txt=self.driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div[1]/div/div/div/div/span[1]').text
            return txt
        except:
            pass
        try:
            txt2=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[2]/div/span[1]/span').text
            return txt2
        except:
            pass
        try:
            txt3=self.driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').text
            txt4=self.driver.find_element_by_xpath('//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[2]').text
            return txt3+" "+txt4
        except:
            pass
        try:
            txt5=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[1]/div/span/span').text
            return txt5
        except:
            pass
        try:
            txt6=self.driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div[2]/div/div/div[3]/div/div/div/div/span').text
            return txt6
        except:
            pass

        try:
            txt6=self.driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div[1]/div/div/div/div/span[1]').text
            return txt6
        except:
            pass

        try:
            txt6=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[2]/div/span/span').text
            return txt6
        except:
            pass

        