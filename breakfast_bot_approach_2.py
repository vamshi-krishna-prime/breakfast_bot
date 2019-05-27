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
        response= input("Please place your order. "
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

def another_order():
    global loop_breaker
    while True:
        another_response= input("Would you like to place another order?"
              " Please say 'yes' or 'no'.\n")
        if compare(another_response, "yes") == True:
            another_result= ("Very good, I'm happy to take another order.")
            return another_result
        elif compare(another_response, "no") == True:
            another_result= ("OK, goodbye!")
            loop_breaker = "activate"
            return another_result
        else:
            print("sorry, I don't understand")

print("Hello! I am Bob, the Breakfast Bot.\n"
    "Today we have two breakfasts available.\n"
    "The first is waffles with strawberries and wipped cream.\n"
    "The second is sweet potato pancakes with butter and syrup.")
loop_breaker = ""
while loop_breaker != "activate":
    print(take_order())
    print(another_order())
