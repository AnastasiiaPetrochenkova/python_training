# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                company="Компания", address="Адрес", home_phone="749512312311", mobile_phone="797788148991",
                email="test@test.test"))
    app.contact.delete_first()
