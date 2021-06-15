from selenium import webdriver

query = input("Enter the query : ")
opts=webdriver.ChromeOptions()
opts.headless=True
driver = webdriver.Chrome(options=opts)
driver.get("http://www.google.com")
driver.maximize_window()
element = driver.find_element_by_name("q")
element.send_keys(query)
element.submit()

elements = driver.find_elements_by_xpath('//div[@class="tF2Cxc"]')
a = []
for element in elements:
    sub_a = {}
    title = element.find_element_by_xpath('.//h3').text
    link = element.find_element_by_xpath('.//div[@class="yuRUbf"]/a').get_attribute('href')
    sub_a["title"] = title
    sub_a["link"] = link
    try:
        detail = element.find_element_by_xpath('.//div[@class="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc"]').text
        sub_a["description"] = detail
    except:
        pass
    a.append(sub_a)
print(a)
