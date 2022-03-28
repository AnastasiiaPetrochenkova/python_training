from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None, work_phone=None, mobile_phone=None, secondary_phone=None,
                 email1=None, email2=None, email3=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.secondary_phone = secondary_phone
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (
            self.firstname, self.middlename, self.lastname, self.nickname, self.title, self.company, self.address,
            self.home_phone, self.work_phone, self.mobile_phone, self.secondary_phone, self.email1, self.email2,
            self.email3, self.id)

    def __eq__(self, other):
        return (
                           self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address, self.home_phone == other.home_phone, self.work_phone == other.work_phone, self.mobile_phone == other.mobile_phone, self.secondary_phone == other.secondary_phone, self.email1 == other.email1, self.email2 == other.email2, self.email3 == other.email3

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
