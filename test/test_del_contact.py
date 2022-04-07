# -*- coding: utf-8 -*-
import random

from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(
            Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                    company="Компания", address="Адрес", home_phone="749512312311", work_phone='71231231212',
                    secondary_phone='1234567890',
                    mobile_phone="797788148991", email1="test@test.test", email2="2test@test.test",
                    email3="3test@test.test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
