# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_name(app):
    app.session.login(user_name='admin', password='secret')
    app.group.edit_first(Group(name="новое имя1"))
    app.session.logout()

def test_edit_first_header(app):
    app.session.login(user_name='admin', password='secret')
    app.group.edit_first(Group(header="новый хедер1"))
    app.session.logout()

def test_edit_first_footer(app):
    app.session.login(user_name='admin', password='secret')
    app.group.edit_first(Group(footer="новый футер1"))
    app.session.logout()
