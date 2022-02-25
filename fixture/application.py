# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper

class Application:

    def __init__(self, method):
        self.driver = webdriver.Chrome(executable_path="/Users/anastasiia/PycharmProjects/python_training/chromedriver")
        self.session = SessionHelper(self)

    def open_home_page(self):
        self.driver = self.driver
        self.driver.get("http://localhost/addressbook/index.php")

    def open_groups_page(self):
        self.driver = self.driver
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.driver = self.driver
        # open groups page
        self.open_groups_page()
        # init group creation
        self.driver.find_element(By.NAME, "new").click()
         # fill group form
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()
        # return to groups page
        self.return_to_groups_page()

    def return_to_groups_page(self):
        self.driver = self.driver
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def add_contact(self, contact):
        self.driver = self.driver
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.driver.find_element(By.NAME, "middlename").click()
        self.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.driver.find_element(By.NAME, "lastname").click()
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.driver.find_element(By.NAME, "nickname").click()
        self.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").send_keys(contact.title)
        self.driver.find_element(By.NAME, "company").click()
        self.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.driver.find_element(By.NAME, "address").click()
        self.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.driver.find_element(By.NAME, "theform").click()
        self.driver.find_element(By.NAME, "home").click()
        self.driver.find_element(By.NAME, "home").send_keys(contact.home_phone)
        self.driver.find_element(By.NAME, "mobile").click()
        self.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile_phone)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

    def destroy(self):
        self.driver = self.driver
        self.driver.quit()