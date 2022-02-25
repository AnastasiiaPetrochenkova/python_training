# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application(request)
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.session.login(user_name='admin', password='secret')
    app.create_group(Group(name="имя", header="хедер", footer="футер"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user_name='admin', password='secret')
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()
