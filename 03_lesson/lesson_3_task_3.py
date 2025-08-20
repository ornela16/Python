from address import Address
from mailing import Mailing

address1 = Address(184600, "Мурманск", "Ленина", "29", "16")
address2 = Address(105064, "Москва", "Земляной вал", "2", "6")

letter = Mailing("в Мурманск", "из Москвы", "300", "103465676998")
letter.mailing()




