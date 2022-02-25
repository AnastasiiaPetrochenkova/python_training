# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(user_name='admin', password='secret')
    app.contact.add(
        Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                company="Компания", address="Адрес", home_phone="749512312311", mobile_phone="797788148991",
                email="test@test.test"))
    app.session.logout()
