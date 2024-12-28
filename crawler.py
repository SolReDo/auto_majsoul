from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_most_powerful(hands):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # 设置驱动路径（假设 chromedriver 在系统路径中）
    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://tenhou.net/2/?q='+hands
    driver.get(url)

    # 获取页面内容
    # print(driver.page_source)

    # XPath 操作
    element = driver.find_element(By.XPATH, '//*[@id="m2"]/textarea')
    print(element.text)

    element_list = element.text.splitlines()
    #print(element_list)

    most_powerful = element_list[1][1:3]
    #print(most_powerful)

    driver.quit()

    return most_powerful
