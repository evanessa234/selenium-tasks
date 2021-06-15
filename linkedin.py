from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
driver.maximize_window()

driver.find_element_by_xpath("//*[@name='session_key']").clear()
driver.find_element_by_xpath("//*[@name='session_password']").clear()

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "session_key"))).send_keys("your_email_here")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "session_password"))).send_keys("your_passsword_here")
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn__primary--large from__button--floating']"))).click()

driver.get('https://www.linkedin.com/feed/')
element = driver.find_element_by_link_text("Discover more")

actions = ActionChains(driver)
actions.move_to_element(element).click().perform()

