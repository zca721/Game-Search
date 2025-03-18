# TCSS 435 A Fall
# Zachary Anderson

import random

# Global Variables
visited_nodes = []
graph_tree = {}
nodes_expanded = 0
depth = 0
stuck = 0


# Builds game tree from current position one depth level at a time
def build_game_tree(maze, max_position, min_position, goal):
    # Calculates max depth level over entire game
    global depth
    depth = depth + 1
    print("depth: ", depth)

    max_parent = max_position
    min_parent = min_position
    child = get_moves(maze, max_parent, min_parent, goal)
    graph_tree.update({(max_parent, min_parent): child})

    return graph_tree

# Gets all possible moves from current position and assigns a utility value to moves
def get_moves(maze, max_position, min_position, goal):
    global stuck
    visited = max_position
    child_and_distance = {}

    # Checks for expanded nodes, and if node is not in expanded nodes, the node is added to fringe
    if visited not in visited_nodes:
        visited_nodes.append(visited)

    # Navigates the maze map dictionary of dictionaries and adds possible moves from expanded node
    for move in maze.maze_map[visited]:
        if move == 'E' and maze.maze_map[visited]['E'] == 1:
            x, y = visited
            east = x + 0, y + 1
            # Checks for expanded nodes, and if node is in expanded nodes, the node is not added to fringe
            if east not in visited_nodes:
                visited_nodes.append(east)
                max_distance = manhattan_distance(east, goal)
                min_distance = manhattan_distance(min_position, goal)
                utility_value = max_distance - min_distance
                child_and_distance.update({(east, min_position): utility_value})

        if move == 'W' and maze.maze_map[visited]['W'] == 1:
            x, y = visited
            west = x + 0, y - 1
            # Checks for expanded nodes, and if node is in expanded nodes, the node is not added to fringe
            if west not in visited_nodes:
                visited_nodes.append(west)
                max_distance = manhattan_distance(west, goal)
                min_distance = manhattan_distance(min_position, goal)
                utility_value = max_distance - min_distance
                child_and_distance.update({(west, min_position): utility_value})

        if move == 'N' and maze.maze_map[visited]['N'] == 1:
            x, y = visited
            north = x - 1, y + 0
            # Checks for expanded nodes, and if node is in expanded nodes, the node is not added to fringe
            if north not in visited_nodes:
                visited_nodes.append(north)
                max_distance = manhattan_distance(north, goal)
                min_distance = manhattan_distance(min_position, goal)
                utility_value = max_distance - min_distance
                child_and_distance.update({(north, min_position): utility_value})

        if move == 'S' and maze.maze_map[visited]['S'] == 1:
            x, y = visited
            south = x + 1, y + 0
            # Checks for expanded nodes, and if node is in expanded nodes, the node is not added to fringe
            if south not in visited_nodes:
                visited_nodes.append(south)
                max_distance = manhattan_distance(south, goal)
                min_distance = manhattan_distance(min_position, goal)
                utility_value = max_distance - min_distance
                child_and_distance.update({(south, min_position): utility_value})

    # This accounts for when the AI agent gets in a spot where all possible moves are in
    # visited nodes and can not make a move and would crash the game, now it selectes moves
    # whether move is in the visited nodes or not and now the agent can continue to move.
    if len(child_and_distance) == 0:
        stuck = 1

        # Navigates the maze map dictionary of dictionaries and adds possible moves from expanded node
        for move in maze.maze_map[visited]:
            if move == 'E' and maze.maze_map[visited]['E'] == 1:
                x, y = visited
                east = x + 0, y + 1
                max_distance = manhattan_distance(east, goal)
                min_distance = manhattan_distance(min_position, goal)
                utility_value = max_distance - min_distance
                child_and_distance.update({(east, min_position): utility_value})

            if move == 'W' and maze.maze_map[visited]['W'] == 1:
                x, y = visited
                west = x + 0, y - 1
                max_distance = manhattan_distance(west, goal)
                min_distance = manhattan_distance(min_position, goal)
                utility_value = max_distance - min_distance
                child_and_distance.update({(west, min_position): utility_value})

            if move == 'N' and maze.maze_map[visited]['N'] == 1:
                x, y = visited
                north = x - 1, y + 0
                max_distance = manhattan_distance(north, goal)
                min_distance = manhattan_distance(min_position, goal)
                utility_value = max_distance - min_distance
                child_and_distance.update({(north, min_position): utility_value})

            if move == 'S' and maze.maze_map[visited]['S'] == 1:
                x, y = visited
                south = x + 1, y + 0
                max_distance = manhattan_distance(south, goal)
                min_distance = manhattan_distance(min_position, goal)
                utility_value = max_distance - min_distance
                child_and_distance.update({(south, min_position): utility_value})

    return child_and_distance

# Calculates what is the best move for Minimax Algorithm from lowest utility value,
# the first lowest utility value is assigned as the best move, there can be mulitple
# best moves amongst the child nodes.
def MM_best_move(moves):
    distance = float('inf')
    list_move = []
    global nodes_expanded
    global stuck

    for current_positions in moves:
        value = moves.get(current_positions)
        for utility_value in value:
            lowest_value = value.get(utility_value)

            # This accounts for when the AI agent gets stuck moving back and forth in the same spot
            # it will now randomly select a move until AI agent gets unstuck moving back and forth.
            if stuck == 1:
                print("agent stuck")
                if lowest_value <= distance:
                    distance = lowest_value
                    list_move.append(utility_value[0])

                    if len(list_move) > 1:
                        # Randomly pop a value
                        random_move = random.randint(0,(len(list_move) - 1))
                        list_move.pop(random_move)

                # Calculates number of nodes expanded over entire game
                nodes_expanded = nodes_expanded + 1

            else:
                if lowest_value < distance:
                    distance = lowest_value

                    if len(list_move) > 0:
                        list_move.pop()

                    list_move.append(utility_value[0])

                # Calculates number of nodes expanded over entire game
                nodes_expanded = nodes_expanded + 1

    graph_tree.clear()

    return list_move

# Calculates what is the best move for Alpha-Beta Pruning Algorithm from lowest value,
# if next utility value is greater than current best utility value, then the rest of 
# the child nodes are pruned off.
def AB_best_move(moves):
    distance = float('inf')
    list_move = []
    global nodes_expanded

    for current_positions in moves:
        value = moves.get(current_positions)
        for utility_value in value:
            lowest_value = value.get(utility_value)

            # This accounts for when the AI agent gets stuck moving back and forth in the same spot
            # it will now randomly select a move until AI agent gets unstuck moving back and forth.
            if stuck == 1:
                print("agent stuck")
                if lowest_value <= distance:
                    distance = lowest_value
                    list_move.append(utility_value[0])

                    if len(list_move) > 1:
                        # Randomly pop a value
                        random_move = random.randint(0,(len(list_move) - 1))
                        list_move.pop(random_move)

                # Calculates number of nodes expanded over entire game
                nodes_expanded = nodes_expanded + 1

            else:
                if lowest_value > distance:
                    break
                
                if lowest_value < distance:
                    distance = lowest_value

                    if len(list_move) > 0:
                        list_move.pop()

                    list_move.append(utility_value[0])

                # Calculates number of nodes expanded over entire game
                nodes_expanded = nodes_expanded + 1

    graph_tree.clear()

    return list_move

# Used to calculate the manhattan distance for each position to goal
def manhattan_distance(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])

# Minimax algorithm using game tree
def MM(maze, maxStart, minStart, goal, update_visited_nodes):
    visited_nodes = update_visited_nodes

    moves = build_game_tree(maze, maxStart, minStart, goal)

    result = MM_best_move(moves)

    return result

# Alpha-Beta pruning algorithm using game tree
def AB(maze, maxStart, minStart, goal, update_visited_nodes):
    visited_nodes = update_visited_nodes

    moves = build_game_tree(maze, maxStart, minStart, goal)

    result = AB_best_move(moves)

    return result