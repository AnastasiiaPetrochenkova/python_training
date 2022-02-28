# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, method):
        self.driver = webdriver.Chrome(executable_path="/Users/anastasiia/PycharmProjects/python_training/chromedriver")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        self.driver = self.driver
        self.driver.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.driver = self.driver
        self.driver.quit()
