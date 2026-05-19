import heapq

#Maze dimension
ROWS, COLS = 15, 15

# 15x15 maze
maze = [
    "S..#...........",
    ".#.#.#####.###.",
    ".#...#...#.....",
    ".###.#.#.#####.",
    ".....#.#.....#.",
    "#####.#.###.#..",
    "....#...#...#..",
    ".##.#####.###..",
    ".#......#......",
    ".######.#.#####",
    "........#.....#",
    ".###########..#",
    "..............#",
    ".############.#",
    "..............G"]

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_position():
    start = None
    goal = None

    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'G':
                goal = (r, c)
    return start, goal

def reconstruct_path(came_from, current):
    path = []

    while current in came_from:
        path.append(current)
        current = came_from[current]

    path.append(current)
    path.reverse()

    return path

def greedy_bfs():
    start, goal = find_position()
    #Priority queue based ONLY on heuristic
    frontier = []
    #heuristic (value, node)
    heapq.heappush(frontier, (heuristic(start, goal), start))

    came_from = {}
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)
        #Goal reached.
        if current == goal:
            return reconstruct_path(came_from, goal)

        if current in visited:
            continue

        visited.add(current)

        for dr, dc in DIRECTIONS:
            nr = current[0] + dr
            nc = current[1] + dc

            #Boundary check
            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue

            #Wall check
            if maze[nr][nc] == '#':
                continue

            neighbor = (nr, nc)
            if neighbor not in visited:
                came_from[neighbor] = current

                priority = heuristic(neighbor, goal)

                heapq.heappush(frontier, (priority, neighbor))

    return None

def print_maze_with_path(path):
    maze_copy = [list(row) for row in maze]

    for r, c in path:
        if maze_copy[r][c] not in ('S', 'G'):
            maze_copy[r][c] = '*'

    print("\nSolved Maze\n")

    for row in maze_copy:
        print(" ".join(row))


def greedy_bfs_run():
    path = greedy_bfs()
    if path:
        print('Path is found')
        print('Steps:', len(path) - 1)
        print("Path: ", path)

        print_maze_with_path(path)
    else:
        print('No Path')