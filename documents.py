from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from sys import platform
import re 
"""
Courtesy from scraper.ipynb by Bhavya
"""


# pip install bs4 selenium
class JavaScript_scrape():
     
    """
    scrapping javascript based website
    """

    def get_js_soup(self, url):
        """
        uses webdriver object to  generate the first 10 results ( first page)
        execute javascript code and get dynamically loaded webcontent
        """
        # create a webdriver object and set options for headless browsing
        options = Options()
        options.headless = True
        options.page_load_strategy = 'eager'

        #skip information that's only valuable for human beings
        prefs = {"profile.managed_default_content_settings.images":2,
         "profile.default_content_setting_values.notifications":2,
         "profile.managed_default_content_settings.stylesheets":2,
         "profile.managed_default_content_settings.cookies":2,
         "profile.managed_default_content_settings.javascript":1,
         "profile.managed_default_content_settings.plugins":1,
         "profile.managed_default_content_settings.popups":2,
         "profile.managed_default_content_settings.geolocation":2,
         "profile.managed_default_content_settings.media_stream":2,
        }
        options.add_experimental_option("prefs",prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        #chrome driver version and system
        driver_version = "95.0.4638.69"
        driver_os = "mac"

        if platform == "linux" or platform == "linux2":
            # linux
            driver_os = "linux"

            #added for cloud containers
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
        elif platform == "darwin":
            # OS X
            driver_os = "mac"
        elif platform == "win32":
            # Windows...
            driver_os = "windows"

        
        #set up the chrome driver
        s = Service(f'./chromedriver' + '-' + driver_version + '-' + driver_os)
        driver = webdriver.Chrome(service = s, options=options)
        driver.get(url)
        res_html = driver.execute_script("return document.body.innerHTML")
        soup = BeautifulSoup(res_html, 'html.parser')  # beautiful soup object to be used for parsing html content
        driver.quit()
        
        #remove script and style
        for script in soup(["script", "style"]):
            script.decompose()

        return soup     

    def process_text(self, text):
        text = text.encode('ascii',errors='ignore').decode('utf-8')       #removes non-ascii characters
        text = re.sub('\s+',' ',text)       #repalces repeated whitespace characters with single space
        return text 

    def scrape_websites(self):
        """
        extracts newest articles from medical news today
        """
        links = []
        documents = []
        url_txt = 'links.txt'
        with open(url_txt) as f:
            for line in f:
                base_url = line.rstrip()
               # scrape to find news links in the base url
                soup = self.get_js_soup(base_url)
                text_section = soup.find("section", {"id": "main-content"})
                if text_section is not None:
                    links.append(base_url)
                    documents.append(self.process_text(text_section.get_text(separator=' ')))
        return documents, links 

if __name__ == '__main__':
    counter = 0
    items = JavaScript_scrape().scrape_websites()
    counter+= len(items)
    '''
    items = JavaScript_scrape().scrape_medscape(limit=-1,output='elasticsearch')
    counter+= len(items)
    items = JavaScript_scrape().scrape_aapNews(limit=-1,output='elasticsearch')
    counter+= len(items)
    items = JavaScript_scrape().scrape_medicalNewsToday(limit=-1,output='elasticsearch')
    counter+= len(items)'''
    
    print(items)