def my_shopping_advisor():
    # create a list and dictionary as containers
    shopping_history = []
    shopping_item = {}

    quit_shopping = False
    while not quit_shopping:
        response = input("Do you want to add an item to your list? Type 'a' to Add, 'q' to quit or 's' for other "
                         "actions: \n").lower()

        if response == 'q':
            quit_shopping = True
        elif response == 'a':
            quit_shopping = False
            name = input("Enter name of item: \n")
            quantity = int(input("Enter the quantity: \n"))
            cost = float(input("Enter cost per item: \n"))

            shopping_item = {'item_name': name, 'item_quantity': quantity, 'item_cost': cost}
            shopping_history.append(shopping_item)
        elif response != 'q' and response != 'c' and response != "s":
            print("Invalid input...")
        else:
            while response == 's':
                print("""
                            ___ Other Actions ___
                            1. View shopping list
                            2. Remove items from shopping list
                            3. Check if an item is on the shopping list
                            4. Count the number of items on the shopping list
                            5. Clear the shopping list 
                            6. Exit       

                            """)
                selection = input("Make a selection: ")

                def view_list():
                    print("### Your Shopping List ###")
                    for item in shopping_history:
                        print("* %d %s" % (item['item_quantity'], item['item_name']))

                def remove_items():
                    item_to_remove = input("Enter the name of the item you wish to remove: \n")
                    for item in shopping_history:
                        if item['item_name'] == item_to_remove:
                            shopping_history.remove(item)
                            print(f"{item_to_remove} has been removed from the list...")

                def item_checker():
                    item_to_check = input("Enter the name of the item you wish to check for: \n")
                    found_item = []
                    for item in shopping_history[:]:
                        if item['item_name'] == item_to_check:
                            found_item.append(item_to_check)
                            if item_to_check in found_item:
                                print(f"Yes, {item_to_check} is on the list...")

                def counter():
                    print(f"There are {len(shopping_history)} items on your shopping list...")

                def clear_list():
                    shopping_history.clear()
                    print("The shopping list has been cleared...")

                if selection == "1":
                    view_list()
                elif selection == "2":
                    remove_items()
                elif selection == "3":
                    item_checker()
                elif selection == "4":
                    counter()
                elif selection == "5":
                    clear_list()
                elif selection == "6":
                    break
    # create a grand_total variable
    grand_total = 0

    # calculate the total of each shopping item
    for item in shopping_history:
        item_total = item['item_quantity'] * item['item_cost']
        print("%d %s @ Ksh %.2f each - Ksh %.2f" % (
            item['item_quantity'], item['item_name'], item['item_cost'], item_total))
        grand_total += item_total
    print("Grand Total: Ksh %.2f" % grand_total)
    return " "


print(my_shopping_advisor())
