# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test', header='test1', footer='test2'))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="новое имя1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test', header='test1', footer='test2'))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(header="новый хедер1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_first_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test', header='test1', footer='test2'))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(footer="новый футер1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
