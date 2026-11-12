next = True




while next == True:
    total = 0
    selected = False
    confirm = False
    correct = False

    print("Items: 501 - crisps, 502 - chocolate, 503 - cereal bar, 504 - water")

    while selected == False:

        item = input("Select item:").lower()
        item = item.replace(" ", "")
        if item == "501":
            item = "crisps"
        if item == "502":
            item = "chocolate"
        if item == "503":
            item = "cereal bar"
        if item == "504":
            item = "water"

        if item == "crisps":
            price = 60
            selected = True
        elif item == "chocolate":
            price = 80
            selected = True
        elif item == "cereal bar":
            price = 50
            selected = True
        elif item == "water":
            price = 90
            selected = True 
        else:
            print("no such item")

        if selected == True:
            print("You have selected", item, "it costs", price)
            decision = input("Confirm? (yes or no)").lower()
            decision = decision.replace(" ", "")
            if decision == "yes":
                selected = True
            elif decision == "y":
                selected = True
            elif decision == "true":
                selected = True
            elif decision == "confirm":
                selected = True
            elif decision == "t":
                selected = True
            else:
                selected = False


    while total < price:
        coin = input("enter money ")
        coin = coin.replace(" ", "")
        while coin.isdigit() == False or int(coin) != 10 and int(coin) != 20 and int(coin) != 50 and int(coin) != 100 and int(coin) != 0:
            print("Invalid coins.")
            print(coin)
            coin = input("enter money ")
           
        
        coin = int(coin)
        total = total + coin
    change = total - price

    print(item)
    print(change,"P")
    print("Next person:")