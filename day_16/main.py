# Get vertex list (coordinates). A vertex is a point surrounded by 3 or 4 point in the cardinal directions.
# Start and End points are also vertex.
# Get vertex connections and cost
from collections import defaultdict

from utils import Point, Maze

def main():
    with open("input_data") as f:
        raw_map  =  f.read()
    maze = Maze(raw_map, 'east')
    maze.get_connections()

if __name__ == "__main__":
    main()









