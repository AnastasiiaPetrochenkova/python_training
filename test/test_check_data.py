import re
from random import randrange
from fixture.contact import Contact


def test_alldata_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add(
            Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                    company="Компания", address="Адрес", home_phone="749512312311", work_phone='71231231212',
                    secondary_phone='1234567890',
                    mobile_phone="797788148991", email1="test@test.test", email2="2test@test.test",
                    email3="3test@test.test"))
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact_from_home_page in contacts_from_home_page:
        for contact_from_db in contacts_from_db:
            if contact_from_home_page.id == contact_from_db.id:
                assert contact_from_home_page.lastname == contact_from_db.lastname.strip()
                assert contact_from_home_page.firstname == contact_from_db.firstname.strip()
                assert contact_from_home_page.address == contact_from_db.address.strip()
                assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
                    contact_from_db)
                assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
                    contact_from_db)

#     alldata_from_home_page = app.contact.get_contact_list()
#     index = randrange(len(alldata_from_home_page))
#     person_data_from_home_page = alldata_from_home_page[index]
#     person_data_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert person_data_from_home_page.firstname == person_data_from_edit_page.firstname.strip()
#     assert person_data_from_home_page.lastname == person_data_from_edit_page.lastname.strip()
#     assert person_data_from_home_page.address == person_data_from_edit_page.address.strip()
#     assert person_data_from_home_page.id == person_data_from_edit_page.id
#     assert person_data_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(person_data_from_edit_page)
#     assert person_data_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(person_data_from_edit_page)
#
#
# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
#     assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
#     assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
#     assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone
#
#
def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email1, contact.email2, contact.email3])))
