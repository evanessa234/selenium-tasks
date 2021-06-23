from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, datetime

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
actions = ActionChains(driver)

driver.get("https://operaduomofirenze.skiperformance.com/en/store#/en/buy")

## closing cookies request ....................
## element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sitcookies"]/button')))
## element.click()
def click_xpath_element(xpath: str) -> str:
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        print("No such element : {}".format(xpath))
        exit()
    else:
        # actions.move_to_element(element).click().perform()
        element.click()
        return element

# checking available product .............
def click_link_element(link_text: str) -> bool:
    try:
        # element = driver.find_element_by_link_text(link_text)
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
    except:
        print("No such element : {}".format(link_text))
        exit()
    else:
        element.click()
        # actions.move_to_element(element).click().perform()
        # except:
        #     print("{} : not interactable".format(link_text))
        #     exit()

def product_existence(product_type: str, product_name: str) -> bool:
    try:
        click_link_element("Products")
        print("1 click")
        time.sleep(4)
        click_link_element(product_type)
        print("2 click")
        click_link_element(product_name)
        print("3 click")
        return True
    except:
        return False

# Checking datetime availabilty ..............
def is_datetime_valid(datetime_str: str) -> datetime:
    try:
        date_time_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    except:
        print("Wrong datetime or format")
        exit()
    else:
        now = datetime.now()
        if (date_time_obj >= now):
            print("We are good to go")
            return date_time_obj
        else:
            print("selected datetime has already passed")
            exit()

def month(valid_date: datetime) -> str:
    return valid_date.strftime("%B")

def day(valid_date: datetime) -> str:
    return valid_date.day

def get_time(valid_date: datetime) -> str:
    return valid_date.time()

# date picker ...................
def calender_page(valid_date: datetime):
    click_xpath_element("//input[@id='js-validity_start-p_5131']")
    title_month = month(datetime.today())
    title_year = datetime.today().year
    req_month = month(valid_date)
    req_year = str(valid_date.year)
    while not (title_month == req_month and title_year == req_year):
        try:
            click_xpath_element("//div[@id='zs-ui-datepicker-div']//span[@class='zs-ui-icon zs-ui-icon-circle-triangle-e'][normalize-space()='Next']")
        except:
            print("Date out of booking range")
            exit()
        else:
            title_date = click_xpath_element("//div[@id='zs-ui-datepicker-div']//div[@class='zs-ui-datepicker-title']").text
            title_month = title_date.split(" ")[0]
            title_year = title_date.split(" ")[1]

def select_date(valid_date: datetime):
    try:
        click_link_element(str(valid_date.day))
    except:
        print("Date not available")
        exit()

def date_picker(valid_date: str):
    calender_page(valid_date)
    select_date(valid_date)


click_xpath_element("//*[@id='site-cookies']/button")
valid_date = is_datetime_valid("2021-12-29 19:39:19")
product_existence("Tickets", "Brunelleschi's Dome")
time.sleep(5)
date_picker(valid_date)


# ele = click_xpath_element("//div[@id='zs-ui-datepicker-div']//table[@class='zs-ui-datepicker-calendar']")
# print("yes")
# click_link_element(str(valid_date.day))
# elem = driver.find_element_by_link_text('30')
# actions.move_to_element(elem).click().perform()
# //*[@id="zs-ui-datepicker-div"]/table/tbody/tr[5]/td[3]/a
# try:
    # click_xpath_element("//a[normalize-space()='{}']".format(24))
    # click_link_element(str(valid_date.day))
    # click_xpath_element("//a[normalize-space()='14']")
# except:
    # print("Date not available")
    # l = driver.find_element_by_xpath("//div[@id='zs-ui-datepicker-div']//table[@class='zs-ui-datepicker-calendar']")
    # driver.execute_script("arguments[0].scrollIntoView(true);", l)
    # time.sleep(6)
    # # click_xpath_element("//a[normalize-space()='{}']".format(valid_date.day))
    # click_link_element(str(valid_date.day))
    # print("Scrolled and selected date")
    # //*[@id="zs-ui-datepicker-div"]/table/tbody/tr[5]/td[7]/a
# dateelem = driver.find_element_by_xpath("//a[normalize-space()='{}']".format(30))
# l = driver.find_element_by_xpath("//div[@id='zs-ui-datepicker-div']//table[@class='zs-ui-datepicker-calendar']")
# click_xpath_actions_element("//a[normalize-space()='{}']".format(valid_date.day))
# actions.move_to_element(dateelem).click().perform()
# driver.execute_script("arguments[0].scrollIntoView(true);", l)
# print("no")
# //*[@id="buy_scroller"]/div/div[2]/div[2]/div/form/div/div[3]/div[2]/div[3]/div[3]/fieldset/div[1]/div[2]/input
# //*[@id="zs-ui-datepicker-div"]/table/tbody/tr[5]/td[7]/a
# rows = ele.find_elements_by_tag_name("tr")
# columns = ele.find_elements_by_tag_name("td")
# for cell in columns:
#     element = cell.text
#     # print(str(valid_date.day))
#     print(element)
#     if element == '23':
#         cell.click()
#         break
#     else:
#         pass

# elem = driver.find_element(By.XPATH, "//div[@id='zs-ui-datepicker-div']")
# elem.click()

# time.sleep(4)
# elem = driver.find_element_by_name("sku_qty_20410")
# elem.send_keys(1)
#     # if cell.text == 25:
#     #     cell.find_element_by_link_text('25').click()
#     # //*[@id="buy_scroller"]/div/div[2]/div[2]/div/form/div/div[3]/div[2]/div[1]/div[3]/fieldset/div[1]/div[2]/input

# elements = driver.find_elements_by_class_name("gc xs-gc12 pointer js-booking-clickable")


# # selecting product type ..............
# b = By.XPATH
# c = 'Tickets'
# mypath = "//a[contains(@class,'tab-link bold xs-text-20 lg-text-16')][normalize-space()='{}']".format(c)
# myelem = driver.find_element(b, mypath)
# myelem.click()
# time.sleep(4)


# # find if product name exists...............
# elements = driver.find_element(By.CLASS_NAME, "xs-width-full xs-width-fit")
# available_product_names = []
# for element in elements:
#     product_name = element.find_element_by_xpath('.//h3').text
#     available_product_names.append()
# print(available_product_names)


# Sign up code chunk .....................

# driver.find_element_by_link_text("Sign in").click()

# time.sleep(5)
# myButton = driver.find_element_by_xpath("//header/div[@id='interfacecontainerdiv']/a[2]")
# myButton.click()
# time.sleep(4)
# parent = driver.window_handles[0]
# chwnd = driver.window_handles[1]
# driver.switch_to.window(chwnd)

# driver.find_element_by_xpath("//input[@type='email']").send_keys("teammetry5@gmail.com")
# driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/div/button/span").click()
# time.sleep(4)
# passwordElem = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
# passwordElem.send_keys('test@321')
# signinButton = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
# signinButton.click()

# driver.switch_to.window(parent)
# time.sleep(10)


# driver.find_element_by_xpath("//body/div[@id='js-multi_modal_container']/div[@id='modal_content']/div[@id='modal-layout']/div[1]/div[1]/div[1]/form[1]/fieldset[1]/label[1]").click()

# driver.find_element_by_xpath("//button[contains(text(),'Accept')]").click()



