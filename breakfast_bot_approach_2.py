import time

def compare(longstring, shortstring):
    index=0
    longstring=longstring.lower()
    while index < len(longstring):
        if longstring[index: index + len(shortstring)] == shortstring:
            return True
        index += 1
    return False

def take_order():
    while True:
        response= input("Plaese place your order. "
                        "Would you like waffles or pancakes?")
        if compare(response, "waffles") == True:
            result= ("waffles it is!\n"
                     "Your order will be ready shortly.")
            return result
        elif compare(response, "pancakes") == True:
            result= ("pancakes it is!\n"
                     "Your order will be ready shortly.")
            return result
        else:
            print("sorry, I don't understand")

time.sleep(1)
print("Hello! I am Bob, the Breakfast Bot.\n"
    "Today we have two breakfasts available.\n"
    "The first is waffles with strawberries and wipped cream.\n"
    "The second is sweet potato pancakes with butter and syrup.")
while True:
    print(take_order())
    another_response= input("Would you like to place another order?"
          " Please say 'yes' or 'no'.")
    if compare(another_response, "yes") == True:
        print("Very good, I'm happy to take another order.")
    elif compare(another_response, "no") == True:
        print("OK, goodbye!")
        break
    else:
        print("sorry, I don't understand")
