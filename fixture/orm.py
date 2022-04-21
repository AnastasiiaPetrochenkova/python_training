from datetime import datetime

from pony.orm import *

from model.contact import Contact
from model.group import Group


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')  # Обязательное поле, по которому объекты будут идентифицироваться
        name = Optional(str, column='group_name')  # Optional потому что это поле может быть пустым
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column='id', reverse='groups',
                       lazy=True)  # Set - множество, table - указываем по какой таблице идет связь

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')  # Обязательное поле, по которому объекты будут идентифицироваться
        firstname = Optional(str, column='firstname')  # Optional потому что это поле может быть пустым
        middlename = Optional(str, column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        title = Optional(str, column='title')
        company = Optional(str, column='company')
        address = Optional(str, column='address')
        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        secondary_phone = Optional(str, column='phone2')
        email1 = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column='group_id', reverse='contacts',
                     lazy=True)

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    def get_group_list(self):
        with db_session:
            return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, middlename=contact.middlename,
                           lastname=contact.lastname, nickname=contact.nickname, title=contact.title,
                           company=contact.company, address=contact.address, home_phone=contact.home_phone,
                           mobile_phone=contact.mobile_phone, work_phone=contact.work_phone,
                           secondary_phone=contact.secondary_phone, email1=contact.email1, email2=contact.email2,
                           email3=contact.email3)

        return list(map(convert, contacts))

    def get_contact_list(self):
        with db_session:
            return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))









