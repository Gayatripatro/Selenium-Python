import pytest
from utils.webdriver_factory import get_driver

@pytest.fixture
def browser():
    driver = get_driver()
    yield driver
    driver.quit()
