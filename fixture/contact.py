import re

from selenium.webdriver.common.by import By

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_contact_page(self):
        if not (self.driver.current_url.endswith("index.php") and len(
                self.driver.find_elements(By.XPATH, '//input[@value="Send e-Mail"]')) > 0):
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
        self.edit_contact_field("work", contact.work_phone)
        self.edit_contact_field("phone2", contact.secondary_phone)
        self.edit_contact_field("email", contact.email1)
        self.edit_contact_field("email2", contact.email2)
        self.edit_contact_field("email3", contact.email3)

    def add(self, contact):
        self.open_contact_page()
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        self.edit_contact_page(contact)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        self.driver.find_elements(By.NAME, 'selected[]')[index].click()

    def select_contact_by_id(self, id):
        self.driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def delete_contact_by_index(self, index):
        self.open_contact_page()
        self.select_contact_by_index(index)
        self.driver.find_element(By.CSS_SELECTOR, '[value="Delete"]').click()
        self.driver.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        self.open_contact_page()
        self.select_contact_by_id(id)
        self.driver.find_element(By.CSS_SELECTOR, '[value="Delete"]').click()
        self.driver.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def edit_contact_by_index(self, contact, index):
        self.open_contact_to_edit_by_index(index)
        self.edit_contact_page(contact)
        self.driver.find_element(By.NAME, "update").click()
        self.open_contact_page()
        self.contact_cache = None

    def edit_contact_by_id(self, contact, id):
        self.open_contact_to_edit_by_id(id)
        self.edit_contact_page(contact)
        self.driver.find_element(By.NAME, "update").click()
        self.open_contact_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        self.open_contact_page()
        self.driver.find_elements(By.CSS_SELECTOR, '[title="Edit"]')[index].click()

    def open_contact_to_edit_by_id(self, id):
        self.open_contact_page()
        self.driver.find_element(By.XPATH, "//input[@id='%s']/../..//*[@title='Edit']" % id).click()

    def open_contact_view_by_index(self, index):
        self.open_contact_page()
        self.driver.find_elements(By.CSS_SELECTOR, '[title="Details"')[index].click()

    def count(self):
        self.open_contact_page()
        return len(self.driver.find_elements(By.NAME, 'selected[]'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.open_contact_page()
            self.contact_cache = []
            for element in self.driver.find_elements(By.NAME, 'entry'):
                id = element.find_element(By.XPATH, './td[1]/input').get_attribute('id')
                lastname = element.find_element(By.XPATH, './td[2]').text
                firstname = element.find_element(By.XPATH, './td[3]').text
                address = element.find_element(By.XPATH, './td[4]').text
                all_emails = element.find_element(By.XPATH, './td[5]').text
                all_phones = element.find_element(By.XPATH, './td[6]').text
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                            all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        firstname = self.driver.find_element(By.NAME, 'firstname').get_attribute('value')
        lastname = self.driver.find_element(By.NAME, 'lastname').get_attribute('value')
        id = self.driver.find_element(By.NAME, 'id').get_attribute('value')
        address = self.driver.find_element(By.NAME, 'address').get_attribute('value')
        home_phone = self.driver.find_element(By.NAME, 'home').get_attribute('value')
        work_phone = self.driver.find_element(By.NAME, 'work').get_attribute('value')
        secondary_phone = self.driver.find_element(By.NAME, 'phone2').get_attribute('value')
        mobile_phone = self.driver.find_element(By.NAME, 'mobile').get_attribute('value')
        email1 = self.driver.find_element(By.NAME, 'email').get_attribute('value')
        email2 = self.driver.find_element(By.NAME, 'email2').get_attribute('value')
        email3 = self.driver.find_element(By.NAME, 'email3').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, home_phone=home_phone,
                       mobile_phone=mobile_phone, work_phone=work_phone, secondary_phone=secondary_phone, email1=email1,
                       email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        self.open_contact_view_by_index(index)
        text = self.driver.find_element(By.ID, 'content').text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        secondary_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       secondary_phone=secondary_phone)
