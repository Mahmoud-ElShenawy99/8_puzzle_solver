from Controller.MainWindowController import MainWindowController
from PyQt5 import QtWidgets

from Model.UninformedSearchAgents import UninformedSearch
from Model.InformedSearchAgents import informedSearch

if __name__ == "__main__":

    initial = 312450678
    goal = 12345678
    search=UninformedSearch()
    isearch=informedSearch()
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
    solved, path_to_goal, cost, explored, time = isearch.A_star(initial, goal)
    print("Time= " + str(time))
    print("Path= " + str(path_to_goal))
    print("Cost= " + str(cost))
    print("Explored= " + str(explored))
    print("Explored Number= " + str(len(explored)))
    print("Depth= " + str(cost))
    print("{A*} finished")

