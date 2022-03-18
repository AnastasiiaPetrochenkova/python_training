from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None,  work_phone=None, mobile_phone=None,
                 email=None, id=None):
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
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s" % (self.firstname, self.lastname, self.address, self.id, self.home_phone, self.work_phone, self.mobile_phone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address, self.home_phone == other.home_phone, self.work_phone == other.work_phone, self.mobile_phone == other.mobile_phone

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
