def start_game():
    print("Welcome to Escape the Prison!")
    print("Your goal is to escape without getting caught. Choose wisely!")
    
    cell_action()

def cell_action():
    print("\nYou wake up in your prison cell. The door is locked, but you see a vent above and hear footsteps outside.")
    print("1. Shout for help")
    print("2. Try to open the vent")
    print("3. Wait and listen")

    choice = input("What do you do? (1/2/3): ")

    if choice == "1":
        print("\nYou shout for help, but a guard hears you and comes to check. You're caught! Game Over.")
    elif choice == "2":
        print("\nYou manage to open the vent and crawl into the air ducts.")
        vent_action()
    elif choice == "3":
        print("\nYou wait and listen. A guard passes by, and you hear him muttering about a missing key.")
        print("You notice a key hanging from his belt.")
        key_action()
    else:
        print("\nInvalid choice. Try again.")
        cell_action()

def vent_action():
    print("\nYou crawl through the vents and reach a junction.")
    print("1. Go left (towards the kitchen)")
    print("2. Go right (towards the armory)")

    choice = input("Which way do you go? (1/2): ")

    if choice == "1":
        print("\nYou reach the kitchen and find a knife. A cook sees you and raises the alarm. Game Over.")
    elif choice == "2":
        print("\nYou reach the armory and find a guard's uniform. You put it on and continue exploring the prison.")
        armory_action()
    else:
        print("\nInvalid choice. Try again.")
        vent_action()

def key_action():
    print("\nYou decide to take the key from the guard.")
    print("1. Pickpocket the key quietly")
    print("2. Distract the guard and grab the key")

    choice = input("How do you proceed? (1/2): ")

    if choice == "1":
        print("\nYou quietly take the key and unlock your cell. You sneak out and find yourself in a hallway.")
        hallway_action()
    elif choice == "2":
        print("\nYou try to distract the guard, but he notices you and calls for backup. You're caught! Game Over.")
    else:
        print("\nInvalid choice. Try again.")
        key_action()

def hallway_action():
    print("\nYou are in a dimly lit hallway. There are two paths ahead.")
    print("1. Go left (towards the warden's office)")
    print("2. Go right (towards the exit)")

    choice = input("Which way do you go? (1/2): ")

    if choice == "1":
        print("\nYou sneak into the warden's office and find a map of the prison. It shows a secret tunnel leading outside.")
        secret_tunnel_action()
    elif choice == "2":
        print("\nYou head towards the exit but encounter a locked door with a keypad. Without the code, you can't proceed. You're caught by guards! Game Over.")
    else:
        print("\nInvalid choice. Try again.")
        hallway_action()

def armory_action():
    print("\nDressed as a guard, you move freely through the prison. You overhear two guards talking about a supply truck leaving soon.")
    print("1. Head to the truck loading area")
    print("2. Investigate the warden's office")

    choice = input("Where do you go? (1/2): ")

    if choice == "1":
        print("\nYou reach the truck loading area and hide in the back of a supply truck. The truck leaves the prison. You escaped! Congratulations!")
    elif choice == "2":
        print("\nYou sneak into the warden's office and find a map of the prison. It shows a secret tunnel leading outside.")
        secret_tunnel_action()
    else:
        print("\nInvalid choice. Try again.")
        armory_action()

def secret_tunnel_action():
    print("\nYou follow the map to the secret tunnel. It's dark and filled with obstacles.")
    print("1. Use a flashlight you found in the armory")
    print("2. Proceed carefully in the dark")

    choice = input("How do you proceed? (1/2): ")

    if choice == "1":
        print("\nUsing the flashlight, you navigate the tunnel safely and find an exit leading to freedom. You escaped! Congratulations!")
    elif choice == "2":
        print("\nIn the dark, you trip over a rock and make noise. Guards discover the tunnel and catch you. Game Over.")
    else:
        print("\nInvalid choice. Try again.")
        secret_tunnel_action()

# Start of the game
start_game()
