from address import Address
from mailing import Mailing

to_address = Address("132345", "Волгоград", "Сталинградская", "34", "543")
from_address = Address("567383", "Магадан", "Николаевская", "3", "67")

mailing = Mailing(to_address, from_address, 1500, "К59493732327")

print(mailing)