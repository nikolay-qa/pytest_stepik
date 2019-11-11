import pytest
from selenium import webdriver


lg = """["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt", "pt-br", 
"ro", "ru", "sk", "uk", "zh-hans"]"""  # define all the available languages in list, triple quotes for wrapping


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")      # adding option for different internet browsers
    parser.addoption('--language', action='store', default="en-gb",
                     help=f"Choose language:{lg}")      # adding option for choosing necessary language


@pytest.fixture(scope="function")
def browser(request):       # return variable with requested browser
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def lang(request):      # return variable with requested language
    user_language = request.config.getoption("language")
    if user_language in lg:
        return user_language
    else:
        raise pytest.UsageError(f"--language should be in: {lg}")

