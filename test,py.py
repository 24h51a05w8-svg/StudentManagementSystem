from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev")
priint("page Title:", driver.title)
assert "selenium" In driver.title
print("Test Passed")
driver.quit()