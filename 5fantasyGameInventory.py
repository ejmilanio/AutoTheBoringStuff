"""
Project: Fantasy Game Inventory

Dictionary in which...
key = str naming item
value = int of how much of that item is held

"""

playerInventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
    }

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, amount in inventory.items():
        item_total += amount
        print('    ' + str(amount) + ' ' + str(item))
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)
        inventory.get(i, 1)
    pass

inv = addToInventory(playerInventory, dragonLoot)

print(displayInventory(playerInventory))

