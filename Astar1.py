import heapq
from pydoc import visiblename

#Maze size.
ROWS, COLS = 15, 15

# 15x15 maze
# S = Start
# G = Goal
# . = Free path
# # = Wall

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
    "..............G"
]

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#Manhattan distance
def heuristic(a, b):
    return(abs(a[0] - b[0])) + abs(a[1] - b[1])

def find_positions():
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

def a_start():
    start, goal = find_positions()
    #priority queues
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    #Cost from start to node.
    g_score = {start: 0}
    #estimated total cost
    f_score = {start: heuristic(start, goal)}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)

        visited.add(current)

        for dr, dc in DIRECTIONS:
            nr, nc = current[0] + dr, current[1] + dc
            #Check boundaries
            if not (0 <= nr < ROWS and 0 <= nc < COLS): continue

            #Check walls
            if maze[nr][nc] == '#':
                continue
            neighbor = (nr, nc)

            tentative_g = g_score[current] + 1
            if neighbor in visited and tentative_g >= g_score.get(neighbor, float('inf')):
                continue
            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None


def print_maze_with_path(path):
    maze_copy = [list(row) for row in maze]

    for r, c in path:
        if maze_copy[r][c] not in ('S', 'G'):
            maze_copy[r][c] = '*'

        print("\nSolve Maze\n")

        for row in maze_copy:
            print("".join(row))
# Run A star search
