import contextlib
import smtplib
# from contextlib import contextmanager
from selenium import webdriver

from selenium.webdriver.common.by import By


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
driver = webdriver.Chrome()

def browser_bot():
    try:
        driver.get("https://www.packtpub.com")
        popup_expand = driver.find_element_by_class_name("login-popup")
        popup_expand.click()
        print("Clicked the popup")
        driver.implicitly_wait(4)
        email = driver.find_element_by_id("email")
        print("Found email")
        driver.implicitly_wait(5)
        print("waited")
        email.send_keys("l1020007@mvrht.com")
        print("Sent email")
        driver.implicitly_wait(1)
        password = driver.find_element_by_id("password")
        password.send_keys("antoher")
        driver.implicitly_wait(1)
        driver.find_element_by_id("edit-submit-1").click()
        driver.implicitly_wait(6)
        driver.get("https://www.packtpub.com/packt/offers/free-learning")
        free_ebook = driver.find_element(By.CSS_SELECTOR, "value='Claim Your Free eBook'")
        free_ebook.click()

    except Exception as e:
        print(e)
        driver.quit()
    driver.quit()

# ChromeProfile.setPreference("browser.helperApps.neverAsk.saveToDisk","application/pdf,text/csv");


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("YOUR EMAIL ADDRESS", "YOUR PASSWORD")
    msg = "YOUR MESSAGE!"
    server.sendmail("YOUR EMAIL ADDRESS", "THE EMAIL ADDRESS TO SEND TO", msg)
    server.quit()

if __name__ == '__main__':
    browser_bot()