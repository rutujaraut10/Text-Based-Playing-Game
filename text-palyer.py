class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.enemy = None

    def set_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def set_enemy(self, enemy):
        self.enemy = enemy


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} is defeated!"
        return f"{self.name} has {self.health} health left."


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100

    def take_item(self, item):
        self.inventory.append(item)
        return f"{item.name} added to your inventory."

    def fight(self, enemy):
        if not enemy:
            return "There's no one to fight here."
        damage = 20
        return enemy.take_damage(damage)


# Game setup
room1 = Room("Entrance Hall", "A large hall with a grand staircase.")
room2 = Room("Armory", "A room filled with ancient weapons.")
room3 = Room("Treasure Room", "A room glittering with gold and jewels.")

room1.set_exit("north", room2)
room2.set_exit("south", room1)
room2.set_exit("east", room3)

sword = Item("Sword", "A sharp and shiny sword.")
room2.add_item(sword)

goblin = Enemy("Goblin", 50)
room3.set_enemy(goblin)

player = Player("Hero")

# Game loop
current_room = room1

while True:
    print(f"\nYou are in the {current_room.name}.")
    print(current_room.description)
    if current_room.items:
        print("Items in the room:")
        for item in current_room.items:
            print(f"- {item.name}: {item.description}")
    if current_room.enemy:
        print(f"You encounter a {current_room.enemy.name}!")

    command = input("\nWhat do you want to do? ").lower()

    if command.startswith("go "):
        direction = command.split(" ")[1]
        if direction in current_room.exits:
            current_room = current_room.exits[direction]
        else:
            print("You can't go that way.")

    elif command.startswith("take "):
        item_name = command.split(" ")[1]
        item = next((i for i in current_room.items if i.name.lower() == item_name), None)
        if item:
            print(player.take_item(item))
            current_room.items.remove(item)
        else:
            print("There's no such item here.")

    elif command == "fight":
        if current_room.enemy:
            print(player.fight(current_room.enemy))
            if current_room.enemy.health <= 0:
                current_room.enemy = None
        else:
            print("There's no one to fight here.")

    elif command == "quit":
        print("Thanks for playing!")
        break

    else:
        print("I don't understand that command.")
