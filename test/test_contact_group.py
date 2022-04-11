import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
from model.group import Group

def test_add_contact_to_group(app, db):
    contact_list = db.get_contact_list()
    if len(contact_list) == 0:
        app.contact.add(
            Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                    company="Компания", address="Адрес", home_phone="749512312311", work_phone='71231231212',
                    secondary_phone='1234567890',
                    mobile_phone="797788148991", email1="test@test.test", email2="2test@test.test",
                    email3="3test@test.test"))
        contact_list = db.get_contact_list()
    group_list = db.get_group_list()
    if len(group_list) == 0:
        app.group.create(Group(name='test', header='test1', footer='test2'))
        group_list = db.get_group_list()
    index = random.randrange(len(contact_list))
    app.contact.select_contact_by_index(index)
    number = random.randrange(len(group_list))
    app.contact.add_contact_to_group(number)

def test_del_contact_from_group(app, db):
    # Не мое Выбираем группу
    groups = db.get_groups_w_contacts_list()
    group = random.choice(groups)
    # Фильтруем контакты по группе
    Select(app.driver.find_element(By.NAME, 'group')).select_by_value(group.id)
    # Выбираем контакт
    contacts = db.get_contacts_in_groups_list(group.id)
    contact = random.choice(contacts)
    # Удаляем контакт из группы
    app.contact.remove_from_group(contact, group)
    app.open_home_page()