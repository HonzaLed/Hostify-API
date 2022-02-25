from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def initialize_browser():
    try:
        return webdriver.Firefox()
    except:
        try:
            return webdriver.Chrome()
        except:
            try:
                return webdriver.Chromium()
            except:
                try:
                    return webdriver.Edge()
                except:
                    try:
                        return webdriver.Safari()
                    except:
                        try:
                            return webdriver.Opera()
                        except:
                            try:
                                return webdriver.Ie()
                            except:
                                raise Exception("No compatible browser found!")
def getSession():
    driver = initialize_browser()
    driver.get("https://admin.hostify.cz/login")
    while driver.current_url == "https://admin.hostify.cz/login":
        time.sleep(1)
    driver.get("https://gql.hostify.cz/gql")
    session = driver.get_cookie("session")
    driver.close()
    return session["value"]
