from Controller.MainWindowController import MainWindowController
from PyQt5 import QtWidgets

from Model.UninformedSearchAgents import UninformedSearch
if __name__ == "__main__":
    # 4 3 1
    # 7 8 2
    # 0 6 5


    initial = 12345867
    goal = 12345678
    search=UninformedSearch()

    solved,path_to_goal,cost,explored,time=search.BFS(initial, goal)
    print("Time= "+str(time))
    print("Path= "+str(path_to_goal))
    print("Cost= "+str(cost))
    print("Explored= "+ str(explored))
    print("Explored Number= "+str(len(explored)))
    print("Depth= "+str(cost))
    print("{BFS} finished")
    solved,path_to_goal,cost,explored,time=search.DFS(initial, goal)
    print("Time= "+str(time))
    print("Path= "+str(path_to_goal))
    print("Cost= "+str(cost))
    print("Explored= "+ str(explored))
    print("Explored Number= "+str(len(explored)))
    print("Depth= "+str(cost))
    print("{DFS} finished")

