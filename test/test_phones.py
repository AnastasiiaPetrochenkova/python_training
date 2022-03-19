import re
from random import randrange


def test_alldata_on_home_page(app):
    alldata_from_home_page = app.contact.get_contact_list()
    index = randrange(len(alldata_from_home_page))
    person_data_from_home_page = alldata_from_home_page[index]
    person_data_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert person_data_from_home_page.firstname == person_data_from_edit_page.firstname
    assert person_data_from_home_page.lastname == person_data_from_edit_page.lastname
    assert person_data_from_home_page.address == person_data_from_edit_page.address
    assert person_data_from_home_page.id == person_data_from_edit_page.id
    assert person_data_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(person_data_from_edit_page)
    assert person_data_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(person_data_from_edit_page)
    print(person_data_from_home_page)
    print(person_data_from_edit_page)

def test_get_contact_list(app):
    app.contact.get_contact_list()


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))

