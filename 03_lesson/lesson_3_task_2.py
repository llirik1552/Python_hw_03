from smartphone import Smartphone

catalog = [Smartphone("Самсунг", "А-50", "+79824567893"),
           Smartphone("Сяоми", "Редми 10А", " +79344532671"),
           Smartphone("Хуавей", "Z-8", "+79824598712"),
           Smartphone("Нокиа", "3310", "+79024567822"),
           Smartphone("Сименс", "Е-59", "+79345899382")
           ]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} {smartphone.phone_model} {smartphone.subscriber_number}")