# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_name(app):
    app.group.edit_first(Group(name="новое имя1"))

def test_edit_first_header(app):
    app.group.edit_first(Group(header="новый хедер1"))

def test_edit_first_footer(app):
    app.group.edit_first(Group(footer="новый футер1"))
