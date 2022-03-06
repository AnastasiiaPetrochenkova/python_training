from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def login(self, user_name, password):
        self.app.open_home_page()
        self.driver.find_element(By.NAME, "user").click()
        self.driver.find_element(By.NAME, "user").clear()
        self.driver.find_element(By.NAME, "user").send_keys(user_name)
        self.driver.find_element(By.NAME, "pass").click()
        self.driver.find_element(By.NAME, "pass").clear()
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def is_logged_in(self):
        return len(self.driver.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        return self.driver.find_element(By.XPATH, '//*[@id="top"]/form/b').text == "(" + username + ")"

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
