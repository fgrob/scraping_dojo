from selenium import webdriver
driver = webdriver.Chrome('webdriver/chromedriver.exe')
driver.get('https://pythonspot.com')
driver.save_screenshot("screenshot.png")
driver.close()

options = Options()
options.headless = True
website = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
website.maximize_window()