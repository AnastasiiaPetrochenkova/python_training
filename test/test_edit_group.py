# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first(app):
    app.session.login(user_name='admin', password='secret')
    app.group.edit_first(Group(name="имя1", header="хедер1", footer="футер1"))
    app.session.logout()


