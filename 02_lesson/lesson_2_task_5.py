
def month_to_season(n):

    if n in (1,2,12):
        print("сезон Зима")
    if n in (3,4,5):
        print("сезон Весна")
    if n in (6,7,8):
        print("сезон Лето")
    if n in (9,10,11):
        print("сезон Осень")

month_to_season(int(input("номер месяца n = ")))