"""
@Author SunYL
@Time 2023/9/13 22:13
"""

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.login_base import LoginBase


class LoginPage(LoginBase):

    def login_input_value(self, driver: WebDriver, input_placeholder, input_value):
        """
        获取页面用户名，设置用户名
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        input_xpath = self.login_input(input_placeholder)
        return driver.find_element(By.XPATH, input_xpath).send_keys(input_value)

    def click_login(self, driver: WebDriver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        login_button = self.login_button(button_name)
        return driver.find_element(By.XPATH, login_button).click()
