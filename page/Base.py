class BrowserContainer(object):
    def __init__(self, driver, baseURL):
        self.driver = driver
        self.baseURL = baseURL

class BasePage(BrowserContainer):
    def __init__(self, driver, baseURL, path):
        BrowserContainer.__init__(self, driver, baseURL)
        self.path = path

    def open(self):
        self.driver.get(self.baseURL + self.path)
