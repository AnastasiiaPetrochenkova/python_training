from model.contact import Contact
from mimesis import Generic
from mimesis.locales import Locale
from mimesis import Person
from mimesis import Address
import os.path
import jsonpickle
import getopt
import sys

g = Generic(locale=Locale.RU)
personal = Person('ru')
ad = Address('ru')

# Читаем опции с командной строки.
# Опция n: - задает кол-во генерируемых данных
# Опция f: - задает файл, в который должно помещаться
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

testdata = [Contact(firstname="Имя2", middlename="Отчество", lastname="Фамилия", nickname="Никнейм", title="Название",
                    company="Компания", address="Адрес", home_phone="749512312311", work_phone='71231231212',
                    secondary_phone='1234567890',
                    mobile_phone="797788148991", email1="test@test.test", email2="2test@test.test",
                    email3="3test@test.test")] + [
               Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title,
                       company=company, address=address, home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, secondary_phone=secondary_phone, email1=email1, email2=email2,
                       email3=email3)
                for i in range(n)
                   for firstname in [personal.name()]
                   for middlename in [personal.name()]
                   for lastname in [personal.last_name()]
                   for nickname in [personal.username()]
                   for title in [personal.title()]
                   for company in [g.text.word()]
                   for address in [ad.address()]
                   for home_phone in [personal.telephone()]
                   for work_phone in [personal.telephone()]
                   for mobile_phone in [personal.telephone()]
                   for secondary_phone in [personal.telephone()]
                   for email1 in [personal.email()]
                   for email2 in [personal.email()]
                   for email3 in [personal.email()]
               ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2, ensure_ascii=False)
    out.write(jsonpickle.encode(testdata))

