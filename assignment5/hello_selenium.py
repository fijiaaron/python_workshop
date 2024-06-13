from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://selenium.dev")
print(driver.title)
assert driver.title == "selenium"