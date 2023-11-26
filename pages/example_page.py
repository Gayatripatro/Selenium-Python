from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ExamplePage(BasePage):
    # Locators
    SEARCH_BOX = (By.XPATH, "//textarea[@id='APjFqb']")
    SELECT_DATA = (By.XPATH, "(//div[@class='lnnVSe'])[1]")
    SEARCH_BUTTON = (By.XPATH, "(//input[@name='btnK'])[2]")

    AMAZON_SEARCH_BOX = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    AMAZON_SEARCH_BUTTON = (By.XPATH, "//input[@id='nav-search-submit-button']")

    def search(self, query):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(query)
        self.driver.find_element(*self.SELECT_DATA).click()
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def amazon_search(self,testdata):
        self.driver.find_element(*self.AMAZON_SEARCH_BOX).send_keys(testdata)
        self.driver.find_element(*self.AMAZON_SEARCH_BUTTON).click()
