from xml.dom.minicompat import NodeList
import numpy as np
from project5map import is_obstacle
import random
import matplotlib.pyplot as plt
from math import sqrt, pow, atan2, sin, cos

plt.xlim(0, 10)
plt.ylim(0, 10)

def get_random_point():
    x = round(10*(random.random()), 1)
    y = round(10*(random.random()), 1)
    return x, y

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def get_nearest_node(random_point):
    nearest_node = start_node
    min_distance = distance(start_node[0], random_point)
    for node in node_list:
        if distance(node[0], random_point) < min_distance:
            min_distance = distance(node[0], random_point)
            nearest_node = node
    return nearest_node

def is_obstructed(random_point, nearest_node):
    x1, y1 = nearest_node[0]
    x2, y2 = random_point
    x_int_pts = np.linspace(x1, x2, num=100).round(decimals=1)
    y_int_pts = np.linspace(y1, y2, num=100).round(decimals=1)
    for x, y in list(zip(x_int_pts, y_int_pts)):
        if is_obstacle(x, y):
            return True
    return False


def step(random_point, nearest_node):
    # get dy, dx between points for atan2
    dx = random_point[0] - nearest_node[0][0]
    dy = random_point[1] - nearest_node[0][1]
    # get angle of line between points and x axis
    theta = atan2(dy,dx)
    # get x coord of step length with this angle
    sx = nearest_node[0][0] + step_size * cos(theta)
    # get y coord
    sy = nearest_node[0][1] + step_size * sin(theta)
    return (round(sx, 2), round(sy, 2))

def add_node(new_node_position, nearest_node, node_count):
    pos = new_node_position[0], new_node_position[1]
    node_count += 1
    node_list.append((pos, node_count, nearest_node[1]))
    return node_count

def draw_edge(node1, node2):
    x1, y1 = node1[0]
    x2, y2 = node2[0]
    plt.plot([x1, x2], [y1, y2])

def is_goal(position):
    if distance(position, goal_node[0]) < threshold:
        return True
    return False


def get_path():
    solution_path = [node_list[-1]]
    while solution_path[-1][2] != "root":
        for node in node_list:
            if node[1] == solution_path[-1][2]:
                solution_path.append(node)
    return solution_path
    

def draw_path(path):
    for node in path:
        x, y = node[0]
        plt.plot([x], [y], "go")  



        
def save_path(revpath):
    file = open("output.txt", "w+")
    path = []
    for node in revpath:
        x, y = node[0]
        path.append(node[0])
    path = path[::-1]
   
    for x, y in path:
        file.write(str(round(x,2)) + ' ' + str(round(y,2)))
        file.write('\n')
    file.close()

# __/\\\\____________/\\\\_____/\\\\\\\\\_____/\\\\\\\\\\\__/\\\\\_____/\\\_        
#  _\/\\\\\\________/\\\\\\___/\\\\\\\\\\\\\__\/////\\\///__\/\\\\\\___\/\\\_       
#   _\/\\\//\\\____/\\\//\\\__/\\\/////////\\\_____\/\\\_____\/\\\/\\\__\/\\\_      
#    _\/\\\\///\\\/\\\/_\/\\\_\/\\\_______\/\\\_____\/\\\_____\/\\\//\\\_\/\\\_     
#     _\/\\\__\///\\\/___\/\\\_\/\\\\\\\\\\\\\\\_____\/\\\_____\/\\\\//\\\\/\\\_    
#      _\/\\\____\///_____\/\\\_\/\\\/////////\\\_____\/\\\_____\/\\\_\//\\\/\\\_   
#       _\/\\\_____________\/\\\_\/\\\_______\/\\\_____\/\\\_____\/\\\__\//\\\\\\_  
#        _\/\\\_____________\/\\\_\/\\\_______\/\\\__/\\\\\\\\\\\_\/\\\___\//\\\\\_ 
#         _\///______________\///__\///________\///__\///////////__\///_____\/////__

# node: ((x, y), node_index, parent_node_index)
start_node = ((1, 1), 0, "root")
goal_node = ((9, 9), "goal", "goal")
# node_list = [start_node, goal_node]
node_list = [start_node]
node_count = 0

# tuning parameters
node_limit = 1000
step_size = 0.5
threshold = step_size * 1.1

# draw start, goal and goal area
plt.scatter([start_node[0][0]], [start_node[0][0]])
# plt.scatter([goal_node[0][0]], [goal_node[0][0]])
goal_circle = plt.Circle((goal_node[0]), threshold, ec="red", fc='None')
plt.gca().add_patch(goal_circle)

# draw obstacles
for i in range(0, 100):
    for j in range(0, 100):
        x,y = i/10, j/10
        # if circle1(x,y) or circle2(x,y) or rectangle1(x,y) or rectangle2(x,y) or rectangle3(x,y):
        if is_obstacle(x,y):
            plt.plot(x, y, "b.")


# search for goal, grow tree
goal_found = False
for i in range(node_limit):
    randompoint = get_random_point()
    nearestnode = get_nearest_node(randompoint)
    newnodeposition = step(randompoint, nearestnode)
    # check for obstruction
    if is_obstructed(newnodeposition, nearestnode):
       continue 
    plt.scatter([newnodeposition[0]], [newnodeposition[1]], marker=".")
    node_count = add_node(newnodeposition, nearestnode, node_count)
    draw_edge(nearestnode, node_list[-1])
    if is_goal(newnodeposition):
        print("goal reached")
        goal_found = True
        break
    # plt.pause(0.05)



if goal_found:
    # do...
    path_to_goal = get_path()
    draw_path(path_to_goal)
    save_path(path_to_goal)
else:
    print("goal not found, increase node limit")




    



plt.show()

