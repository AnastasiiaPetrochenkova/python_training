from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.driver = self.app.driver
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        self.driver = self.app.driver
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
        self.driver = self.app.driver
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def delete_first_group(self):
        self.driver = self.app.driver
        self.open_groups_page()
        # select first group
        self.driver.find_element(By.NAME, 'selected[]').click()
        # delete selected group
        self.driver.find_element(By.NAME, 'delete').click()
        self.return_to_groups_page()
