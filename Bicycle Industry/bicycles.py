__author__ = 'Ryan'

class Bicycle(object):

    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

    def __repr__(self):

        template = "The {0} | Cost: ${1}, Weight: {2}Pounds"
        return template.format(self.model, self.cost, self.weight)



class BicycleShop(object):

    def __init__(self, name, inventory, margin, profit):

        self.name = name
        self.inventory = []
        self.margin = margin
        self.profit = 0

        for bike in inventory:

            bike.markup = int((bike.cost / 100.0) * self.margin)
            bike.price = bike.cost + bike.markup
            self.inventory[bike.model] = bike

    def __repr__(self):

        template = "\n{0} (${1} profit)\n{2}\n"
        bikes = "\n".join(str(bike) for bike in self.inventory.values())
        return template.format(self.name, self.profit, bikes)

    def filter(self, budget):

        bikes = self.inventory.values()
        return [ bike for bike in bikes if bike.price <= budget ]

    def sell(self, bike, customer):

        customer.bike = bike
        customer.fund -= bike.price
        self.profit += bike.markup
        del self.inventory[bike.model]


class Customers(object):

    def __init__(self, name, money):
        self.name = name
        self.money = money

