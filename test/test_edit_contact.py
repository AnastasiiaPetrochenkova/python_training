# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                company="Компания", address="Адрес", home_phone="749512312311", mobile_phone="797788148991",
                email="test@test.test"))
    app.contact.edit_first(
        Contact(firstname="Имя123", middlename="Отчество123", lastname="Фамилия123", nickname="Никнейм123", title="Название123",
                company="Компания123", address="Адрес123", home_phone="12345", mobile_phone="12345",
                email="test123@test.test"))
