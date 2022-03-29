# -*- coding: utf-8 -*-
from random import randrange
from model.group import Group


def test_edit_some_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test', header='test1', footer='test2'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="новое имя1")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_some_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test', header='test1', footer='test2'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = (Group(header="новый хедер1"))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_some_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test', header='test1', footer='test2'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = (Group(footer="новый футер1"))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
