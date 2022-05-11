#!/usr/bin/env python3 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# login credentials 
email_address = "musiyarirajoshua@gmail.com"
psswd = "BeezApple13!!"

options = Options()
options.add_argument("start-maximized")

# allows script to be run without a GUI on a server
# options.headless = True 

class SCRAPE:

    def __init__(self, options):
        self.options = options
        

    def setup(self):
        """Setup for the chrome web driver."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
    

    def site_navigation(self):
        """Navigates to the webpage where friend requests are waiting approval"""
        driver = self.driver

        driver.get("https://www.penpalworld.com/friendsListAwait.asp")

        # accept cookies
        cookie_elem = driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]').click()

        # logging in and navigating to requests needing deletion 
        username = driver.find_element(By.XPATH, '//*[@id="strLogInEmail"]').send_keys(email_address)
        password = driver.find_element(By.XPATH, '//*[@id="passLogInPassword"]').send_keys(psswd)
        login_button = driver.find_element(By.XPATH, '//*[@id="contentWrap"]/div[1]/div[2]/form/fieldset/div/input').click()

        smart_safe_acceptance = driver.find_element(By.XPATH, '//*[@id="contentWrap"]/div[1]/form/div/input[1]').click()

    def delete_requests(self):
        """Deletes friend requests awaiting approval and then signs out"""
        driver = self.driver

        for i in range(25): # 711 requests / 29 requests deleted per page
            for cancel_button in range(29):
                try:
                    xpath = f'//*[@id="cancel{cancel_button}"]' 
                    # waiting .5 seconds prior to selctin
                    delete_req_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                    delete_req_button.click()

                # catches error where an object is not clickable, of which will occur once all requests have been deleted.
                except: 
                    print("All requests have been deleted.")    
                    sys.exit(1)

    def close_driver(self):
        """Closes the webdriver once all requests have been deleted"""
        self.driver.quit()           
            
def main():
    run = SCRAPE(options=options)
    run.setup()
    run.site_navigation()
    run.delete_requests()
    run.close_driver()

if __name__ == "__main__":
    main()

