
def month_to_season(n):

    if n in (1,2,12):
        return "сезон Зима"
    if n in (3,4,5):
        return "сезон Весна"
    if n in (6,7,8):
        return "сезон Лето"
    if n in (9,10,11):
        return "сезон Осень"

month_to_season(int(input("Номер месяца n = ")))

