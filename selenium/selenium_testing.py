from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait



def test_eight_components():


    driver = webdriver.Chrome()

    driver.get("https://opl.tmhp.com/")

    driver.implicitly_wait(10)
    
    def select_dropdown_by_value(dropdown_element, value):
        dropdown = Select(dropdown_element)
        dropdown.select_by_value(value)


    healthPlanDropdown = driver.find_element(by=By.NAME, value="HealthPlan")
    providerTypeDropdown = driver.find_element(by=By.NAME, value="ProviderGroupType")
    # zipInput = driver.find_element(by=By.NAME, value="ZipCode")

    select_dropdown_by_value(healthPlanDropdown, "10") 
    WebDriverWait(driver, 5)
    # select_dropdown_by_value(providerTypeDropdown, "5")

    # driver.execute_script("arguments[0].value = arguments[1]", zipInput, "73301")

    time.sleep(30)
    driver.quit()


test_eight_components()
