# Objects

Objects are things in Python. We'll go over them in class.

## Exercises

Congratulations! You are now a restaurateur. All of the existing restaurant management software out there is garbage, so since you know how to write code in Python, you're going to custom build a system for yourself!

### In Class

1. The first method we'll implement, *print_menu*, will print out all of the menu items and their prices.

1. The next method we'll be writing is the *has_item* method. It should simply return True or False depending on if a particular item is on the menu.

1. *take_order* is going to be one of the more challenging methods. It takes an item name and an amount of money and can do one of three things:
    * print an "item doesn't exist" message
    * print a "not enough money" message
    * record the transaction and return the amount of change

1. Implement *take_big_order* which accepts a list of items to order.

1. *print_sales_report* prints out the total number of each item ordered and a total amount earned so far.


### Homework

1. Add an inventory for each item and adjust the *has_item* and *take_order* methods accordingly.

1. Add a LawAbidingRestaurant subclass of Restaurant that accepts an additional parameter to *\_\_init\_\_* that takes a tax percentage.
    * Override *print_menu* to include totals with tax, example:
        
        `PB&J ........ 1.99 (2.09)`
        
    * Override *take_order* to charge the tax rate
