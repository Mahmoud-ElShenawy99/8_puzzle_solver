import threading
import time
from PyQt5.QtCore import pyqtSignal, QObject
from Model.DataStructures import HashSet
from Model.DataStructures import HashMap
import heapq


class node:
    def __init__(self,nodee,h):
        self.h=h
        self.nodee=nodee

    def __lt__(self, nxt):
        return self.h < nxt.h

class informedSearch(QObject):
    state_signal = pyqtSignal(int)
    def __init__(self):
        super(informedSearch, self).__init__()
        self._frontier = [] #list
        self._explored_set = HashSet()
        self._parent_map = HashMap()
        self.path=[]
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
        return True if inv_count %2 == 1 else False

    def find_heuristic(self,inital_state,goal_state):
        if inital_state==goal_state:
            return 0
        converted_i = str(inital_state)
        converted_g = str(goal_state)
        temp = 0
        my_list = []
        for x in converted_g:
            my_list.append(x)
        my_list.insert(0, '0')
        for i in range(0, len(converted_i)):
             if converted_i[i] != my_list[i] and converted_i[i] != "0" :
                temp += 1
        return temp

    def A_star(self,inital_state,goal_state):
        if self._check_solvable(inital_state):
            print("Unsolvable")
            return False,[],-1,[],0
        begin = time.time()
        self._frontier.clear()
        self._explored_set.clear()
        self._parent_map.clear()
        h=self.find_heuristic(inital_state,goal_state)
        inital_node=node(inital_state,h)
        self._frontier.append(inital_node)
        self._parent_map.set_val(inital_node.nodee,inital_node.nodee)
        while(len(self._frontier) != 0):
            # print("frontier:",self._frontier[0].nodee)
            heapq.heapify(self._frontier)
            # print("frontier after:", self._frontier[0].nodee)
            s=heapq.heappop(self._frontier)

            self._explored_set.add(s.nodee)
            # print(s.nodee,s.h)
            if s.nodee==goal_state:
                break
            neighbors=self._get_neighbors(s.nodee)
            for neighbor in neighbors:
                # print(neighbor)
                neighbor_node=node(neighbor,self.find_heuristic(neighbor,goal_state))
                if neighbor_node not in self._frontier and not self._explored_set.contains(neighbor_node.nodee):
                    self._frontier.append(neighbor_node)
                    self._parent_map.set_val(neighbor_node.nodee, s.nodee)
        end = time.time()
        path_to_goal, cost_to_path = self.get_path(inital_state, goal_state)
        return True, path_to_goal, cost_to_path, self._explored_set.get_values(), (end - begin)
# 3 1 2
# 0 4 5
# 6 7 8

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

    def _swap(self,my_list, position1, position2):
        my_list[position1], my_list[position2] = my_list[position2], my_list[position1]
        return my_list
if __name__ == "__main__":
    initial = 312045678   #3 1 2  0 1 2
                          #4 7 5  3 4 5
                          #0 6 8  6 7 8
    goal = 12345678
    obj=informedSearch()


    # print(obj.find_heuristic(initial,goal))
    # obj.A_star(initial,goal)
    # d=1
    # f=2
    # g=3
    # a=node("1",7)
    # b=node("2",8)
    # c=node("3",4)
    # z = node("4", 9)
    # x = node("5", 10)
    # list=[]
    # list.append(b)
    # list.append(c)
    # list.append(a)
    # list.append(z)
    # list.append(x)
    # print("before",list[0].nodee)
    # heapq.heapify(list)
    # print("after",list[0].nodee)
    # s=heapq.heappop(list)
    #
    # print(s.nodee)
    # for i in range(0, len(list)):
    #     print(list[i].h)
    #     print(list[i].nodee)