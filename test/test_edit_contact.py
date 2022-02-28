# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first(app):
    app.session.login(user_name='admin', password='secret')
    app.contact.edit_first(
        Contact(firstname="Имя3", middlename="Отчество3", lastname="Фамилия3", nickname="Никнейм3", title="Название3",
                company="Компания3", address="Адрес3", home_phone="7495123123113", mobile_phone="7977881489913",
                email="test3@test.test"))
    app.session.logout()
