from selenium.webdriver.common.by import By

from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    def open_groups_page(self):
        if not (self.driver.current_url.endswith("/group.php") and len(self.driver.find_elements(By.NAME, 'new')) > 0):
            self.driver.find_element(By.LINK_TEXT, "groups").click()

    def select_group_by_index(self, index):
        self.driver.find_elements(By.NAME, 'selected[]')[index].click()

    def select_group_by_id(self, id):
        self.driver.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

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

    def create(self, json_groups):
        self.open_groups_page()
        self.driver.find_element(By.NAME, "new").click()
        self.edit_group_page(json_groups)
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        self.open_groups_page()
        self.select_group_by_index(index)
        self.driver.find_element(By.NAME, 'delete').click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        self.open_groups_page()
        self.select_group_by_id(id)
        self.driver.find_element(By.NAME, 'delete').click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_index(self, index, group):
        self.open_groups_page()
        self.select_group_by_index(index)
        self.driver.find_element(By.NAME, 'edit').click()
        self.edit_group_page(group)
        self.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, id, group):
        self.open_groups_page()
        self.select_group_by_id(id)
        self.driver.find_element(By.NAME, 'edit').click()
        self.edit_group_page(group)
        self.driver.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        self.open_groups_page()
        return len(self.driver.find_elements(By.NAME, 'selected[]'))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.open_groups_page()
            self.group_cache = []
            for element in self.driver.find_elements(By.CSS_SELECTOR, 'span.group'):
                text = element.text
                id = element.find_element(By.NAME, 'selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
