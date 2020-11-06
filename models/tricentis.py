from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class PageTest:
    def __init__(self, url, driver_path):
        self.url = url
        self.driver_path = driver_path
        self.driver = webdriver.Chrome(self.driver_path)

    def open_browser(self):
        self.driver.get(self.url)

    def select_tab(self, tab_id):
        tab = self.driver.find_element_by_id(tab_id)
        tab.click()

    def fill_text_by_id(self, element_id, content):
        input_field = self.driver.find_element_by_id(element_id)
        input_field.click()
        input_field.send_keys(content)
        input_field.send_keys(Keys.RETURN)

    def select_option_by_xpath(self, element_xpath):
        clicked_option = self.driver.find_element_by_xpath(element_xpath)
        clicked_option.click()
        clicked_option.send_keys(Keys.RETURN)

    def button_click_by_id(self, button_id):
        button_clicked = self.driver.find_element_by_id(button_id)
        button_clicked.click()

    def delay_timer(self, timer_count):
        time.sleep(timer_count)

    def quit_test(self):
        self.driver.quit()
