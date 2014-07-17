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

        for item, price in self.menu.items():
            print("%s ... %0.2f" % (item, price))


    def has_item(self, item):
        """ Check if the restaurant has an item by the given name """

        return item in self.menu


    def take_order(self, item, money):
        """ Take an order for item, given a certain amount of money.

            If the item doesn't exist, print "Sorry, we don't have <ITEM>".

            If the cost of the item is greater than the money provided, print
            "Sorry, <ITEM> costs <COST>" (eg. "Sorry, PB&J costs 1.99")

            If the order is successful, record the order and return the person's
            change (money - price) to them.
        """

        if not self.has_item(item):
            print("Sorry, we don't have %s" % item)
            return money

        price = self.menu[item]

        if price > money:
            print("Sorry, %s costs %0.2f" % (item, price))
            return money

        self.items_ordered.append(item)

        return money - price


    def take_big_order(self, items, money):
        """ Works just like take_order but takes an order for multiple items

            Error if money cannot pay for all items:
                "Total price of items is <COST>, you paid <MONEY>"

            Error if any items are not on menu:
                "Sorry, we don't have <ITEM>"

            In either error case, no order should take place (no money exchanged)

            If the order is successful, record the order and return the person's
            change (money - price) to them.
        """

        for item in items:
            if not self.has_item(item):
                print("Sorry, we don't have %s" % item)
                return money

        total_price = sum(self.menu[item] for item in items)

        if total_price > money:
            print("Total price of items is %0.2f, you paid %0.2f" % (total_price, money))
            return money

        self.items_ordered.extend(items)

        return money - total_price


    def print_sales_report(self):
        """ Print daily sales report. Example:

            PB&J : 2
            Cheeseburger : 5
            Milkshake : 3
            -----
            Total: $27.23
        """
        total_price = 0
        report = {}

        for item in self.items_ordered:

            price = self.menu[item]

            if item not in report:
                report[item] = 0

            report[item] += 1
            total_price += price

        for item, count in report.items():
            print("%s : %d" % (item, count))
        print("-----")
        print("Total: $%0.2f" % total_price)


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
        print("Ordered a ShackBurger, paid 10.00 and got %0.2f in change" % change)

    order = ('ShackBurger', 'ShackBurger', 'Fries', 'Shake')
    change = r.take_big_order(order, 50.00)
    if change:
        print("Ordered %s, paid 50.00 and got %0.2f in change" % (", ".join(order), change))

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
