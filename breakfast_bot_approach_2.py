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
                        "Would you like waffles or pancakes?\n")
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


print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(1)
print("Today we have two breakfasts available.")
time.sleep(1)
print("The first is waffles with strawberries and wipped cream.")
time.sleep(1)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(1)
while True:
    print(take_order())
    time.sleep(1)
    another_response= input("Would you like to place another order?"
          " Please say 'yes' or 'no'.\n")
    if compare(another_response, "yes") == True:
        print("Very good, I'm happy to take another order.")
        time.sleep(1)
    elif compare(another_response, "no") == True:
        print("OK, goodbye!")
        time.sleep(1)
        break
    else:
        print("sorry, I don't understand.")
        time.sleep(1)
