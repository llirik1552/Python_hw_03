from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

award_element = wait.until(EC.presence_of_element_located((By.ID, "award")))
src = award_element.get_attribute("src")
print(src)

driver.quit()

