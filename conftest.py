import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import allure

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--headless', action='store_true',
                     help='Run tests in headless mode')

@pytest.fixture(scope='function')
def driver(request):
    browser_name = request.config.getoption('browser')
    headless = request.config.getoption('headless')
    
    if browser_name == 'chrome':
        options = ChromeOptions()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        options = FirefoxOptions()
        if headless:
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser should be chrome or firefox')
    
    driver.implicitly_wait(5)
    driver.maximize_window()
    
    yield driver
    
    if request.node.rep_call.failed:
        try:
            allure.attach(
                driver.get_screenshot_as_png(),
                name='screenshot_on_failure',
                attachment_type=allure.attachment_type.PNG
            )
        except:
            pass
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
