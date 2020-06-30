# encoding=utf-8

import unittest
from selenium import webdriver

class Hsy_LogIn(unittest.TestCase):
    def setUp(self):
        # 实例化浏览器
        self.driver = webdriver.Chrome()
        # 打开项目网站
        self.driver.get("https://haoshengy.com/pc_workbench/login")
        # 设置隐式等待
        self.driver.maximize_window()
        # 浏览器最大化
        self.driver.implicitly_wait(30)

    def test_logIn(self):
        driver = self.driver
        # 定位用户名及操作
        driver.find_elements_by_class_name("el-input__inner")[1].send_keys('18582892580')
        # 定位密码及操作
        driver.find_elements_by_class_name("el-input__inner")[2].send_keys('123456789')
        # 点击登录
        driver.find_elements_by_class_name("login__button")[0].click

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__' :
    unittest.main()