import time

def print_pause(message):
    print(message)
    time.sleep(2)

def order():
    while True:
        response = input("Please place your order. "
                         "Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(2)
            break
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)

print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

while True:
    order()
    print("Your order will be ready shortly.")
    time.sleep(2)
    while True:
        order_again= input("Would you like to place another order?"
                           " Please say 'yes' or 'no'.\n").lower()
        if "yes" in order_again:
            print("Very good, I'm happy to take another order.")
            time.sleep(1)
            break
        elif "no" in order_again:
            print("OK, goodbye!")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
    if "no" in order_again:
        break
