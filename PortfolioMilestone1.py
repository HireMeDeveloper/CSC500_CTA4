class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(self.item_name + ": " + str(self.item_quantity) + " @ $" + str(self.item_price) + " = $" + str(total_cost))
    

def get_item(itemNum: int) -> ItemToPurchase:
    print("Item " + str(itemNum) + ": ")
    item = ItemToPurchase()
    item.item_name = input("Enter the item name: ")
    item.item_price = float(input("Enter the item price: "))
    item.item_quantity = int(input("Enter the item quantity: ")) 
    return item 

itemNumber = 2
items = [ItemToPurchase] * 2

for i in range(0, itemNumber):
    items[i] = get_item(i)

total = 0
for item in items:
    total += (item.item_quantity * item.item_price)
    item.print_item_cost()

print("Total: $" + str(total))