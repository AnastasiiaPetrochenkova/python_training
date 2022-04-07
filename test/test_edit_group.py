# -*- coding: utf-8 -*-
import random

from model.group import Group


def test_edit_by_id(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test', header='test1', footer='test2'))
    old_groups = db.get_group_list()
    edit_group = random.choice(old_groups)
    index = old_groups.index(edit_group)
    group = Group(name='test1', header='test2', footer='test3')
    group.id = edit_group.id
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#
# def test_edit_some_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test', header='test1', footer='test2'))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = (Group(header="новый хедер1"))
#     group.id = old_groups[index].id
#     app.group.edit_group_by_index(index, group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
#
# def test_edit_some_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name='test', header='test1', footer='test2'))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = (Group(footer="новый футер1"))
#     group.id = old_groups[index].id
#     app.group.edit_group_by_index(index, group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
