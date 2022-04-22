import random
from datetime import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app):
    contact_list = app.orm.get_contact_list()
    if len(contact_list) == 0:
        app.contact.add(
            Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                    company="Компания", address="Адрес", home_phone="749512312311", work_phone='71231231212',
                    secondary_phone='1234567890',
                    mobile_phone="797788148991", email1="test@test.test", email2="2test@test.test",
                    email3="3test@test.test"))
    group_list = app.orm.get_group_list()
    if len(group_list) == 0:
        app.group.create_contact_to_group(Group(name='test', header='test1', footer='test2'))
    groups = app.orm.get_group_list()
    group = random.choice(groups)
    old_contacts = app.orm.get_contacts_in_group(group)
    if len(old_contacts) == 0:
        app.contact.create_contact_to_group(Contact(firstname='Firstname', lastname='Lastname'), group)
        old_contacts = app.orm.get_contacts_in_group(group)
    contacts = app.orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_to_group(contact, group)
    old_contacts.append(contact)
    new_contacts = app.orm.get_contacts_in_group(group)
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(
        new_contacts, key=Contact.id_or_max)

def test_del_contact_from_group(app, db):
    contact_list = app.orm.get_contact_list()
    if len(contact_list) == 0:
        app.contact.add(
            Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                    company="Компания", address="Адрес", home_phone="749512312311", work_phone='71231231212',
                    secondary_phone='1234567890',
                    mobile_phone="797788148991", email1="test@test.test", email2="2test@test.test",
                    email3="3test@test.test"))
    group_list = app.orm.get_group_list()
    if len(group_list) == 0:
        app.group.create_contact_to_group(Group(name='test', header='test1', footer='test2'))
    groups = app.orm.get_group_list()
    group = random.choice(groups)
    Select(app.driver.find_element(By.NAME, 'group')).select_by_value(group.id)
    contacts = app.orm.get_contacts_in_group(group)
    if len(contacts) == 0:
        app.contact.create_contact_to_group(Contact(firstname='Firstname', lastname='Lastname'), group)
        contacts = app.orm.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_contact_from_group(contact, group)
    contacts.remove(contact)
    new_contacts = app.orm.get_contacts_in_group(group)
    assert len(contacts) == len(new_contacts)
    assert sorted(contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

