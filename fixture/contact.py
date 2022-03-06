from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_contact_page(self):
        self.driver.find_element(By.XPATH, '//a[contains(text(),"home")]').click()

    def edit_contact_field(self, field_name, text):
        if text is not None:
            self.driver.find_element(By.NAME, field_name).clear()
            self.driver.find_element(By.NAME, field_name).send_keys(text)

    def edit_contact_page(self, contact):
        self.edit_contact_field("firstname", contact.firstname)
        self.edit_contact_field("middlename", contact.middlename)
        self.edit_contact_field("lastname", contact.lastname)
        self.edit_contact_field("nickname", contact.nickname)
        self.edit_contact_field("title", contact.title)
        self.edit_contact_field("company", contact.company)
        self.edit_contact_field("address", contact.address)
        self.edit_contact_field("home", contact.home_phone)
        self.edit_contact_field("mobile", contact.mobile_phone)
        self.edit_contact_field("email", contact.email)

    def add(self, contact):
        self.open_contact_page()
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        self.edit_contact_page(contact)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

    def delete_first(self):
        self.open_contact_page()
        self.driver.find_element(By.NAME, 'selected[]').click()
        self.driver.find_element(By.XPATH, '//input[@value="Delete"]').click()
        self.driver.switch_to.alert.accept()
        self.open_contact_page()

    def edit_first(self, contact):
        self.open_contact_page()
        self.driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.edit_contact_page(contact)
        self.driver.find_element(By.NAME, "update").click()
        self.open_contact_page()

    def count(self):
        self.open_contact_page()
        return len(self.driver.find_elements(By.NAME, 'selected[]'))

