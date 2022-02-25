# -*- coding: utf-8 -*-

def test_add_new_group(app):
    app.session.login(user_name='admin', password='secret')
    app.group.create(Group(name="имя", header="хедер", footer="футер"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(user_name='admin', password='secret')
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
