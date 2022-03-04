from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver


    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def return_to_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
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

    def delete_first(self):
        self.open_groups_page()
        # select first group
        self.driver.find_element(By.NAME, 'selected[]').click()
        # delete selected group
        self.driver.find_element(By.NAME, 'delete').click()
        self.return_to_groups_page()

    def edit_first(self, group):
        # open groups page
        self.open_groups_page()
        self.driver.find_element(By.NAME, 'selected[]').click()
        self.driver.find_element(By.NAME, 'edit').click()
        self.driver.find_element(By.NAME, "group_name").clear()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").clear()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").clear()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        self.driver.find_element(By.NAME, 'update').click()
        self.return_to_groups_page()