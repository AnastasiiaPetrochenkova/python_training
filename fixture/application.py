# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper
from fixture.orm import ORMFixture



class Application:

    def __init__(self, browser, base_url):
        if browser == 'chrome':
            self.driver = webdriver.Chrome(
                executable_path="/Users/anastasiia/PycharmProjects/python_training/chromedriver")
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url
        self.orm = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self):
        self.driver = self.driver
        self.driver.get(self.base_url)

    def destroy(self):
        self.driver = self.driver
        self.driver.quit()
