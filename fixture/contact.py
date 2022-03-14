from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_contact_page(self):
        if not (self.driver.current_url.endswith("index.php") and len(self.driver.find_elements(By.XPATH, '//input[@value="Send e-Mail"]')) > 0):
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
        self.contact_cache = None

    def select_contact_by_index(self, index):
        self.driver.find_elements(By.NAME, 'selected[]')[index].click()

    def delete_contact_by_index(self, index):
        self.open_contact_page()
        self.select_contact_by_index(index)
        self.driver.find_element(By.CSS_SELECTOR, '[value="Delete"]').click()
        self.driver.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def edit_contact_by_index(self, contact, index):
        self.open_contact_page()
        self.driver.find_elements(By.CSS_SELECTOR, '[title="Edit"]')[index].click()
        self.edit_contact_page(contact)
        self.driver.find_element(By.NAME, "update").click()
        self.open_contact_page()
        self.contact_cache = None

    def count(self):
        self.open_contact_page()
        return len(self.driver.find_elements(By.NAME, 'selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.open_contact_page()
            self.contact_cache = []
            for element in self.driver.find_elements(By.NAME, 'entry'):
                firstname = element.find_element(By.XPATH, './td[3]').text
                lastname = element.find_element(By.XPATH, './td[2]').text
                address = element.find_element(By.XPATH, './td[4]').text
                id = element.find_element(By.XPATH, './td[1]/input').get_attribute('id')
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id))
        return list(self.contact_cache)


