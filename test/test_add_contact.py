# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application(request)
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
  app.session.login(user_name='admin', password='secret')
  app.add_contact(Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название", company="Компания", address="Адрес", home_phone="749512312311", mobile_phone="797788148991", email="test@test.test"))
  app.session.logout()
