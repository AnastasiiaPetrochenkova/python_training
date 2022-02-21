# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group

class Test_add_group():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path="/Users/anastasiia/PycharmProjects/python_training/chromedriver")

  def open_home_page(self):
    self.driver.get("http://localhost/addressbook/index.php")

  def login(self, user_name, password):
    self.driver.find_element(By.NAME, "user").click()
    self.driver.find_element(By.NAME, "user").clear()
    self.driver.find_element(By.NAME, "user").send_keys(user_name)
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").clear()
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_groups_page(self):
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def create_group(self, group):
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

  def return_to_groups_page(self):
    self.driver.find_element(By.LINK_TEXT, "group page").click()

  def logout(self):
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def test_add_new_group(self):
    self.open_home_page()
    self.login(user_name='admin', password='secret')
    self.open_groups_page()
    self.create_group(Group(name="имя", header="хедер", footer="футер"))
    self.return_to_groups_page()
    self.logout()

  def test_add_empty_group(self):
    self.open_home_page()
    self.login(user_name='admin', password='secret')
    self.open_groups_page()
    self.create_group(Group(name="", header="", footer=""))
    self.return_to_groups_page()
    self.logout()

  def teardown_method(self, method):
    self.driver.quit()
  
