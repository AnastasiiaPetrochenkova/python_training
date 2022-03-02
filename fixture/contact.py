from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def contact_profile(self, contact):
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").clear()
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.driver.find_element(By.NAME, "middlename").clear()
        self.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.driver.find_element(By.NAME, "lastname").clear()
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.driver.find_element(By.NAME, "nickname").clear()
        self.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.driver.find_element(By.NAME, "title").clear()
        self.driver.find_element(By.NAME, "title").send_keys(contact.title)
        self.driver.find_element(By.NAME, "company").clear()
        self.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.driver.find_element(By.NAME, "address").clear()
        self.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.driver.find_element(By.NAME, "home").clear()
        self.driver.find_element(By.NAME, "home").send_keys(contact.home_phone)
        self.driver.find_element(By.NAME, "mobile").clear()
        self.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys(contact.email)

    def add(self, contact):
        self.driver = self.app.driver
        self.driver.find_element(By.XPATH, '//a[contains(text(),"home")]').click()
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        ContactHelper.contact_profile(self, contact)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

    def delete_first(self):
        self.driver = self.app.driver
        self.driver.find_element(By.XPATH, '//a[contains(text(),"home")]').click()
        self.driver.find_element(By.NAME, 'selected[]').click()
        self.driver.find_element(By.XPATH, '//input[@value="Delete"]').click()
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"home")]').click()

    def edit_first(self, contact):
        self.driver = self.app.driver
        self.driver.find_element(By.XPATH, '//a[contains(text(),"home")]').click()
        self.driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
        ContactHelper.contact_profile(self, contact)
        self.driver.find_element(By.NAME, "update").click()


