# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_add_new_group():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path="/Users/anastasiia/PycharmProjects/python_training/chromedriver")
  
  def test_add_new_group(self):
    # open home page
    self.driver.get("http://localhost/addressbook/index.php")
    # login
    self.driver.find_element(By.NAME, "user").click()
    self.driver.find_element(By.NAME, "user").clear()
    self.driver.find_element(By.NAME, "user").send_keys('admin')
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").clear()
    self.driver.find_element(By.NAME, "pass").send_keys('secret')
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    # open groups page
    self.driver.find_element(By.LINK_TEXT, "groups").click()
    # init group creation
    self.driver.find_element(By.NAME, "new").click()
    # fill group form
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys("fghjk")
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys("fghjkl")
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys("fghjkl")
    # submit group creation
    self.driver.find_element(By.NAME, "submit").click()
    # return to group page
    self.driver.find_element(By.LINK_TEXT, "group page").click()
    # logout
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def teardown_method(self, method):
    self.driver.quit()
  
