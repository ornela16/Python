
def month_to_season(n):

    if n in (1,2,12):
        print("cезон " + "Зима")

    if n in (3,4,5):
        print("cезон " + "Весна")

    if n in (6,7,8):
         print("cезон " + "Лето")

    if n in (9,10,11):
          print("cезон " + "Осень")

month_to_season(int(input("Номер месяца n = ")))

