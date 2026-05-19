from playwright.sync_api import sync_playwright

# Первый тестовый скрипт - открываем браузер и сайт SauceDemo
with sync_playwright() as p:
    # Запускаем браузер (headless=False — чтобы видеть окно браузера)
    browser = p.chromium.launch(
        headless=False,      # False = видимый режим
        slow_mo=800          # Замедление действий (для удобства обучения)
    )
    
    # Создаём новую вкладку
    page = browser.new_page()
    
    # Переходим на SauceDemo
    print("Открываем браузер и переходим на https://www.saucedemo.com/")
    page.goto("https://www.saucedemo.com/")
    
    # Проверяем, что страница загрузилась
    print("✅ Страница успешно загрузилась!")
    print(f"Заголовок страницы: {page.title()}")
    
    # Ждём 8 секунд, чтобы ты могла посмотреть результат
    page.wait_for_timeout(8000)
    
    # Закрываем браузер
    browser.close()
    print("Браузер закрыт. Первый скрипт выполнен успешно!")