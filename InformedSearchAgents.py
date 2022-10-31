from DataStructures import HashSet
from DataStructures import HashMap

def swap(my_list,position1,position2):
    my_list[position1], my_list[position2] = my_list[position2], my_list[position1]
    return my_list

def get_neighbors(s,type):
    converted_s= str(s)
    index = converted_s.find("0")
    my_list = []
    for x in converted_s:
        my_list.append(x)
    neighbors=[]

    if index == -1:
        my_list.insert(0,'0')
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




def DFS (initial_state,goal_state):
    frontier=[] # stack
    explored_set= HashSet()
    parent_map=HashMap()
    frontier.append(initial_state) #insert s' into frontier
    parent_map.set_val(initial_state,initial_state) #insert <s',s'> into parent map
    while len(frontier) != 0 : #while (frontier not empty)
        s=frontier.pop(0)
        print(s)
        explored_set.add(s)
        if s == goal_state:
            break
        neighbors = get_neighbors(s,"DFS")
        for neighbor in neighbors:
            print(neighbor)
            if neighbor not in frontier and not explored_set.contains(neighbor):
                frontier.append(neighbor)
                parent_map.set_val(neighbor,s)



