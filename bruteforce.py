def algo_Force_Brute(capacite, actions, elements_selection = []):
    if actions: 
        val1, listVal1 = algo_Force_Brute(capacite, actions[1:], elements_selection)
        objet = actions[0]     
        if objet[1] <= capacite:
            val2, listVal2 = algo_Force_Brute(capacite - objet[1], actions[1:], elements_selection + [objet])
            if val1 < val2:
                return val2, listVal2
        return val1, listVal1
    else: 
        return sum([i[2] for i in elements_selection]), elements_selection

actions = [
    ("Action-1", 20, 5),
    ("Action-2", 30, 10),
    ("Action-3", 50, 15),
    ("Action-4", 70, 20),
    ("Action-5", 60, 17),
    ("Action-6", 80, 25),
    ("Action-7", 22, 7),
    ("Action-8", 26, 11),
    ("Action-9", 48, 13),
    ("Action-10", 34, 27),
    ("Action-11", 42, 17),
    ("Action-12", 110, 9),
    ("Action-13", 38, 23),
    ("Action-14", 14, 1),
    ("Action-15", 18, 3),
    ("Action-16", 8, 8),
    ("Action-17", 4, 12),
    ("Action-18", 10, 14),
    ("Action-19", 24, 21),
    ("Action-20", 114, 18)]

print(f'Algorithme', algo_Force_Brute(500, actions))

