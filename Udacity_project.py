import time
import random


"""A text-based dragon adventure game where players collect points to win."""
points = []


"------------------------- Print_pause ---------------------------"


def print_pause(x):
    """Print a message and pause for 1 second."""
    print(x)
    time.sleep(1)


"------------------------- tools ---------------------------"


def random_tool():
    """Choose a random magical tool and update player's points."""
    tools = [
        {"Name": "Wand of ice", "Points": 4, "Accuracy": "High"},
        {"Name": "Amulet of fire resistance", "Points": 3, "Accuracy": "Mid"},
        {"Name": "Potion of speed", "Points": 2, "Accuracy": "Low"}
    ]
    print_pause("Magic tools:")
    print_pause("")
    for tool in tools:
        print_pause(f"Tool: `{tool['Name']}` points: `{tool['Points']}` and "
                    f"accuracy: `{tool['Accuracy']}`")
    use_tool = random.choice(tools)
    tool_name = use_tool["Name"]
    tool_points = use_tool["Points"]
    print("")
    print_pause(f"You have ` {tool_name} ` tool with {tool_points} bonus .")
    bonus = tool_points
    points.append(bonus)
    total_points = sum(points)
    print(f"Total points {total_points}")


"------------------------- Land ---------------------------"


def land():
    """Start the game by choosing between the cave or the bridge."""
    points.append(0)
    total_points = sum(points)
    print_pause(" ")
    print_pause("You are in a land full of dragons.")
    print_pause("In front of you, you see a cave and a bridge.")
    print_pause("You need to collect 10 points at least to win.")
    print_pause("1.In the cave there is a friendly dragon and...")
    print_pause("Will share his treasure with you.")
    print_pause("2.On the bridge there is a dragon that is maybe..")
    print_pause("Hungry, and will eat you.")
    print_pause("")
    print_pause(f"Your points --> {total_points}")
    "------------------------- Option ---------------------------"
    def option():
        """Make player choose between (cave or bridge)."""
        option = input("In which way will you go? (1 or 2): ")
        while option:
            if option == "1":
                cave_1()
                break
            elif option == "2":
                bridge()
                break
            else:
                print_pause("Please choose (1 or 2).")
                option = input("In which way will you go? (1 or 2): ")

    option()


"------------------------- Cave_1 ---------------------------"


def cave_1():
    """Handle the cave scenario with the friendly dragon."""
    print_pause(" ")
    return_to_cave()
    print_pause("### The Cave ###")
    print_pause("You approach the cave...")
    print_pause("It is dark and spooky...")
    print_pause("A large dragon jumps out in front of you!")
    action = input("Run or talk? (run/talk): ")
    while action:
        if action == "talk":
            points.append(3)
            total_points = sum(points)
            print_pause("He opens his jaws and...")
            print_pause("Gives you his treasure!")
            print_pause("You are rich now!")
            print_pause(f"You have --> {total_points} points")
            print_pause(" ")
            random_tool()
            print_pause(" ")
            back = input("Leave the cave (y/n): ")
            while back:
                if back == "y":
                    print_pause(" ")
                    print_pause("You leave the cave and return to the land.")
                    print_pause("To fight super dragon must have 10 points")
                    go()
                    break
                elif back == "n":
                    print_pause(" ")
                    print_pause("You find there's nothing else to do.")
                    print_pause("You run back to the land.")
                    land()
                    break
                else:
                    print_pause("Please choose a valid option (y/n).")
                    back = input("Leave the cave (y/n): ")
            break
        elif action == "run":
            print_pause("You run back to the land.")
            land()
            break
        else:
            print_pause("Please choose a valid option (run/talk).")
            action = input("Run or talk? (run/talk): ")


"------------------------- Go(options) ---------------------------"


def go():
    """Choose (go to bridge or fight the super dragon)."""
    go_action = input("Go to bridge or fight the SUPER dragon. (g or f): ")
    while go_action:
        if go_action == "g":
            print_pause("Going to the bridge...")
            bridge()
            break
        elif go_action == "f":
            if sum(points) >= 10:
                print_pause("You fight the super dragon!")
                print_pause("After a huge fight, you win!")
                end_game()
                break
            else:
                print_pause("You decide to fight the SUPER dragon...")
                print_pause("You fail..!")
                print_pause(f"because you have {sum(points)} points.")
                print_pause("The SUPER dragon kills you.")
                print_pause("Game over")
                points.clear()
                points.append(0)
                print_pause("You lose your points.")
                print_pause(F"You have `{sum(points)}` points")
                play_again()
                break
        else:
            print_pause("Please choose a valid option (g/f).")
            go_action = input("Please use (g `go` or f `fight`): ")


"------------------------- Return_to_cave ---------------------------"


def return_to_cave():
    """Show message if player has points when returning to cave."""
    if sum(points) == 0:
        return
    print_pause("The dragon gives you his treasure")
    print_pause(f"You have:{sum(points)} points")
    print_pause("You find there's nothing else to do.")
    go()


"------------------------- Bridge ---------------------------"


def bridge():
    """Handle the bridge encounter with the dragon."""
    print_pause(" ")
    print_pause("### The Bridge ###")
    print_pause("You approach the bridge...")
    print_pause("Unfortunately..!")
    print_pause("A large dragon jumps out in front of you!")
    print_pause(f"But you have {sum(points)} points.")
    action = input(f"Run or fight?(Must have at least 5 points): ")
    while action:
        if action == "fight":
            if sum(points) >= 5:
                print_pause("You fight the dragon on the bridge!")
                print_pause("After a huge fight, you win!")
                end_game()
                break
            else:
                print_pause("He opens his jaws and...")
                print_pause("Gobbles you down in one bite!")
                print_pause("You are dead!")
                print_pause("Game over!")
                points.clear()
                points.append(0)
                print_pause("You lose all your points.")
                print_pause(f"You have `{sum(points)}` points")
                play_again()
                break
        elif action == "run":
            print_pause("You run back to the land.")
            land()
            break
        else:
            print_pause("Please choose a valid option (run/fight).")
            action = input("Run or fight? (run/fight): ")


"------------------------- End_game ---------------------------"


def end_game():
    """Conclude the game with a victory message."""
    points.append(5)
    total_points = sum(points)
    print_pause("You kill the dragon and...")
    print_pause("You see a light and run towards it.")
    print_pause("When you catch this light.")
    print_pause("you find a sea and a small boat to escape from this land.") 
    print_pause("You end the game successfully.")
    print_pause(f"You have {total_points} points.")
    print_pause("Thanks for playing.")
    play_again()


"------------------------- Play_again ---------------------------"


def play_again():
    """Ask the player if they want to start a new game."""
    play_again = input("Do you want to play again? (yes or no): ")
    while play_again:
        if play_again == "yes":
            print_pause("Thanks for playing!")
            print_pause("Starting a new game...")
            reset_points()
            land()
            break
        elif play_again == "no":
            print_pause("Thanks for playing!")
            exit()
        else:
            print_pause("Please choose a valid option.")
            play_again = input("Do you want to play again? (yes or no): ")


"------------------------- Reset_points ---------------------------"


def reset_points():
    """Reset player's points to 0."""
    points.clear()
    points.append(0)


"------------------------- Main ---------------------------"
if __name__ == "__main__":
    land()
