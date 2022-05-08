import matplotlib.pyplot as plt

r = 0.1
c = 0.05
t = r + c

# rectangle1 definition
# point is inside if:
def rectangle1(x, y):
    if x >= 0.25 - t and \
       x <= 1.75 + t and \
       y >= 4.25 - t and \
       y <= 5.75 + t:
        return True
    return False
# rectangle2 definition
# point is inside if:
def rectangle2(x, y):
    if x >= 3.75 - t and \
       x <= 6.25 + t and \
       y >= 4.25 - t and \
       y <= 5.75 + t:
        return True
    return False
# rectangle3 definition
# point is inside if:
def rectangle3(x, y):
    if x >= 7.25 - t and \
       x <= 8.75 + t and \
       y >= 2 - t and \
       y <= 4 + t:
        return True
    return False
# circle1 definition
# point is inside if:
def circle1(x, y):
    if (pow(x-2,2)+pow(y-2,2)) <= (1 + t) ** 2:
        return True
    return False
# circle2 definition
# point is inside if:
def circle2(x, y):
    if (pow(x-2,2)+pow(y-8,2)) <= (1 + t) ** 2:
        return True
    return False

# combined obstacle
def is_obstacle(x, y):
    if x >= 0.25 - t and \
       x <= 1.75 + t and \
       y >= 4.25 - t and \
       y <= 5.75 + t:
        return True
    if x >= 3.75 - t and \
       x <= 6.25 + t and \
       y >= 4.25 - t and \
       y <= 5.75 + t:
        return True
    if x >= 7.25 - t and \
       x <= 8.75 + t and \
       y >= 2 - t and \
       y <= 4 + t:
        return True
    if (pow(x-2,2)+pow(y-2,2)) <= (1 + t) ** 2:
        return True
    if (pow(x-2,2)+pow(y-8,2)) <= (1 + t) ** 2:
        return True
    if x <= t and \
       x >= 10 - t and \
       y <= t and \
       y >= 10 - t:
        return True   
            
    return False

if __name__ == "__main__":
    plt.figure(figsize=(5, 5))
    axes = plt.axes()
    # x axis
    axes.set_xlim(0, 10)
    # axes.set_xticks([])
    # y axis
    axes.set_ylim(0, 10)
    # axes.set_yticks([])

    # rectangle1 = plt.Rectangle((0.25, 4.25), 1.5, 1.5, fc="blue", ec="red")
    # rectangle2 = plt.Rectangle((3.75, 4.25), 2.5, 1.5, fc="blue", ec="red")
    # rectangle3 = plt.Rectangle((7.25,2), 1.5, 2, fc="blue", ec="red")
    # circle1 = plt.Circle((2, 2),1, fc='blue',ec="red")
    # circle2 = plt.Circle((2,8),1, fc='blue',ec="red")
    # plt.gca().add_patch(rectangle1)
    # plt.gca().add_patch(rectangle2)
    # plt.gca().add_patch(rectangle3)
    # plt.gca().add_patch(circle1)
    # plt.gca().add_patch(circle2)

    for i in range(0, 100):
        for j in range(0, 100):
            x,y = i/10, j/10
            # if circle1(x,y) or circle2(x,y) or rectangle1(x,y) or rectangle2(x,y) or rectangle3(x,y):
            if is_obstacle(x,y):
                plt.plot(i/10, j/10, "bo")

    plt.show()