import pymysql.cursors

from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_groups_w_contacts_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_list.group_id, group_list.group_name, group_list.group_header, group_list.group_footer FROM group_list JOIN address_in_groups ON group_list.group_id=address_in_groups.group_id")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contacts_in_groups_list(self, id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT addressbook.id, addressbook.firstname, addressbook.lastname, addressbook.middlename, address_in_groups.group_id FROM addressbook JOIN address_in_groups ON addressbook.id=address_in_groups.id WHERE address_in_groups.group_id=%s" % id)
            for row in cursor:
                (id, firstname, lastname, middlename, group_id) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename, group_id=group_id))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, lastname, firstname, address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, lastname, firstname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(
                    Contact(firstname=firstname, lastname=lastname, address=address, home_phone=home, work_phone=work,
                            mobile_phone=mobile, secondary_phone=phone2,
                            email1=email, email2=email2, email3=email3, id=str(id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
