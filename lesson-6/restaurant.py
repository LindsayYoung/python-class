class Restaurant(object):

    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.items_ordered = []


    def print_menu(self):
        """ Print the entire menu. Example:

            PB&J ... 1.99
            Cheeseburger ... 3.75
        """
        # YOUR CODE HERE


    def has_item(self, item):
        """ Check if the restaurant has an item by the given name """
        # YOUR CODE HERE
        return False


    def take_order(self, item, money):
        """ Take an order for item, given a certain amount of money.

            If the item doesn't exist, print "Sorry, we don't have <ITEM>".

            If the cost of the item is greater than the money provided, print
            "Sorry, <ITEM> costs <COST>" (eg. "Sorry, PB&J costs 1.99")

            If the order is successful, record the order and return the person's
            change (money - price) to them.
        """
        # YOUR CODE HERE
        return money


    def take_big_order(self, items, money):
        """ Works just like take_order but takes an order for multiple items

            Error if money cannot pay for all items:
                "Total price of items is <COST>, you paid <MONEY>"

            Error if any items are not on menu:
                "Sorry, we don't have <ITEM>"

            In both error cases, no order should take place (no money exchanged)

            If the order is successful, record the order and return the person's
            change (money - price) to them.
        """
        # YOUR CODE HERE
        return money


    def print_sales_report(self):
        """ Print daily sales report. Example:

            PB&J : 2
            Cheeseburger : 5
            Milkshake : 3
            -----
            Total: $27.23
        """
        # YOUR CODE HERE


if __name__ == '__main__':

    menu = {
        'ShackBurger': 4.85,
        'Fries': 2.85,
        'Shake': 5.00,
    }

    r = Restaurant('Shake Shack', menu)

    print("")

    print("------------\nThe menu\n------------")
    r.print_menu()

    print("")

    print("%s has Fries: %s" % (r.name, r.has_item('Fries')))
    print("%s has BBQ: %s" % (r.name, r.has_item('BBQ')))

    print("")

    change = r.take_order('ShackBurger', 10.00)
    if change:
        print("Ordered a ShackBurger and got %0.2f in change" % change)

    order = ('ShackBurger', 'ShackBurger', 'Fries', 'Shake')
    change = r.take_big_order(order, 50.00)
    if change:
        print("Ordered %s and got %0.2f in change" % (", ".join(order), change))

    print("")

    print("------------\nSales Report\n------------")
    r.print_sales_report()


    # test some error cases

    print("")
    print("------------\nTest Errors\n------------")
    print "\t%0.2f in change" % r.take_order('Kale Salad', 5.00)
    print "\t%0.2f in change" % r.take_order('ShackBurger', 0.25)
    print "\t%0.2f in change" % r.take_big_order(('ShackBurger', 'Kale Salad'), 5.00)
    print "\t%0.2f in change" % r.take_big_order(('ShackBurger', 'Fries'), 5.00)
