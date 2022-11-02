import threading
import time
from PyQt5.QtCore import pyqtSignal, QObject
from Model.DataStructures import HashSet
from Model.DataStructures import HashMap
import heapq

def swap(my_list, position1, position2):
    my_list[position1], my_list[position2] = my_list[position2], my_list[position1]
    return my_list





class UninformedSearch(QObject):
    state_signal = pyqtSignal(int)
    def __init__(self):
        super(UninformedSearch, self).__init__()
        self._frontier = []  # stack
        self._explored_set = HashSet()
        self._parent_map = HashMap()
        # self.thread = threading.Thread(target=self.DFS,args=(arg1,arg2))
        # self.thread.start()
        self.path=[]

    def A_star(self,inital_state,goal_state):
        self._frontier.clear()
        self._explored_set.clear()
        self._parent_map.clear()
        self._frontier.append(inital_state)
        self._parent_map.set_val(inital_state,inital_state)
        while(len(self._frontier) != 0):
            s=heapq.heappop(self._frontier)
            self._explored_set.add(s)
            if s==goal_state:
                break
            neighbors=self._get_neighbors(s)
            for neighbor in neighbors:
                if neighbor not in self._frontier and not self._explored_set.contains(neighbor):
                    self._frontier.append(neighbor)
                    self._parent_map.set_val(neighbor, s)
                if neighbor is in self._frontier:
                    self.

    def get_path(self,initial_state,goal_state):
        path_to_goal=[]
        x=goal_state
        path_to_goal.append(goal_state)
        while self._parent_map.get_val(x) != initial_state:
            x=self._parent_map.get_val(x)
            path_to_goal.append(x)
        path_to_goal.append(initial_state)
        return path_to_goal,len(path_to_goal)-1

    def _get_neighbors(self,s):
        converted_s = str(s)
        index = converted_s.find("0")  # [0 1 3 4 5 6 7 2 8]
        my_list = []
        for x in converted_s:
            my_list.append(x)
        neighbors = []

        if index == -1:
            my_list.insert(0, '0')
            neighbors.append(int("".join(swap(my_list.copy(), 0, 1))))
            neighbors.append(int("".join(swap(my_list.copy(), 0, 3))))

        elif index == 1:
            neighbors.append(int("".join(swap(my_list.copy(), 1, 0))))
            neighbors.append(int("".join(swap(my_list.copy(), 1, 2))))
            neighbors.append(int("".join(swap(my_list.copy(), 1, 4))))

        elif index == 2:
            neighbors.append(int("".join(swap(my_list.copy(), 2, 1))))
            neighbors.append(int("".join(swap(my_list.copy(), 2, 5))))

        elif index == 3:
            neighbors.append(int("".join(swap(my_list.copy(), 3, 0))))
            neighbors.append(int("".join(swap(my_list.copy(), 3, 4))))
            neighbors.append(int("".join(swap(my_list.copy(), 3, 6))))

        elif index == 4:
            neighbors.append(int("".join(swap(my_list.copy(), 4, 1))))
            neighbors.append(int("".join(swap(my_list.copy(), 4, 3))))
            neighbors.append(int("".join(swap(my_list.copy(), 4, 5))))
            neighbors.append(int("".join(swap(my_list.copy(), 4, 7))))

        elif index == 5:
            neighbors.append(int("".join(swap(my_list.copy(), 5, 2))))
            neighbors.append(int("".join(swap(my_list.copy(), 5, 4))))
            neighbors.append(int("".join(swap(my_list.copy(), 5, 8))))

        elif index == 6:
            neighbors.append(int("".join(swap(my_list.copy(), 6, 3))))
            neighbors.append(int("".join(swap(my_list.copy(), 6, 7))))

        elif index == 7:
            neighbors.append(int("".join(swap(my_list.copy(), 7, 4))))
            neighbors.append(int("".join(swap(my_list.copy(), 7, 6))))
            neighbors.append(int("".join(swap(my_list.copy(), 7, 8))))

        else:
            neighbors.append(int("".join(swap(my_list.copy(), 8, 5))))
            neighbors.append(int("".join(swap(my_list.copy(), 8, 7))))

        neighbors.sort()
        return neighbors

    def _swap(self,my_list, position1, position2):
        my_list[position1], my_list[position2] = my_list[position2], my_list[position1]
        return my_list
