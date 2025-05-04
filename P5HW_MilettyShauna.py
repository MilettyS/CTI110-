#Shauna Miletty
#05/02/2025
#P5HW



def create_character():
    #Creating a new character""
    name = input("Enter cat's name; ")
    health = int(input(f"Enter{name}'s health: "))
    strength = int(input(f"Enter{name}'s strength: "))
    character = {'name': name, "health": health, 'strength': strength}
    print(f"{name} has been created: ")
    return character

def display_character(character):
    print("Character Information:")
    print(f"Name: {character['name']}")
    print(f"Health: {character['health']}")
    print(f"Strength: {character['strength']}")

print("--------------------------Rules------------------------------------------")
print("Your are the Letter P and you need to exit this maze\U0001F914\nType left, right, up, or down\nYou need get to the Letter E in 9 turns in order to win the game. ")
print("-------------------------------------------------------------------------")


import sys

# Constants
MAZE_SIZE = 5
MAX_TURNS = 9
EXIT_POSITION = (4, 3)
START_POSITION = (0, 0)

maze = [
    ['S', '.', 'M', '.', 'M'],
    ['.', 'M', '.', 'M', '.'],
    ['M', '.', '.', '.', '.'],
    ['.', 'M', 'M', '.', 'M'],
    ['M', '.', 'M', 'E', '.']
]

monsters = {
    (0, 2): {'health': 10, 'strength': 3},
    (1, 1): {'health': 8, 'strength': 2},
    (1, 3): {'health': 12, 'strength': 4},
    (3, 0): {'health': 9, 'strength': 3},
    (3, 2): {'health': 11, 'strength': 2},
    (3, 4): {'health': 14, 'strength': 5}
}

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def create_character():
    name = input("Enter your character's name: ")
    while True:
        try:
            health = int(input("Enter your character's starting health (e.g., 20): "))
            strength = int(input("Enter your character's strength (e.g., 5): "))
            break
        except ValueError:
            print("Please enter valid integers for health and strength.")
    return {'name': name, 'health': health, 'strength': strength, 'position': START_POSITION}

def display_maze(player_pos):
    for i in range(MAZE_SIZE):
        row = []
        for j in range(MAZE_SIZE):
            if (i, j) == player_pos:
                row.append('P')
            else:
                row.append(maze[i][j])
        print(" ".join(row))
    print()

def is_valid_position(x, y):
    return 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE

def combat(player, monster):
    print("A wild monster appears!")
    while player['health'] > 0 and monster['health'] > 0:
        monster['health'] -= player['strength']
        print(f"{player['name']} hits the monster for {player['strength']} damage.")
        if monster['health'] <= 0:
            print("Monster defeated!\n")
            break
        player['health'] -= monster['strength']
        print(f"Monster hits {player['name']} for {monster['strength']} damage.")
        print(f"{player['name']}'s health: {player['health']}\n")
    return player['health'] > 0

def main():
    player = create_character()
    turn = 0

    while turn < MAX_TURNS:
        print(f"\nTurn {turn + 1} of {MAX_TURNS}")
        display_maze(player['position'])
        print(f"Health: {player['health']}, Strength: {player['strength']}")
        move = input("Move (up/down/left/right): ").strip().lower()
        if move not in directions:
            print("Invalid direction. Try again.")
            continue

        dx, dy = directions[move]
        new_x = player['position'][0] + dx
        new_y = player['position'][1] + dy

        if not is_valid_position(new_x, new_y):
            print("Can't move there, out of bounds!")
            continue

        player['position'] = (new_x, new_y)

        if player['position'] in monsters:
            monster = monsters[player['position']]
            if not combat(player, monster):
                print("You died. Game over.\U0001F915")
                return
            del monsters[player['position']]

        if player['position'] == EXIT_POSITION:
            print("You reached the exit! You win!\U0001F607")
            return

        turn += 1

    print("Out of turns. You failed to escape the maze.\U0001F915")

if __name__ == "__main__":
    main()


    
