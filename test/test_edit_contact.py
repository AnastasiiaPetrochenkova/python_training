# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add(
            Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                    company="Компания", address="Адрес", home_phone="749512312311", work_phone='71231231212',
                    secondary_phone='1234567890',
                    mobile_phone="797788148991", email1="test@test.test", email2="2test@test.test",
                    email3="3test@test.test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Имя123", middlename="Отчество123", lastname="Фамилия123", nickname="Никнейм123",
                      title="Название123",
                      company="Компания123", address="Адрес123", home_phone="1231231231212", work_phone='8908907878',
                      mobile_phone="456789752345", secondary_phone='12345678901', email1="2test@test.test",
                      email2="22test@test.test",
                      email3="33test@test.test")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
