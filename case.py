import unittest
from selenium import webdriver

import page.Site

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.site = page.Site.Site(self.driver,\
                'file:///C:/Users/Administrator/Desktop/sample')
        self.loginPage = self.site.getLoginPage()

    def testLogin(self):
        self.loginPage.open()
        self.loginPage.login('test', 'test')

        alert = self.driver.switch_to_alert()
        assert 'succ' in alert.text
        alert.accept()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
