# Datei: faerbung.py
# Author: Micky & Erik
# Version: 1.3


import time

start_time = time.time()

colors = ["red", "blue", "green", "yellow"]
all_list = []
colors_list = [("A", 1)]
g = {"A": ["B", "E", "F"],
     "B": ["A", "C", "D", "E", "G"],
     "C": ["B", "D", "F"],
     "D": ["C", "B", "G"],
     "E": ["A", "B", "G", "H"],
     "F": ["C", "A", "H"],
     "G": ["B", "D", "E", "H"],
     "H": ["G", "E", "F"]
     }


def intersect(node, graph_list, clist):
    if not clist:
        return 0

    for i in clist:
        if node[0] == i[0]:
            return 1

    for n in graph_list[node[0]]:
        for element in clist:
            if element[0] == n:
                if node[1] == element[1]:
                    return 1
    return 0


def replace_colors(c_list, colors):
    l = []
    for i in c_list:
        k = i[1]
        k = colors[k-1]
        l.append(((i[0]), k))
    return l


forward = True


def faerben(graph_list, clist, all_list, one_time=False):
    global forward
    if len(clist) == len(graph_list):
        all_list.append(replace_colors(clist, colors))
        if one_time:
            forward = False
        print(replace_colors(clist, colors))
    else:
        for e in graph_list.keys()[1:]:
            for i in range(1, 5):
                if not intersect((str(e), i), graph_list, clist) and not len(clist) == len(graph_list) and forward:
                    faerben(graph_list, clist + [(str(e), i)], all_list)


faerben(g, colors_list, all_list, one_time=False)
print("Amount found: ", len(all_list))
print("Execution time: " + str(abs(start_time - time.time())) + " seconds")
