# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Astar1 import *




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = a_start()

    if path:
        print("Path found")
        print("Steps:", len(path) - 1)
        print("Path:", path)

        print_maze_with_path(path)
    else:
        print("No path found")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

