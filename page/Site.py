import page.Base

class Site(page.Base.BrowserContainer):
    def __init__(self, driver, baseURL):
        page.Base.BrowserContainer.__init__(self, driver, baseURL)
    def getLoginPage(self):
        return LoginPage(self.driver, self.baseURL, '/login_test.html')


class LoginPage(page.Base.BasePage):
    def __init__(self, driver, baseURL, path):
        page.Base.BasePage.__init__(self, driver, baseURL, path)

    def login(self, username, pwd):
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_id('pwd').send_keys(pwd)
        self.driver.find_element_by_id('ok').click()
