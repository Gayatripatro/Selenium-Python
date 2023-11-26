import pytest
from pages.example_page import ExamplePage
from utils.webdriver_factory import get_driver

@pytest.fixture
def browser():
    driver = get_driver()
    yield driver
    driver.quit()


def test_google_search(browser):
    page = ExamplePage(browser)
    browser.get("https://www.google.com/")
    page.search('pytest selenium')
    assert 'pytest' in browser.title.lower()


#@pytest.mark.amazon
def test_amazon_search(browser):
    page = ExamplePage(browser)
    browser.get("https://www.amazon.in/")
    page.amazon_search("tv 32 inchs")
    assert 'tv' in browser.title.lower()