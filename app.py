#!/usr/bin/env python3 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import param_store, time



# login credentials read from parameter store
email_address = param_store.get_email() 
psswd = param_store.get_password()

# chrome driver options 
options = Options()
# options.headless = True # allows script to be run without a GUI on a server

class SCRAPE:

    def __init__(self, options):
        self.options = options
        

    def setup(self):
        """Setup for the chrome web driver."""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
    

    def site_navigation(self):
        """Navigates to the webpage where friend requests are waiting approval"""
        driver = self.driver

        driver.get("https://www.penpalworld.com/friendsListAwait.asp") # webpage containing requests to be deleted 
        
        privacy_acceptance = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]'))).click()
        username = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="strLogInEmail"]'))).send_keys(email_address)
        password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="passLogInPassword"]'))).send_keys(psswd)
        login_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contentWrap"]/div[1]/div[2]/form/fieldset/div/input'))).click()
        smart_safe_acceptance = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="contentWrap"]/div[1]/form/div/input[1]'))).click()
        


    def delete_requests(self):
        """
        Deletes friend requests awaiting approval and then signs out.
        Closes the webdriver once all requests have been deleted
        """
        driver = self.driver

        while True: 
            try: 
                time.sleep(3) # explicit wait required as script kept failing after deleting a few requests. 
                delete_req_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cancel1"]'))).click() # iteratively selecting the same xpath
                driver.get("https://www.penpalworld.com/friendsListAwait.asp") # reopens awaiting friend requests URL and refreshes the page after each delete request
                driver.refresh()
            except:
                driver.quit()
            
def main():
    run = SCRAPE(options=options)
    run.setup()
    run.site_navigation()
    run.delete_requests()
   

if __name__ == "__main__":
    main()

