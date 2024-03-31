from rich import print
from rich.console import Console

# Initialize Rich Console 
console = Console()

# Print a decorative ASCII art
print('''[yellow]
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
[/yellow]''')

# Print introductory messages
print("[cyan][+} Welcome to Treasure Island.[/cyan]")
print("[cyan][+] Your mission is to find the treasure.[/cyan]") 

# Get user's choice for the first decision
choice1 = console.input('[bold blue]You\'re at a cross road. Where do you want to go? Type "left" or "right" \n[/bold blue]').lower()

if choice1 == "left":
    # If user chose to go left
    choice2 = console.input('[bold blue]You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n[/bold blue]').lower()

    if choice2 == "wait":
        # If user chose to wait for the boat
        choice3 = console.input("[bold blue]You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose? \n[/bold blue]").lower()
        
        if choice3 == "red":
            # If user chose the red door
            print("[bold red][+] It's a room full of fire. Game Over.[/bold red]")
        elif choice3 == "yellow":
            # If user chose the yellow door
            print("[green][+] You found the treasure! You Win![/green]")
        elif choice3 == "blue":
            # If user chose the blue door
            print("[bold red][+] You enter a room of beasts. Game Over.[/bold red]")
        else:
            # If user entered an invalid choice
            print("[green][+] You chose a door that doesn't exist. Game Over.[/green]")
    else:
        # If user chose to swim across the lake
        print("[bold red][+] You get attacked by an angry trout. Game Over.[/bold red]")
else:
    # If user chose to go right
    print("[bold red][+] You fell into a hole. Game Over.[/bold red]")