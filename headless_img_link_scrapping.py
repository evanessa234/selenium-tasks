from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opts=webdriver.ChromeOptions()
opts.headless=True
driver = webdriver.Chrome(options=opts)
driver.maximize_window()

driver.get("https://wall.alphacoders.com/")

input_field = driver.find_element_by_xpath('//input[@class=\'search-bar form-control input-lg\']')
input_field.send_keys("apple")
input_field.send_keys(Keys.RETURN)

elements = driver.find_elements_by_class_name("img-responsive")
img_links = []
for element in elements:
    img_links.append(element.get_attribute("src"))
print(img_links)
