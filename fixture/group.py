from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def select_first_group(self):
        self.driver.find_element(By.NAME, 'selected[]').click()

    def edit_group_field(self, field_name, text):
        if text is not None:
            self.driver.find_element(By.NAME, field_name).clear()
            self.driver.find_element(By.NAME, field_name).send_keys(text)

    def edit_group_page(self, group):
        self.edit_group_field("group_name", group.name)
        self.edit_group_field("group_header", group.header)
        self.edit_group_field("group_footer", group.footer)

    def return_to_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        self.open_groups_page()
        self.driver.find_element(By.NAME, "new").click()
        self.edit_group_page(group)
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def delete_first(self):
        self.open_groups_page()
        self.select_first_group()
        self.driver.find_element(By.NAME, 'delete').click()
        self.return_to_groups_page()

    def edit_first(self, group):
        self.open_groups_page()
        self.select_first_group()
        self.driver.find_element(By.NAME, 'edit').click()
        self.edit_group_page(group)
        self.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def count(self):
        self.open_groups_page()
        return len(self.driver.find_elements(By.NAME, 'selected[]'))








