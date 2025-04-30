import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language", 
        action="store",
        default="en",
        help="Choose browser language (e.g., 'es', 'fr')"
    )

@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    user_language = request.config.getoption("language")
    
    # Настраиваем Chrome для указанного языка
    options = Options()
    options.add_experimental_option(
        'prefs', 
        {'intl.accept_languages': user_language}
    )
    
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()