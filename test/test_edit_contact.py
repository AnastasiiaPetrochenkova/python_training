# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(
            Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                    company="Компания", address="Адрес", home_phone="749512312311", work_phone='71231231212',
                    secondary_phone='1234567890',
                    mobile_phone="797788148991", email1="test@test.test", email2="2test@test.test",
                    email3="3test@test.test"))
    old_contacts = db.get_contact_list()
    edited_contact = random.choice(old_contacts)
    index = old_contacts.index(edited_contact)
    contact = Contact(firstname="Имя123", middlename="Отчество123", lastname="Фамилия123", nickname="Никнейм123",
                      title="Название123",
                      company="Компания123", address="Адрес123", home_phone="1231231231212", work_phone='8908907878',
                      mobile_phone="456789752345", secondary_phone='12345678901', email1="2test@test.test",
                      email2="22test@test.test",
                      email3="33test@test.test")
    contact.id = edited_contact.id
    app.contact.edit_contact_by_id(contact, contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
