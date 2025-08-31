from smartphone import Smartphone

catalog = [
    Smartphone("Honor", "200 Pro", "+79213458966"),
    Smartphone("Samsung", " Galaxy A55", "+79113186835"),
    Smartphone("Apple", "iPhone 16 Pro", "+79583259045"),
    Smartphone("Huawei", "Pura 70", "+79637806532"),
    Smartphone("Tecno", "Pova 6", "+79213457249")]

for smartphone in catalog:
    print(smartphone.markphone, "-", smartphone.modelphone, ".", smartphone.numberphone)
