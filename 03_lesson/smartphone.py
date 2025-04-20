class Smartphone:

    def __init__(self, phone_brand, phone_model, subscriber_number):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.subscriber_number = subscriber_number

    def say_phone_brand(self):
        print(self.phone_brand)

    def say_pphone_model(self):
        print(self.phone_model)

    def say_subscriber_number(self):
        print(self.subscriber_number)