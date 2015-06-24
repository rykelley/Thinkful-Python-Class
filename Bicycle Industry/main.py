__author__ = 'Ryan'


import random
from bicycles import Bicycle, BicycleShop, Customers


bikes = [
    Bicycle("Trek Remedy", 75, 100), Bicycle("Yeti ASR", 70, 150),
    Bicycle("Niner Rip9 ", 50, 250), Bicycle("Trek Stache", 90, 350),
    Bicycle("Santa Cruz Bantam", 65, 100), Bicycle("Trek X-Caliber", 75, 550)
    ]

shop = BicycleShop("Surplus Cycles", 20, bikes)



customers = [Customers("Ryan", 200), Customers("Jim", 500), Customers("Megan", 1000)]

for Customers in customers:

    bikes = ", ".join(bike.model for bike in shop.filter(Customers.money))
    print(Customers.name, "|", bikes)



print(shop)



template = "{0} bought the {1} at ${2}, and they have ${3} left over."

for Customers in customers:

    affordable = shop.filter(Customers.money)
    shop.sell(random.choice(affordable), Customers)

    print(template.format(Customers.name, Customers.bike.model,Customers.bike.price, Customers.money))


print(shop)
