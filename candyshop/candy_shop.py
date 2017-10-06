# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"

class CandyShop(object):

    def __init__(self, candy_type):
        self.inventory = []
        self.sugar = 0
        self.price = 0
        self.income = 0
        self.amount_of_sugar = 0
        self.raise_rate = 0
        self.candy_type = candy_type

    def create_sweets(self, sweets):
        self.sweets.append(sweet)
        return ("Inventory: {}, Income: {}, Sugar: {}".format(lent(self.inventory), self.income, self.sugar))

    def sell(self):
        pass

    def raise_prices(self):
        self.price *= self.raise_rate

    def buy_sugar(self):
        if self.amount_of_sugar > self.sugar:
            self.amount_of_sugar += self.sugar
            self.income -= self.price


class Sweets(object):
    def __init__(self):
        self.sugar = 10
        self.price = 20
        self.candy_type == 'sweet'
        
        self.sugar = 5
        self.price = 10


candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
print(candy_shop
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 285gr"
candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:35, Sugar: 285gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 315gr"
