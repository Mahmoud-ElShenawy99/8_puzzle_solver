import threading
import time

from PyQt5.QtCore import pyqtSignal, QObject

from Model.DataStructures import HashSet
from Model.DataStructures import HashMap


def swap(my_list, position1, position2):
    my_list[position1], my_list[position2] = my_list[position2], my_list[position1]
    return my_list





class UninformedSearch(QObject):
    state_signal = pyqtSignal(int)
    def __init__(self):
        super(UninformedSearch, self).__init__()
        print("UninformedSearch")
        self._frontier = []  # stack
        print("UninforrfsdmedSearch")
        self._explored_set = HashSet()
        self._parent_map = HashMap()
        print("UninformedSearch")
        self.thread = threading.Thread(target=self.DFS,args=(arg1,arg2))
        self.thread.start()



    def DFS(self,initial_state, goal_state):
        # self._frontier.clear()
        # self._explored_set.clear()
        # self._parent_map.clear()
        print(initial_state)
        self.state_signal.emit(initial_state)
        time.sleep(1)
        self._frontier.append(initial_state)  # insert s' into frontier
        self._parent_map.set_val(initial_state, initial_state)  # insert <s',s'> into parent map
        while len(self._frontier) != 0:  # while (frontier not empty)
            s = self._frontier.pop()
            self.state_signal.emit(s)
            time.sleep(1)
            self._explored_set.add(s)
            if s == goal_state:
                break
            neighbors = self._get_neighbors(s, "DFS")
            for neighbor in neighbors:
                if neighbor not in self._frontier and not self._explored_set.contains(neighbor):
                    self._frontier.append(neighbor)
                    self._parent_map.set_val(neighbor, s)


    def BFS(self,initial_state, goal_state):
        # self._frontier.clear()
        # self._explored_set.clear()
        # self._parent_map.clear()
        self._frontier.append(initial_state)  # insert s' into frontier
        self._parent_map.set_val(initial_state, initial_state)  # insert <s',s'> into parent map
        while len(self._frontier) != 0:  # while (frontier not empty)
            s = self._frontier.pop(0)
            self.state_signal.emit(s)
            self._explored_set.add(s)
            if s == goal_state:
                break
            neighbors = self._get_neighbors(s, "BFS")
            for neighbor in neighbors:
                print(neighbor)
                if neighbor not in self._frontier and not self._explored_set.contains(neighbor):
                    self._frontier.append(neighbor)
                    self._parent_map.set_val(neighbor, s)

    def _get_neighbors(self,s, type):
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

        neighbors.sort(reverse=True) if type == "DFS" else neighbors.sort()
        return neighbors

    def _swap(self,my_list, position1, position2):
        my_list[position1], my_list[position2] = my_list[position2], my_list[position1]
        return my_list
