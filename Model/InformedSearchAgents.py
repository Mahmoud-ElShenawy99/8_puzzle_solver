import math
import threading
import time
from PyQt5.QtCore import pyqtSignal, QObject
from Model.DataStructures import HashSet
from Model.DataStructures import HashMap
import heapq


class node:
    def __init__(self, nodee, h, g):
        self.h = h
        self.g = g
        self.f = self.h + self.g
        self.nodee = nodee

    def __lt__(self, nxt):
        return self.f < nxt.f


class informedSearch(QObject):
    state_signal = pyqtSignal(int)

    def __init__(self):
        super(informedSearch, self).__init__()
        self._frontier = []  # list
        self._explored_set = HashSet()
        self._parent_map = HashMap()
        self._frontier_map = dict()
        self.path = []

    def _check_solvable(self, state):
        state = str(state)
        arr = []
        for x in state:
            arr.append(x)
        inv_count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] > arr[j] and arr[i] != '0' and arr[j] != '0'):
                    inv_count += 1
        return True if inv_count % 2 == 1 else False

    # 361 012
    # 475 345
    # 208 678

    # 1+3+1+1+1+0+4+3+0

    def get_2D_index(self, n, key):
        converted_n = str(n)
        my_list = []
        for x in converted_n:
            my_list.append(x)
        if len(my_list) < 9:
            my_list.insert(0, '0')
        for e, i in zip(my_list, range(0, 9, 1)):

            if int(e) == key:
                x = i // 3
                y = i % 3
                return x, y

    def get_manhattan_heuristic(self, inital_state, goal_state):  # 3120456789
        converted_i = str(inital_state)
        heu = 0
        my_list = []
        for x in converted_i:
            my_list.append(x)
        if len(my_list) < 9:
            # print("in")
            my_list.insert(0, '0')
        for e, i in zip(my_list, range(0, 9, 1)):
            if str(e) == str(0):
                continue
            x, y = self.get_2D_index(goal_state, int(e))
            l = i // 3
            m = i % 3

            heu += abs(x - l) + abs(y - m)
        return heu

    def get_euclidean_heuristic(self, inital_state, goal_state):  # 3120456789
        converted_i = str(inital_state)
        heu = 0
        my_list = []
        for x in converted_i:
            my_list.append(x)
        if len(my_list) < 9:
            my_list.insert(0, '0')
        for e, i in zip(my_list, range(0, 9, 1)):
            if str(e) == str(0):
                continue
            x, y = self.get_2D_index(goal_state, int(e))
            l = i // 3
            m = i % 3

            heu += math.sqrt(pow(x - l, 2) + pow(y - m, 2))

        return heu

    def get_missplaced_heuristic(self,inital_state, goal_state):
        if inital_state == goal_state:
            return 0
        converted_i = str(inital_state)
        converted_g = str(goal_state)
        temp = 0
        my_list = []
        for x in converted_g:
            my_list.append(x)
        my_list.insert(0, '0')
        for i in range(0, len(converted_i)):
            if converted_i[i] != my_list[i] and converted_i[i] != "0":
                temp += 1
        return temp

    def A_star(self,Heu_algorithm, inital_state, goal_state):
        if self._check_solvable(inital_state):
            print("Unsolvable")
            return False, [], -1, [], 0
        begin = time.time()
        self._frontier.clear()
        self._explored_set.clear()
        self._parent_map.clear()
        self._frontier_map.clear()
        h = self.get_manhattan_heuristic(inital_state, goal_state)
            # if Heu_algorithm =="Man" else self.get_euclidean_heuristic(inital_state, goal_state)
        inital_node = node(inital_state, h, 0)
        self._frontier.append(inital_node)
        self._frontier_map[inital_state] = h
        self._parent_map.set_val(inital_node.nodee, inital_node.nodee)
        while (len(self._frontier) != 0):
            # heapq.heapify(self._frontier)
            s = heapq.heappop(self._frontier)
            if s in self._frontier_map:
                self._frontier_map.pop(s)
            self._explored_set.add(s.nodee)
            if s.nodee == goal_state:
                break
            neighbors = self._get_neighbors(s.nodee)
            for neighbor in neighbors:
                # if Heu_algorithm == "Man":
                neighbor_node = node(neighbor, self.get_manhattan_heuristic(neighbor, goal_state), s.g + 1)
                # else:
                #     neighbor_node = node(neighbor, self.get_euclidean_heuristic(neighbor, goal_state), s.g)

                if neighbor_node not in self._frontier_map and not self._explored_set.contains(neighbor_node.nodee):
                    self._frontier.append(neighbor_node)
                    self._frontier_map[neighbor] = neighbor_node.f
                    self._parent_map.set_val(neighbor_node.nodee, s.nodee)
                elif neighbor_node in self._frontier_map:
                    if neighbor_node.f < self._frontier_map[neighbor]:
                        heapq.heappush(self._frontier, neighbor)
                        self._frontier_map[neighbor] = neighbor_node.f
                        self._parent_map.set_val(neighbor, s.nodee)
        end = time.time()
        path_to_goal, cost_to_path = self.get_path(inital_state, goal_state)
        return True, path_to_goal, cost_to_path, self._explored_set.get_values(), (end - begin)

    def get_path(self, initial_state, goal_state):
        path_to_goal = []
        x = goal_state
        path_to_goal.append(goal_state)
        while self._parent_map.get_val(x) != initial_state:
            x = self._parent_map.get_val(x)
            path_to_goal.append(x)
        path_to_goal.append(initial_state)
        return path_to_goal, len(path_to_goal) - 1

    def _get_neighbors(self, s):
        converted_s = str(s)
        index = converted_s.find("0")  # [0 1 3 4 5 6 7 2 8]
        my_list = []
        for x in converted_s:
            my_list.append(x)
        neighbors = []

        if index == -1:
            my_list.insert(0, '0')
            neighbors.append(int("".join(self._swap(my_list.copy(), 0, 1))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 0, 3))))

        elif index == 1:
            neighbors.append(int("".join(self._swap(my_list.copy(), 1, 0))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 1, 2))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 1, 4))))

        elif index == 2:
            neighbors.append(int("".join(self._swap(my_list.copy(), 2, 1))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 2, 5))))

        elif index == 3:
            neighbors.append(int("".join(self._swap(my_list.copy(), 3, 0))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 3, 4))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 3, 6))))

        elif index == 4:
            neighbors.append(int("".join(self._swap(my_list.copy(), 4, 1))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 4, 3))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 4, 5))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 4, 7))))

        elif index == 5:
            neighbors.append(int("".join(self._swap(my_list.copy(), 5, 2))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 5, 4))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 5, 8))))

        elif index == 6:
            neighbors.append(int("".join(self._swap(my_list.copy(), 6, 3))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 6, 7))))

        elif index == 7:
            neighbors.append(int("".join(self._swap(my_list.copy(), 7, 4))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 7, 6))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 7, 8))))

        else:
            neighbors.append(int("".join(self._swap(my_list.copy(), 8, 5))))
            neighbors.append(int("".join(self._swap(my_list.copy(), 8, 7))))

        return neighbors

    def _swap(self, my_list, position1, position2):
        my_list[position1], my_list[position2] = my_list[position2], my_list[position1]
        return my_list


if __name__ == "__main__":
    initial = 12345678
    goal = 12345678
    obj = informedSearch()
    print(obj.get_2D_index(45632178, 2))
    # 150682734
    # solved, path_to_goal, cost, explored, time =obj.A_star(initial,goal)
    # print("Time= " + str(time))
    # print("Path= " + str(path_to_goal))
    # print("Cost= " + str(cost))
    # print("Explored= " + str(explored))
    # print("Explored Number= " + str(len(explored)))
    # print("Depth= " + str(cost))
