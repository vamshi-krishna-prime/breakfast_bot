import time

def print_pause(list, delay):
    for index in range(len(intro)):
        print(intro[index])
        time.sleep(delay)

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

intro= ["Hello! I am Bob, the Breakfast Bot.",
        "Today we have two breakfasts available.",
        "The first is waffles with strawberries and whipped cream.",
        "The second is sweet potato pancakes with butter and syrup."]
print_pause(intro, 2)

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
