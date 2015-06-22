__author__ = 'Ryan'

class Bicycle(object):

    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost

    def __repr__(self):

        template = "The {0} | Cost: ${1}, Weight: {2}pounds"
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


class Customers(object):

    def __init__(self, name, money):
        self.name = name
        self.money = money

