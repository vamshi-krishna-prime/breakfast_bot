import time
options= ["waffles", "pancakes", "yes", "no"]
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def valid_input(prompt, options):
    while True:
        response= input(prompt).lower()
        for option in options:
            if option in response:
                return response
        print_pause("Sorry, I don't understand")

def Intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

def get_order():
    response = valid_input("Please place your order. "
                           "Would you like waffles or pancakes?\n",
                           options)
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")

def order_again():
    order_again = valid_input("Would you like to place another order? "
                              "Please say 'yes' or 'no'.\n",
                              options)
    if "no" in order_again:
        print_pause("OK, goodbye!")
#         break
    elif "yes" in order_again:
        print_pause("Very good, I'm happy to take another order.")
        get_order()

Intro()
get_order()
order_again()
