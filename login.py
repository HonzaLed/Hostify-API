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

    driver.find_element(by=By.CLASS_NAME, value="custom-control-label").click()

    while driver.current_url == "https://admin.hostify.cz/login":
        #print("[DEBUG] Waiting!")
        time.sleep(1)

    driver.get("https://gql.hostify.cz/gql")
    session = driver.get_cookie("session")
    driver.close()
    return session

"""
PACKAGE CONTENTS
    chrome (package)
    chromium (package)
    edge (package)
    firefox (package)
    ie (package)
    opera (package)
    safari (package)
"""