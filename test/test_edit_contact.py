# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first(app):
    app.contact.edit_first(
        Contact(firstname="Имя123", middlename="Отчество123", lastname="Фамилия123", nickname="Никнейм123", title="Название123",
                company="Компания123", address="Адрес123", home_phone="12345", mobile_phone="12345",
                email="test123@test.test"))
