from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://discord.com/login')
user = driver.find_element_by_xpath('//input[@name=\'email\']').send_keys("your_email_here")

pwd = driver.find_element_by_xpath('//input[@name=\'password\']')
pwd.send_keys("your_password_here")

login = driver.find_element_by_xpath('//button[@class=\'marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN\']')
login.click()


