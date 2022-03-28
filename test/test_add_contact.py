# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(self, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone_number(self):
    first = str(random.randint(8000, 8999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}{}{}'.format(first, second, last)


def random_email(self, maxlen):
    email_domen = ['@gmail.com', '@yandex.ru', '@mail.ru', '@list.com']
    index = random.randrange(len(email_domen))
    name = ''.join(random.choice(string.ascii_letters) for _ in range(maxlen))
    email = name + email_domen[index]
    return email


testdata = [
    Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
            company=company, address=address, home_phone=home_phone, work_phone=work_phone, mobile_phone=mobile_phone,
            secondary_phone=secondary_phone,
            email1=email1, email2=email2, email3=email3)
    for firstname in [random_string('firstname', 10)]
    for middlename in [random_string('middlename', 15)]
    for lastname in [random_string('lastname', 15)]
    for nickname in [random_string('nickname', 20)]
    for title in [random_string('title', 20)]
    for company in [random_string('company', 20)]
    for address in [random_string('address', 20)]
    for home_phone in [random_phone_number('home_phone')]
    for work_phone in [random_phone_number('work_phone')]
    for mobile_phone in [random_phone_number('mobile_phone')]
    for secondary_phone in [random_phone_number('secondary_phone')]
    for email1 in [random_email('email1', 7)]
    for email2 in [random_email('email2', 7)]
    for email3 in [random_email('email3', 7)]
]


@pytest.mark.parametrize('contact', testdata, ids=[str(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
