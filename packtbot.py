#! /usr/bin/python3
import contextlib
import smtplib
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# email: l1020007@mvrht.com
# nombre: Antonio Hernandez
# contraseña: antoher

"""
go to https://www.packtpub.com/
click on class="login-popup"
email a id="email"
contraseña a id="password"
click on id="edit-submit-1"
go to https://www.packtpub.com/packt/offers/free-learning
click on: driver.findElement(By.cssSelector("value='Claim Your Free eBook'"))
click on first class="float-right toggle-product-line shown"
click on driver.findElement(By.cssSelector("format='pdf'"))
HANDLE THE DOWNLOAD... HARD
http://stackoverflow.com/questions/18009310/how-to-download-any-file-using-selenium-webdriver
"""

chrome_options = Options()
driver = webdriver.Chrome(chrome_options=chrome_options)

def browser_bot():
    try:
        driver.get("https://www.packtpub.com")
        popup_expand = driver.find_element_by_class_name("login-popup")
        popup_expand.click()
        print("Clicked the popup")
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
        )
        
        # email = driver.find_element_by_id("email")
        email = driver.find_element_by_css_selector('form#packt-user-login-form input[placeholder="E-mail address"]')
        print("Found email")
        driver.implicitly_wait(5)
        print("waited")
        driver.implicitly_wait(4)
        email.clear()
        email.send_keys("l1020007@mvrht.com")
        print("wrote email")
        
        driver.implicitly_wait(1)
        # password = driver.find_element_by_id("password")
        password = driver.find_element_by_css_selector('form#packt-user-login-form input[placeholder="Password"]')
        password.clear()
        password.send_keys("antoher")
        print("wrote password")
        driver.implicitly_wait(1)
        # driver.find_element_by_id("edit-submit-1").click()
        driver.find_element_by_css_selector('form#packt-user-login-form input[id="edit-submit-1"]').click()
        print("Clicked submit")
        driver.implicitly_wait(3)
        driver.get("https://www.packtpub.com/packt/offers/free-learning")
        driver.implicitly_wait(4)
        # scroll one page
        driver.execute_script("window.scrollBy(0, window.innerHeight)")
        #element = WebDriverWait(driver, 12).until(
        #EC.presence_of_element_located((By.CSS_SELECTOR, "value='Claim Your Free eBook'"))
        #)
        print("free ebook element present")
        # free_ebook = driver.find_element(By.CSS_SELECTOR, "value='Claim Your Free eBook'")
        free_ebook = driver.find_element_by_css_selector('input[value="Claim Your Free eBook"]')
        print("free ebook element almost clicked")
        free_ebook.click()

    except Exception as e:
        print(e)
        driver.quit()
    driver.quit()

# ChromeProfile.setPreference("browser.helperApps.neverAsk.saveToDisk","application/pdf,text/csv");
# developers@finametrix.com

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")
    msg = "YOUR MESSAGE!"
    server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
    server.quit()

if __name__ == '__main__':
    browser_bot()