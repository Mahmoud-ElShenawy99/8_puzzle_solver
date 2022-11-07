import threading
import time
import timeit
from PyQt5.QtCore import pyqtSignal, QObject

from Model.DataStructures import HashSet
from Model.DataStructures import HashMap








class UninformedSearch(QObject):
    state_signal = pyqtSignal(int)
    def __init__(self):
        super(UninformedSearch, self).__init__()
        self._frontier = []  # stack
        self._explored_set = HashSet()
        self._parent_map = HashMap()
        self._frontier_map = HashMap()
        # self.thread = threading.Thread(target=self.DFS,args=(arg1,arg2))
        # self.thread.start()
        self.path=[]



    def DFS(self,initial_state, goal_state):
        if self._check_solvable(initial_state):
            print("Unsolvable")
            return False,[],-1,[],0
        begin = time.time()
        self._frontier_map.clear()
        self._frontier.clear()
        self._explored_set.clear()
        self._parent_map.clear()
        self.state_signal.emit(initial_state)
        self._frontier.append(initial_state) # insert s' into frontier
        self._frontier_map.set_val(initial_state,None)
        self._parent_map.set_val(initial_state, initial_state)  # insert <s',s'> into parent map
        while len(self._frontier) != 0:  # while (frontier not empty)
            s = self._frontier.pop()
            self._frontier_map.delete_val(s)
            self.state_signal.emit(s)
            self._explored_set.add(s)
            if s == goal_state:
                break
            neighbors = self._get_neighbors(s, "DFS")
            for neighbor in neighbors:
                if not (self._frontier_map.get_val(neighbor)) and not self._explored_set.contains(neighbor):
                    self._frontier.append(neighbor)
                    self._frontier_map.set_val(neighbor, None)
                    self._parent_map.set_val(neighbor, s)

        path_to_goal,cost_to_path=self.get_path(initial_state,goal_state)
        end = time.time()
        return True,path_to_goal,cost_to_path,self._explored_set.get_values(),(end - begin)

    def _check_solvable(self,state):
        state = str(state)
        arr=[]
        for x in state:
            arr.append(x)
        inv_count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] > arr[j] and arr[i] != '0' and arr[j] != '0'):
                    inv_count += 1
        # print(inv_count)
        return True if inv_count %2 == 1 else False

    def BFS(self, initial_state, goal_state):
        if self._check_solvable(initial_state):
            print("Unsolvable")
            return False, [], -1, [], 0
        begin = time.time()
        self._frontier_map.clear()
        self._frontier.clear()
        self._explored_set.clear()
        self._parent_map.clear()
        self.state_signal.emit(initial_state)
        self._frontier.append(initial_state)  # insert s' into frontier
        self._frontier_map.set_val(initial_state, None)
        self._parent_map.set_val(initial_state, initial_state)  # insert <s',s'> into parent map
        while len(self._frontier) != 0:  # while (frontier not empty)
            s = self._frontier.pop(0)
            self._frontier_map.delete_val(s)
            self.state_signal.emit(s)
            self._explored_set.add(s)
            if s == goal_state:
                break
            neighbors = self._get_neighbors(s, "DFS")
            for neighbor in neighbors:
                if not(self._frontier_map.get_val(neighbor)) and not self._explored_set.contains(neighbor):
                    self._frontier.append(neighbor)
                    self._frontier_map.set_val(neighbor, None)
                    self._parent_map.set_val(neighbor, s)

        path_to_goal, cost_to_path = self.get_path(initial_state, goal_state)
        end = time.time()
        return True, path_to_goal, cost_to_path, self._explored_set.get_values(), (end - begin)

    def get_path(self,initial_state,goal_state):
        path_to_goal=[]
        x=goal_state
        path_to_goal.append(goal_state)
        while self._parent_map.get_val(x) != initial_state:
            x=self._parent_map.get_val(x)
            path_to_goal.append(x)
        path_to_goal.append(initial_state)
        return path_to_goal,len(path_to_goal)-1

    def _get_neighbors(self,s, type):
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

        neighbors.sort(reverse=True) if type == "DFS" else neighbors.sort()
        return neighbors

    def _swap(self,my_list, position1, position2):
        my_list[position1], my_list[position2] = my_list[position2], my_list[position1]
        return my_list
