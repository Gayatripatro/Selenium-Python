from selenium import webdriver


def get_driver():
    # Specify the path to your chromedriver executable
    chrome_driver_path = "C:\\Gayatri\\Software\\chromedriver_win32\\chromedriver.exe"
    return webdriver.Chrome()