from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройки драйвера
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)

try:
    # Открываем страницу
    driver.get("https://stellarburgers.education-services.ru/")
    print("Страница загружается...")
    time.sleep(5)
    
    print(f"\n=== ОСНОВНАЯ ИНФОРМАЦИЯ ===")
    print(f"Заголовок: {driver.title}")
    print(f"URL: {driver.current_url}")
    
    # Проверяем основные разделы
    print(f"\n=== СТРУКТУРА СТРАНИЦЫ ===")
    
    # 1. Ищем хедер
    headers = driver.find_elements(By.TAG_NAME, "header")
    print(f"Найдено <header> элементов: {len(headers)}")
    if headers:
        print(f"HTML header: {headers[0].get_attribute('outerHTML')[:500]}...")
    
    # 2. Ищем навигационные элементы
    print(f"\n=== НАВИГАЦИОННЫЕ КНОПКИ ===")
    nav_elements = driver.find_elements(By.XPATH, "//a | //button")
    print(f"Всего ссылок и кнопок: {len(nav_elements)}")
    
    # Фильтруем навигацию
    nav_texts = ["Конструктор", "Лента", "Личный", "Кабинет", "Constructor", "Feed", "Account"]
    for element in nav_elements:
        try:
            text = element.text.strip()
            if text and any(nav_text in text for nav_text in nav_texts):
                print(f"Навигация: '{text}' | Тег: {element.tag_name} | ID: {element.get_attribute('id')} | Класс: {element.get_attribute('class')}")
        except:
            pass
    
    # 3. Ищем основные разделы конструктора
    print(f"\n=== РАЗДЕЛЫ КОНСТРУКТОРА ===")
    sections = ["Булки", "Соусы", "Начинки", "Buns", "Sauces", "Fillings"]
    for section in sections:
        elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{section}')]")
        if elements:
            print(f"Раздел '{section}': найдено {len(elements)} элементов")
            for elem in elements[:2]:
                parent = elem.find_element(By.XPATH, "..")
                print(f"  - Текст: '{elem.text}' | Класс: {elem.get_attribute('class')}")
                print(f"    Родитель класс: {parent.get_attribute('class')}")
    
    # 4. Сохраняем полный HTML для анализа
    with open("page_source.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"\nПолный HTML сохранен в page_source.html")
    
    # 5. Делаем скриншот
    driver.save_screenshot("explore_page.png")
    print("Скриншот сохранен: explore_page.png")
    
    # 6. Ищем по классам
    print(f"\n=== ПОПУЛЯРНЫЕ КЛАССЫ ===")
    all_elements = driver.find_elements(By.XPATH, "//*[@class]")
    class_counter = {}
    for element in all_elements:
        classes = element.get_attribute('class')
        if classes:
            for cls in classes.split():
                class_counter[cls] = class_counter.get(cls, 0) + 1
    
    # Выводим топ-20 классов
    print("Топ-20 классов на странице:")
    for cls, count in sorted(class_counter.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"  {cls}: {count} элементов")

finally:
    driver.quit()
    print("\n=== ИССЛЕДОВАНИЕ ЗАВЕРШЕНО ===")
