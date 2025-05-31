class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(self.item_name + ": " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(total_cost))

    def print_description(self):
        print(self.item_name + ": " + self.item_description)
    
class ShoppingCart:
    def __init__(self, customer_name: str, current_date: str):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)

    def remove_item(self, itemName: str):
        foundItem = self.find_item_by_name(itemName)
        if (foundItem is None):
            print("Item not found in cart. Nothing removed.")
        else:
            self.cart_items.remove(foundItem)

    def find_item_by_name(self, itemName: str) -> ItemToPurchase:
        foundItem = None
        for item in self.cart_items:
            if (item.item_name == itemName):
                foundItem = item
                break
        return foundItem

    def modify_item(self, item: ItemToPurchase):
        foundItem = self.find_item_by_name(item.item_name)
        if (foundItem is None):
            print("Item not found in cart. Nothing modified.")
        else:
            if (item.item_name != "none"):
                foundItem.item_name = item.item_name
            if (item.item_description != "none"):
                foundItem.item_description = item.item_description
            if (item.item_price != 0.0):
                foundItem.item_price = item.item_price
            if (item.item_quantity != 0):
                foundItem.item_quantity = item.item_quantity
        
    def get_num_items_in_cart(self) -> int:
        return sum(item.item_quantity for item in self.cart_items)
    
    def get_cost_of_cart(self) -> float:
        total = 0.0
        for item in self.cart_items:
            total += item.item_price * item.item_quantity
        return total
    
    def print_total(self): 
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Number of Items: " + str(self.get_num_items_in_cart()))
        for item in self.cart_items:
            item.print_item_cost()
        print("Total: $" + str(self.get_cost_of_cart()))
        print()
    
    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_description()
        print()
        
class MenuItem:
    def __init__(self, key: chr, description: str, func: callable):
        self.key = key
        self.description = description
        self.func = func

    def run(self) -> bool:
        return self.func()


def get_item(itemNum: int) -> ItemToPurchase:
    print("Item " + str(itemNum) + ": ")
    item = ItemToPurchase()
    item.item_name = input("Enter the item name: ")
    item.item_description = input("Enter the item description: ")
    item.item_price = float(input("Enter the item price: "))
    item.item_quantity = int(input("Enter the item quantity: ")) 
    return item 

def print_menu(shoppingCart: ShoppingCart):
    menuItems = [
        MenuItem('a', "Add item to cart", lambda: add(shoppingCart)),
        MenuItem('r', "Remove item from cart", lambda: remove(shoppingCart)),
        MenuItem('c', "change item quantity", lambda: change_quantity(shoppingCart)),
        MenuItem('i', "Output items' descriptions", lambda: output_descriptions(shoppingCart)),
        MenuItem('o', "Output shopping cart", lambda: output_cart(shoppingCart)),
        MenuItem('q', "Quit", lambda: quit(shoppingCart))
    ]

    isRunning = True
    while isRunning:
        print("MENU")
        for menuItem in menuItems:
            print(str(menuItem.key) + " - " + menuItem.description)

        validOption = False
        while (validOption == False):
            option = input("Choose an option: ")[0]
            for item in menuItems:
                if (item.key == option):
                    validOption = True
                    isRunning = item.run()
                    break
        
            if (validOption == True): break
            else: 
                print("Invalid Option")
                print()

def add(cart: ShoppingCart) -> bool:
    print("ADD ITEM TO CART")
    cart.add_item(get_item(1))
    print()
    return True
def remove(cart: ShoppingCart) -> bool:
    print("REMOVE ITEM FROM CART")
    itemName = input("Enter name of item to remove: ")
    cart.remove_item(itemName)
    print()
    return True
def change_quantity(cart: ShoppingCart) -> bool:
    print("CHANGE ITEM QUANTITY")
    itemName = input('Enter the item name:')
    quantity = int(input('Enter the new quantity: '))
    item = cart.find_item_by_name(itemName)
    if (item == None):
        print("Failed to find item.")
    else:
        modify = ItemToPurchase()
        modify.item_name = itemName
        modify.item_quantity = quantity
        cart.modify_item(modify)
    print()
    return True
def output_descriptions(cart: ShoppingCart) -> bool:
    print("OUTPUT ITEMS' DESCRIPTIONS")
    cart.print_descriptions()
    print()
    return True
def output_cart(cart: ShoppingCart) -> bool:
    print("OUTPUT SHOPPING CART")
    cart.print_total()
    print()
    return True
def quit(cart: ShoppingCart) -> bool:
    print("Goodbye")
    print()
    return False

name = input("Enter customer's name:")
date = input("Enter today's date:")
shoppingCart = ShoppingCart(name, date)
print("Customer name: " + name)
print("Today's date: " + date)

print_menu(shoppingCart)