__author__ = 'Ryan'

class Bicycle(object):

    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost



class BicycleShop(object):

    def __init__(self, name, inventory, margin, profit ):

        self.name = name
        self.inventory = inventory
        self.margin = margin
        self.profit = profit


class Customers(object):

    def __init__(self, money, credit):
        self.money = money
        self.credit = credit
