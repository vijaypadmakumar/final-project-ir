import numpy as np


class AStar:

    def __init__(self, initial_pair, goal_pair):
        self.grid_dict = self.readgrid()
        self.initial_pair = initial_pair
        self.goal_pair = goal_pair

    def readgrid(self):
        """
        Gets occupancy grid from grid.txt
        """

        grid_dict = {}
        filereader = open("grid.txt", "r")
        grids = filereader.read().split("\n")
        filereader.close()

        for grid in grids:
            if grid != "":
                string = grid.split(" ")
                grid_dict.update(
                    {(int(string[0]), int(string[1])): int(string[2])})

        grid_array = []

        for key, value in grid_dict.items():
            grid_array.append(value)

        data = np.array(grid_array)

        reshape_data = np.reshape(data, (602, 602))

        trans_data = np.transpose(reshape_data)

        rot_data = np.rot90(trans_data)

        counti = 0
        countj = 0

        dict_data = {}

        for i in range(602*602):

            dict_data.update({(counti, countj): rot_data[counti][countj]})
            countj = countj + 1

            if countj == 602:
                countj = 0
                counti = counti + 1

        return dict_data

    def shift_to_origin(self, pair):

        X = 300 - pair[1]*20
        Y = pair[0]*20 + 300

        Pair = (X, Y)

        return Pair

    def shift_from_origin(self, pair):

        X = -(300 - pair[1])/20
        Y = -(pair[0] - 300)/20

        Pair = (X, Y)

        return Pair

    def find_direction(self, node):

        xDiff = node[0][0] - node[1][0]
        yDiff = node[0][1] - node[1][1]

        direction = ""

        if yDiff > 0:
            direction = "t"
        elif xDiff > 0:
            direction = "r"
        elif yDiff < 0:
            direction = "b"
        elif xDiff < 0:
            direction = "l"
        else:
            direction = "N"

        return direction

    def find_neighbours(self, current_pair, count, prev):

        possiblePoints = []

        current_pair = self.shift_to_origin(current_pair)
        prev_pair = self.shift_to_origin(prev)

        xDiff = current_pair[0] - prev_pair[0]
        yDiff = current_pair[1] - prev_pair[1]

        direction = ""

        if yDiff > 0:
            direction = "t"
        elif xDiff > 0:
            direction = "r"
        elif yDiff < 0:
            direction = "b"
        elif xDiff < 0:
            direction = "l"
        else:
            direction = "N"

        for key, value in self.grid_dict.items():

            if current_pair[0] == key[0] and (current_pair[1] + 1) == key[1] and direction != "b":

                if value == 0:

                    # print("FREE -", self.shift_from_origin(key), "-", key)

                    top_neighbour = (current_pair[0], current_pair[1] + 1)

                    xDistance = self.shift_to_origin(self.goal_pair)[
                        0] - top_neighbour[0]
                    yDistance = self.shift_to_origin(self.goal_pair)[
                        1] - top_neighbour[1]
                    if xDistance < 0:
                        xDistance = xDistance*(-1)
                    if yDistance < 0:
                        yDistance = yDistance*(-1)

                    heuristics = xDistance + yDistance

                    point = [self.shift_from_origin(top_neighbour), self.shift_from_origin(
                        current_pair), count + 1, heuristics]
                    possiblePoints.append(point)

                # elif value == 1:
                #     print("BLOCK -", self.shift_from_origin(key), "-", key)
                # elif value == 2:
                #     print("UNKNOWN -", self.shift_from_origin(key), "-", key)

            elif (current_pair[0] + 1) == key[0] and current_pair[1] == key[1] and direction != "l":

                if value == 0:

                    # print("FREE -", self.shift_from_origin(key), "-", key)

                    right_neighbour = (current_pair[0] + 1, current_pair[1])

                    xDistance = self.shift_to_origin(self.goal_pair)[
                        0] - right_neighbour[0]
                    yDistance = self.shift_to_origin(self.goal_pair)[
                        1] - right_neighbour[1]

                    if xDistance < 0:
                        xDistance = xDistance*(-1)
                    if yDistance < 0:
                        yDistance = yDistance*(-1)

                    heuristics = xDistance + yDistance

                    point = [self.shift_from_origin(right_neighbour), self.shift_from_origin(
                        current_pair), count + 1, heuristics]
                    possiblePoints.append(point)

                # elif value == 1:
                #     print("BLOCK -", self.shift_from_origin(key), "-", key)
                # elif value == 2:
                #     print("UNKNOWN -", self.shift_from_origin(key), "-", key)

            elif current_pair[0] == key[0] and (current_pair[1] - 1) == key[1] and direction != "t":

                if value == 0:

                    # print("FREE -", self.shift_from_origin(key), "-", key)

                    bottom_neighbour = (current_pair[0], current_pair[1] - 1)

                    xDistance = self.shift_to_origin(self.goal_pair)[
                        0] - bottom_neighbour[0]
                    yDistance = self.shift_to_origin(self.goal_pair)[
                        1] - bottom_neighbour[1]

                    if xDistance < 0:
                        xDistance = xDistance*(-1)
                    if yDistance < 0:
                        yDistance = yDistance*(-1)

                    heuristics = xDistance + yDistance

                    point = [self.shift_from_origin(bottom_neighbour), self.shift_from_origin(
                        current_pair), count + 1, heuristics]
                    possiblePoints.append(point)

                # elif value == 1:
                #     print("BLOCK -", self.shift_from_origin(key), "-", key)
                # elif value == 2:
                #     print("UNKNOWN -", self.shift_from_origin(key), "-", key)

            elif (current_pair[0] - 1) == key[0] and current_pair[1] == key[1] and direction != "r":

                if value == 0:

                    # print("FREE -", self.shift_from_origin(key), "-", key)

                    left_neighbour = (current_pair[0] - 1, current_pair[1])

                    xDistance = self.shift_to_origin(self.goal_pair)[
                        0] - left_neighbour[0]
                    yDistance = self.shift_to_origin(self.goal_pair)[
                        1] - left_neighbour[1]

                    if xDistance < 0:
                        xDistance = xDistance*(-1)
                    if yDistance < 0:
                        yDistance = yDistance*(-1)

                    heuristics = xDistance + yDistance

                    point = [self.shift_from_origin(left_neighbour), self.shift_from_origin(
                        current_pair), count + 1, heuristics]
                    possiblePoints.append(point)

                # elif value == 1:
                #     print("BLOCK -", self.shift_from_origin(key), "-", key)
                # elif value == 2:
                #     print("UNKNOWN -", self.shift_from_origin(key), "-", key)

        return possiblePoints

    def goal_reached(self, open_nodes):

        for node in open_nodes:

            if node[0] == self.goal_pair:

                print("GOAL STATE REACHED")

                return True

        return False

    def checkClosedNode(self, lowest_node, closed_nodes):

        for node in closed_nodes:

            if node[0] == lowest_node[0] and node[1] == lowest_node[1]:
                return True

        return False

    def findLowestNode(self, equal_distance_nodes, closed_nodes):

        lowest_node = []

        if len(equal_distance_nodes) > 1:

            low_heuristics = equal_distance_nodes[0][3]
            lowest_node = equal_distance_nodes[0]

            for node in equal_distance_nodes:

                if not(self.checkClosedNode(node, closed_nodes)):

                    if node[3] < low_heuristics:

                        lowest_node = node
                        low_heuristics = node[3]

                    elif node[3] == low_heuristics:

                        node_direction = self.find_direction(node)
                        lowest_node_direction = self.find_direction(
                            lowest_node)

                        if node_direction == "t":
                            lowest_node = node
                        elif lowest_node_direction == "t":
                            lowest_node = lowest_node
                        elif node_direction == "r":
                            lowest_node = node
                        elif lowest_node_direction == "r":
                            lowest_node = lowest_node
                        elif node_direction == "b":
                            lowest_node = node
                        elif lowest_node_direction == "b":
                            lowest_node = lowest_node
                        elif node_direction == "l":
                            lowest_node = node
                        else:
                            lowest_node = lowest_node

        else:

            lowest_node = equal_distance_nodes[0]

        return lowest_node

    def retrace_path(self, closed_nodes):

        path = []

        prev_node = self.goal_pair

        while prev_node != self.initial_pair:
            for node in closed_nodes:
                if node[0] == prev_node:
                    prev_node = node[1]
                    path.append(node)

        return path[::-1]

    def AStarPathPlanning(self):

        # print(self.grid_dict)

        open_nodes = self.find_neighbours(
            self.initial_pair, 0, self.initial_pair)
        # print(open_nodes)

        closed_nodes = []

        while not(self.goal_reached(open_nodes)):

            if len(open_nodes) > 1:

                lowest_node = open_nodes[0]
                lowest_distance = lowest_node[2] + lowest_node[3]

            elif len(open_nodes) == 1:

                lowest_node = open_nodes
                lowest_distance = lowest_node[2] + lowest_node[3]

            for node in open_nodes:

                if node[2] + node[3] < lowest_distance:

                    # if not(self.checkClosedNode(lowest_node, closed_nodes)):
                    lowest_distance = node[2] + node[3]
                    # lowest_node = node

                elif node[2] + node[3] == lowest_distance:

                    # if not(self.checkClosedNode(lowest_node, closed_nodes)):

                    if node[3] < lowest_node[3]:
                        lowest_distance = node[2] + node[3]
                        # lowest_node = node

            equal_distance_nodes = []

            for node in open_nodes:

                if node[2] + node[3] == lowest_distance:

                    equal_distance_nodes.append(node)

            lowest_node = self.findLowestNode(
                equal_distance_nodes, closed_nodes)

            open_nodes.remove(lowest_node)
            closed_nodes.append(lowest_node)

            direction = self.find_direction(lowest_node)

            # print(lowest_node, "", direction)

            new_nodes = self.find_neighbours(
                lowest_node[0], lowest_node[2], lowest_node[1])

            # print(len(open_nodes), len(new_nodes), len(closed_nodes))

            if len(new_nodes) != 0:

                remove_open_node = []
                remove_new_node = []

                for nodeO in open_nodes:
                    for nodeN in new_nodes:
                        if nodeN[0][0] == nodeO[0][0] and nodeN[0][1] == nodeO[0][1]:
                            if nodeO[2] + nodeO[3] >= nodeN[2] + nodeN[3]:
                                remove_open_node.append(nodeO)
                            else:
                                remove_new_node.append(nodeN)

                if len(remove_open_node) > 0:
                    for node in remove_open_node:
                        open_nodes.remove(node)

                if len(remove_new_node) > 0:
                    for node in remove_new_node:
                        new_nodes.remove(node)

                for node in new_nodes:
                    open_nodes.append(node)

        for node in open_nodes:

            if node[0] == self.goal_pair:
                closed_nodes.append(node)

        path = self.retrace_path(closed_nodes)

        return path


# def readgrid():

#     grid_dict = {}
#     filereader = open("grid.txt", "r")
#     grids = filereader.read().split("\n")
#     filereader.close()

#     for grid in grids:
#         if grid != "":
#             string = grid.split(" ")
#             grid_dict.update({(int(string[0]), int(string[1])) : int(string[2])})


#     # print(grid_dict[(480, 220)])
#     # print(grid_dict[(120, 220)])
#     # print(grid_dict[(120, 380)])
#     # print(grid_dict[(480, 380)])

#     # print(grid_dict[(380, 120)])
#     # print(grid_dict[(220, 120)])
#     # print(grid_dict[(220, 480)])
#     # print(grid_dict[(380, 480)])

#     # print("\n")

#     grid_array = []

#     for key, value in grid_dict.items():
#         grid_array.append(value)

#     data = np.array(grid_array)

#     reshape_data = np.reshape(data, (602, 602))

#     trans_data = np.transpose(reshape_data)

#     rot1_data = np.rot90(trans_data)

#     # rot2_data = np.rot90(rot1_data)
#     # rot3_data = np.rot90(rot2_data)


#     # filewriter = open("grid_map.txt", "a")

#     # i = 0
#     # j = 0
#     # index = 0

#     # while index != 602*602:

#     #     if j == 601:
#     #         filewriter.write("\n")
#     #     elif i == 300 and j == 300:
#     #         filewriter.write("x")
#     #     elif rot1_data[i][j] == 0:
#     #         filewriter.write(" ")
#     #     elif rot1_data[i][j] == 1:
#     #         filewriter.write("|")
#     #     elif rot1_data[i][j] == 2:
#     #         filewriter.write("*")

#     #     j = j + 1
#     #     index = index + 1

#     #     if j == 602:
#     #         j = 0
#     #         i = i + 1

#     # filewriter.close()

#     counti = 0
#     countj = 0

#     dict_data = {}

#     for i in range(602*602):

#         dict_data.update({(counti, countj) : rot1_data[counti][countj]})
#         # print(dict_data[(counti,countj)], counti, countj)
#         countj = countj + 1

#         if countj == 602:
#             countj = 0
#             counti = counti + 1

#     # print(dict_data)

#     return dict_data

# grid_data = readgrid()

# for key, value in grid_data.items():

#     # if key[0] == 320 and key[1] >= 300 and key[1] <= 320:
#     #     print(key, value)
#     if key[0] == 339 and key[1] == 260:
#         print(key, value)
#     elif key[0] == 340 and key[1] == 220:
#         print(key, value)
#     elif key[0] == 120 and key[1] == 380:
#         print(key, value)
#     elif key[0] == 480 and key[1] == 380:
#         print(key, value)
#     # elif key[0] == 260 and key[1] == 339:
#     #     print(key, value)

# print(grid_data[(260, 340)])
# print(grid_data[(260, 341)])
# print(grid_data[(259, 340)])
# print(grid_data[(261, 340)])
# print(grid_data[(260, 339)])

# print("\n")

# print(grid_data[(480, 220)])
# print(grid_data[(120, 220)])
# print(grid_data[(120, 380)])
# print(grid_data[(480, 380)])

# print(grid_data[(380, 120)])
# print(grid_data[(220, 120)])
# print(grid_data[(220, 480)])
# print(grid_data[(380, 480)])

# print("hello")

obj = AStar((2, 2), (7, -5))

path = obj.AStarPathPlanning()

print(path)


def convert_path(path):

    direction = []

    for node in path:

        xDiff = node[0][0] - node[1][0]
        yDiff = node[0][1] - node[1][1]

        if yDiff > 0:
            direction.append("t")
        elif xDiff > 0:
            direction.append("r")
        elif yDiff < 0:
            direction.append("b")
        elif xDiff < 0:
            direction.append("l")

    return direction


directions = convert_path(path)

filewriter = open("sector3.txt", "a")

for direction in directions:
    filewriter.write(direction + "\n")

filewriter.close()

print(directions)
