import time
from selenium.webdriver.common.by import By

def test_add_to_basket_button_is_present(browser):
    # Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Для визуальной проверки (закомментировать после тестирования)
    time.sleep(30)
    
    # Проверяем наличие кнопки добавления в корзину
    add_button = browser.find_element(
        By.CSS_SELECTOR, 
        "button.btn-add-to-basket"
    )
    
    assert add_button is not None, "Кнопка добавления в корзину не найдена"