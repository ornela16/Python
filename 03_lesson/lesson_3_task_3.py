from address import Address
from mailing import Mailing

to_address = Address(184600, "Мурманск", "Ленина", "29", "16")
from_address = Address(105064, "Москва", "Земляной вал", "2", "6")

letter = Mailing(to_address, from_address, "300", "19860987858")

print(letter)
