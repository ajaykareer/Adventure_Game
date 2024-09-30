import random

def choose_direction():
    directions = ["up", "down", "left", "right"]
    while True:
        user_direction = input("\n****** Choose a direction (⬆️ up, ⬇️ down, ⬅️ left, ➡️ right) or type 'quit' to exit the game: ******\n").lower()
        if user_direction in directions:
            return user_direction
        elif user_direction == 'quit':
            print("👋 You chose to quit. Game over!")
            exit()
        else:
            print("❌ Invalid input. Please choose a valid direction or type 'quit'.")

def choose_weapon():
    weapons = ["axe", "sword", "brick", "ladder", "bow", "shield"]
    while True:
        print("\n****** Choose a weapon: 🪓 axe, ⚔️ sword, 🧱 brick, 🪜 ladder, 🏹 bow, or 🛡️ shield ******\n")
        user_weapon = input("****** Enter your weapon choice: ******\n").lower()
        if user_weapon in weapons:
            return user_weapon
        else:
            print("❌ Invalid weapon choice. Please select a valid weapon.")

def choose_puzzle_answer():
    answers = {
        "What has to be broken before you can use it?": "egg",
        "I’m tall when I’m young, and I’m short when I’m old. What am I?": "candle",
        "What can you catch but not throw?": "cold",
        "What is always in front of you but can’t be seen?": "future"
    }
    puzzle = random.choice(list(answers.keys()))
    print(f"\n****** 🤔 Riddle: {puzzle} ******\n")
    answer = input("****** Your answer: ******\n").lower()
    if answer == answers[puzzle]:
        return True
    else:
        return False

def level_two():
    print("\n🌲 ****** Level 2: The Forest of Mystery ****** 🌲")
    print("You find yourself in a dark forest with paths leading in different directions.")
    direction = choose_direction()

    if direction == "left":
        print("🦕 You encounter a sleeping dragon! Choose your weapon wisely.")
        weapon = choose_weapon()
        if weapon == "bow":
            print("🏹 You shoot the dragon from a distance and safely pass by!")
        else:
            print("🔥 The dragon wakes up and attacks you. You couldn't survive.")
            print("💀 Game Over!")
            exit()
    elif direction == "right":
        print("🧙‍♂️ You encounter a magical barrier. Solve the riddle to pass.")
        if choose_puzzle_answer():
            print("✨ You solved the riddle and the barrier disappears!")
        else:
            print("❌ Wrong answer! The magical barrier traps you.")
            print("💀 Game Over!")
            exit()
    elif direction == "up":
        print("🔥 You encounter a pit of fire. Choose your tool wisely.")
        weapon = choose_weapon()
        if weapon is "ladder":
            print("🪜 You use the ladder to cross the fire safely!")
        else:
            print(f"❌ The {weapon} doesn't help here. You fall into the fire.")
            print("💀 Game Over!")
            exit()
    else:
        print("🌀 You are lost in the forest and cannot continue.")
        print("💀 Game Over!")
        exit()

def level_three():
    print("\n🏰 ****** Level 3: The Castle of Shadows ****** 🏰")
    print("You enter a dark castle, and you must defeat the guards to reach the treasure.")

    print("⚔️ You encounter a guard blocking the treasure room. Choose your weapon!")
    weapon = choose_weapon()
    if weapon in ["sword", "axe"]:
        print(f"🛡️ You fight bravely with your {weapon} and defeat the guard!")
        print("As you reach for the treasure, a final puzzle blocks your way.")
        if choose_puzzle_answer():
            print("🏆 You solved the puzzle and claim the treasure! 🎉 Congratulations, you win!")
            play_again()
        else:
            print("❌ Wrong answer! The treasure disappears before your eyes.")
            print("💀 Game Over!")
            play_again()
    else:
        print(f"❌ The {weapon} is not effective against the guard. You are defeated.")
        print("💀 Game Over!")
        play_again()

def next_challenge():
    print("\n🎉 ****** You survived the first challenge! ******")
    print("Now, you're faced with a new obstacle. Make the right choices to proceed.")
    level_two()  # Proceed to Level 2
    level_three()  # Proceed to Level 3

def left_path():
    print("\n⬅️ ****** You chose the left path. You encounter a group of alligators blocking your way. 🐊 ******")
    weapon = choose_weapon()
    if weapon == "axe":
        print("🪓 You use the axe to fight off the alligators and survive!")
        next_challenge()
    else:
        print(f"❌ Oh no! You chose the {weapon}. The alligators are too strong, and you couldn't survive.")
        print("💀 Game Over!")
        play_again()

def right_path():
    print("\n➡️ ****** You chose the right path. You encounter a locked door. 🚪 ******")
    weapon = choose_weapon()
    if weapon == "ladder":
        print("🪜 You cleverly use the ladder to climb over the door and proceed!")
        next_challenge()
    else:
        print(f"❌ The {weapon} is not useful here. You're stuck at the door.")
        print("💀 Game Over!")
        play_again()

def up_path():
    print("\n⬆️ ****** You chose the up path. You find yourself facing a tall mountain. 🏔️ ******")
    weapon = choose_weapon()
    if weapon == "sword":
        print("⚔️ You use the sword to carve steps into the mountain and climb up!")
        next_challenge()
    else:
        print(f"❌ The {weapon} doesn't help here. You can't climb the mountain.")
        print("💀 Game Over!")
        play_again()

def down_path():
    print("\n⬇️ ****** You chose the down path. You fall into a deep pit filled with snakes! 🐍 ******")
    weapon = choose_weapon()
    if weapon == "brick":
        print("🧱 You throw the brick at the snakes and manage to scare them away!")
        next_challenge()
    else:
        print(f"❌ The {weapon} is useless here. The snakes are too much to handle.")
        print("💀 Game Over!")
        play_again()

def play_again():
    while True:
        choice = input("\n****** Do you want to play again? (yes/no): ******\n").lower()
        if choice == 'yes':
            start_game()
        elif choice == 'no':
            print("👋 Thanks for playing! See you next time!")
            exit()
        else:
            print("❌ Invalid choice. Please enter 'yes' or 'no'.")

def start_game():
    print("🎮 ****** Welcome to the ultimate adventure game! ******")
    print("🔥 ****** This game is created by Ajay Kareer ****** 🔥")
    print("Your mission is to survive multiple challenges, defeat enemies, and solve puzzles.")
    
    while True:
        direction = choose_direction()
        
        if direction == "left":
            left_path()
        elif direction == "right":
            right_path()
        elif direction == "up":
            up_path()
        elif direction == "down":
            down_path()

if __name__ == "__main__":
    start_game()
