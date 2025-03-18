#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TCSS 435 A Fall
# Zachary Anderson
#
#
#
# Assigment 2 Minimax and Alpha-Beta Pruning

import pymaze as maze
import random, sys, GameSearch
from GameSearch import MM, AB, visited_nodes

# Global variables
update_visited_nodes = visited_nodes
current_player = None
max_move = None
min_move = None
player_two = True
min_path = []

text = open("Readme.txt", "a")

# # Arguments passed for creating maze size and what algorithm to be ran
print("Name of Python script:", sys.argv[0])
print("AI is player 1 or player 2:", int(sys.argv[1]))
print("search method:", sys.argv[2])
print("size of maze 10 or 20:", int(sys.argv[3]))

player = int(sys.argv[1])
algorithm = sys.argv[2]
maze_size = int(sys.argv[3])

text.write(str(player) + " " + algorithm + " " + str(maze_size) + ": " + "\n")
text.close()

if maze_size == 10:
    m = maze.maze(10, 10)
    # All (x,y) cooridinates for Agents and maze goal
    max_x = random.randint(1,10)
    max_y = random.randint(1,10)
    min_x = random.randint(1,10)
    min_y = random.randint(1,10)
    goal_x = random.randint(1,10)
    goal_y = random.randint(1,10)
    max_start = max_x, max_y
    min_start = min_x, min_y
    goal = goal_x, goal_y

    print("MAX start: ", max_start)
    print("MIN start: ", min_start)
    print("Goal: ", goal)

    # Makes sure agent MAX doesnt have same spawn point as Goal
    while max_x == goal_x and max_y == goal_y:
        print("Agent MAX has the same spot as Goal")
        max_x = random.randint(1,10)
        max_y = random.randint(1,10)
        max_start = max_x, max_y
        print ("MAX new start: ", max_start)

    # Makes sure agent MIN doesnt have same spawn point as MAX and Goal
    while min_x == max_x and min_y == max_y or min_x == goal_x and min_y == goal_y:
        print("Agent MIN has the same spot as Goal or agent MAX")
        min_x = random.randint(1,10)
        min_y = random.randint(1,10)
        min_start = min_x, min_y
        print ("MIN new start: ", min_start)
    print("-----------------------------------------------------------------------------------------------------------------")
elif maze_size == 20:
    m = maze.maze(20, 30)
    # All (x,y) cooridinates for Agents and maze goal
    max_x = random.randint(1,20)
    max_y = random.randint(1,30)
    min_x = random.randint(1,20)
    min_y = random.randint(1,30)
    goal_x = random.randint(1,20)
    goal_y = random.randint(1,30)
    max_start = max_x, max_y
    min_start = min_x, min_y
    goal = goal_x, goal_y

    print("MAX start: ", max_start)
    print("MIN start: ", min_start)
    print("Goal: ", goal)

    # Makes sure agent MAX doesnt have same spawn point as Goal
    while max_x == goal_x and max_y == goal_y:
        print("Agent MAX has the same spot as Goal")
        max_x = random.randint(1,20)
        max_y = random.randint(1,30)
        max_start = max_x, max_y
        print ("MAX new start: ", max_start)

    # Makes sure agent MIN doesnt have same spawn point as MAX and Goal
    while min_x == max_x and min_y == max_y or min_x == goal_x and min_y == goal_y:
        print("Agent MIN has the same spot as Goal or agent MAX")
        min_x = random.randint(1,20)
        min_y = random.randint(1,30)
        min_start = min_x, min_y
        print ("MIN new start: ", min_start)
    print("-----------------------------------------------------------------------------------------------------------------")
elif maze_size == 5:
    m = maze.maze(5,5)
    # All (x,y) cooridinates for Agents and maze goal
    max_x = random.randint(1,5)
    max_y = random.randint(1,5)
    min_x = random.randint(1,5)
    min_y = random.randint(1,5)
    goal_x = random.randint(1,5)
    goal_y = random.randint(1,5)
    max_start = max_x, max_y
    min_start = min_x, min_y
    goal = goal_x, goal_y

    print("MAX start: ", max_start)
    print("MIN start: ", min_start)
    print("Goal: ", goal)

    # Makes sure agent MAX doesnt have same spawn point as Goal
    while max_x == goal_x and max_y == goal_y:
        print("Agent MAX has the same spot as Goal")
        max_x = random.randint(1,5)
        max_y = random.randint(1,5)
        max_start = max_x, max_y
        print ("MAX new start: ", max_start)

    # Makes sure agent MIN doesnt have same spawn point as MAX and Goal
    while min_x == max_x and min_y == max_y or min_x == goal_x and min_y == goal_y:
        print("Agent MIN has the same spot as Goal or agent MAX")
        min_x = random.randint(1,5)
        min_y = random.randint(1,5)
        min_start = min_x, min_y
        print ("MIN new start: ", min_start)
    print("-----------------------------------------------------------------------------------------------------------------")
else:
    raise Exception("Invalid input! Choose 10 or 20 only.")

# Creates maze and maze goal
m.CreateMaze(goal_x,goal_y, loopPercent=100, theme = maze.COLOR.dark)

# Creates a Agent
max = maze.agent(m,max_x,max_y, shape = 'arrow', footprints = True)
min = maze.agent(m,min_x,min_y, footprints = True, color = maze.COLOR.red)

# Based off input algorith, said algorithm will run and solution path is received for agent
if algorithm == "MM":
    max_path = MM(m, max_start, min_start, goal, update_visited_nodes)
    print("MM ran")
elif algorithm == "AB":
    max_path = AB(m, max_start, min_start, goal, update_visited_nodes)
    print("AB ran")
else:
    raise Exception("Invalid input! Choose MM or AB only.")

# Based on input from user, this decides whether the AI agent goes first or the Human agent goes first
if player == 1:
    current_player = 1
elif player == 2:
    current_player = 2
else:
    raise Exception("Invalid input! Choose 1 or 2 only.")

# https://www.google.com/search?q=taking+turns+code+for+game+in+python&oq=taking&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgwIARBFGDkYsQMYgAQyCggCEC4YsQMYgAQyCggDEC4YsQMYgAQyCggEEAAYsQMYgAQyDQgFEAAYsQMYgAQYigUyDQgGEC4YrwEYxwEYgAQyBwgHEAAYgAQyBwgIEC4YgAQyBwgJEAAYjwLSAQkzNTQwajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8
# AI response on goolge for resource, and alternated to make work with my existing code
# Allows for AI agent and Human agent to take turns in game
while True:
    if max_move == goal or min_move == goal:
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Game Over")
        print("depth: ", GameSearch.depth)
        print("nodes_expanded: ", GameSearch.nodes_expanded)
        text = open("Readme.txt", "a")
        text.write("Evaluation Function: Manhattan distance of AI agents possible moves to goal - Manhattan distance of Human agents position to goal " + "\n"
                    + "Depth: " + str(GameSearch.depth) + "\n"
                    + "Nodes expanded: " + str(GameSearch.nodes_expanded) + "\n"
                    + "\n")
        text.close()
        break

    # Game logic for the current player
    if current_player == 1:

        # Player 1's turn
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Player 1's turn")
        if len(max_path) == 0:
            if algorithm == "MM":
                max_path = MM(m, max_start, min_start, goal, update_visited_nodes)
                
            elif algorithm == "AB":
                max_path = AB(m, max_start, min_start, goal, update_visited_nodes)

        max_move = max_path.pop(0)
        max_start = max_move
        print("max move: ", max_move)
        max.position = max_move
    else:
        # Player 2's turn
        print("-----------------------------------------------------------------------------------------------------------------")
        print("Player 2's turn")

        visited = min_start
        min_possible_moves = []

        # Navigates the maze map dictionary of dictionaries and adds possible moves from expanded node
        for move in m.maze_map[visited]:
            if move == 'E' and m.maze_map[visited]['E'] == 1:
                x, y = visited
                east = x + 0, y + 1
                min_possible_moves.append(east)

            if move == 'W' and m.maze_map[visited]['W'] == 1:
                x, y = visited
                west = x + 0, y - 1
                min_possible_moves.append(west)

            if move == 'N' and m.maze_map[visited]['N'] == 1:
                x, y = visited
                north = x - 1, y + 0
                min_possible_moves.append(north)

            if move == 'S' and m.maze_map[visited]['S'] == 1:
                x, y = visited
                south = x + 1, y + 0
                min_possible_moves.append(south)

        # Gets Human agent move from user
        while True:
            print("Enter coordinate of possible moves displayed: ", min_possible_moves)
            x = int(input("Enter the row: "))
            y = int(input("Enter the column: "))
            user_input = x, y
            min_path.append(user_input)
            min_move = min_path.pop(0)

            # Checks if the input from the user is a possible move, if not re-enter coordinates
            if min_move not in min_possible_moves:
                print("-----------------------------------------------------------------------------------------------------------------")
                print("Invalid input: Choose from list of possible moves.")
                continue

            min_start = min_move
            print("min move: ", min_move)
            min.position = min_move

            # Checks if the input from the user is a possible move, if correct break the loop
            if min_move in min_possible_moves:
                break

            min_possible_moves.clear()

    # Switch to the next player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

m.run()