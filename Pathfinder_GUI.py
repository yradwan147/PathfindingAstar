import math
import pygame
import collections

grid = []
for i in range(15):
    grid.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
MAX = 15
OPEN = []
CLOSED = []
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
LIME = (50,205,50)
BLUE = (0, 0, 200)
ORANGE = (255,165,0)
WINDOW_HEIGHT = 300
WINDOW_WIDTH = 300
blockSize = 20 #Set the size of the grid block

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)


def drawGrid(start_x, start_y, end_x, end_y):
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):               
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            if x == int(start_x) and y == int(start_y):
                pygame.draw.rect(SCREEN, RED, rect, 0)
            elif x == int(end_x) and y == int(end_y):
                pygame.draw.rect(SCREEN, GREEN, rect, 0)
            else:
                pygame.draw.rect(SCREEN, BLACK, rect, 1)
    for o in CLOSED:
        if collections.Counter(o) != collections.Counter([start_y, start_x]) and collections.Counter(o) != collections.Counter([end_y, end_x]):     
            rect_cl = pygame.Rect(o[0] * blockSize, o[1] * blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, ORANGE, rect_cl, 0)
            ##print("drawn")
    for i in OPEN:
        if collections.Counter(i) != collections.Counter([start_y, start_x]) and collections.Counter(i) != collections.Counter([end_y, end_x]):     
            rect_op = pygame.Rect(i[0] * blockSize, i[1] * blockSize, blockSize, blockSize)
            pygame.draw.rect(SCREEN, LIME, rect_op, 0)
            ##print("drawn1")
    
def print_grid():
    for x in range(0, len(grid)):
        print(grid[x])

def find_element(element):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == element:
                position = [y, x]
                return position

def distance(x1 , y1):
    ##print(x1,y1)
    return math.sqrt((abs(x1[0] - y1[0]))^2 + abs((x1[1] - y1[0]))^2)

def f_cost(point):
    return distance(point, find_element(1)) + distance(point, find_element(2))

def neighbor_list(i):
    neighbors = [[i[0] - 1, i[1] - 1], [i[0] - 1, i[1]], [i[0] - 1, i[1] + 1],
                 [i[0], i[1] - 1], [i[0], i[1] + 1],
                 [i[0] + 1, i[1] - 1], [i[0] + 1, i[1]], [i[0] + 1, i[1] + 1]]
    invalid = []
    for i in neighbors:
        for j in range(2):
            if i[j] < 0 or i[j] > MAX:
                invalid.append(i)
    for k in invalid:
        if k in neighbors:
            neighbors.remove(k)
    ##print(neighbors)
    return neighbors

start_x = input("Please input start point x position: ")
start_y = input("Please input start point y position: ")
grid[int(start_y) - 1][int(start_x) - 1] = 1
end_x = input("Please input end point x position: ")
end_y = input("Please input end point y position: ")
grid[int(end_y) - 1][int(end_x) - 1] = 2
OPEN.append([int(start_y), int(start_x)])
print(OPEN)

while True:
    main()
    drawGrid(start_x, start_y, end_x, end_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    f_values = []
    print(OPEN)
    for i in OPEN:
        f_values.append(f_cost(i))
        if f_cost(i) == min(f_values):
            current = i
    OPEN.remove(current)
    CLOSED.append(current)

    if current == [int(end_y), int(end_x)]:
        print("\n" + str(CLOSED))
        for i in CLOSED:
            if i == find_element(1) or i == find_element(2):
                continue
            grid[i[0]][i[1]] = 5
        print_grid()
        break

    for l in neighbor_list(current):
        ##print(l)
        if grid[l[0]][l[1]] == 3 or l in CLOSED:
            continue
        elif l not in OPEN:
            OPEN.append(l)