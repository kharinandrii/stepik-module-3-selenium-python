import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en', help="choose language")



@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        browser.implicitly_wait(5)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
        browser.maximize_window()
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()

#     TODO разобраться с тем как работает этот код по ссылке https://automated-testing.info/t/oshibka-pri-zapuske-pytest-language-es-test-items-py-error-pytest-error-unrecognized-arguments-language-es/22952
