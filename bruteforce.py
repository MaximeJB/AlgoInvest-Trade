import time
import tracemalloc

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
    
def Algo_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite +1)] for x in range(len(elements)+1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite +1):
            if elements[i-1][1] <= w:
                matrice[i][w] = max(elements[i-1][2]+ matrice [i-1][w-elements[i-1][1]], matrice[i-1][w])

            else : 
                matrice[i][w] = matrice[i-1][w]
    
    w = capacite
    n = len(elements)
    elements_selection  = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice [n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w-= e[1]
        n -= 1
    poids_total  = sum(e[1] for e in elements_selection)
    return matrice[-1][-1], elements_selection, poids_total




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

def generer_rapport(capacite, elements):
    report = []
    report.append("# Rapport d'exploitation\n")
    report.append(f"- Capacité du sac : {capacite}\n")

    # Force brute
    tracemalloc.start()
    t0 = time.perf_counter()
    bf_val, bf_sel = algo_Force_Brute(capacite, elements)
    dt_bf = time.perf_counter() - t0
    mem_bf, peak_bf = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    report.append("## 1. Force brute")
    report.append(f"- Temps d'exécution : {dt_bf:.4f} s")
    report.append(f"- Pic mémoire       : {peak_bf/1024:.1f} KiB")
    report.append(f"- Valeur optimale   : {bf_val}")
    report.append(f"- Poids total       : {sum(e[1] for e in bf_sel)}")
    report.append(f"### Objets sélectionnés {bf_sel})

    # Dynamique
    tracemalloc.start()
    t0 = time.perf_counter()
    dyn_val, dyn_sel, dyn_pds = Algo_dynamique(capacite, elements)
    dt_dyn = time.perf_counter() - t0
    mem_dyn, peak_dyn = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    report.append("## 2. Programmation dynamique")
    report.append(f"- Temps d'exécution : {dt_dyn:.4f} s")
    report.append(f"- Pic mémoire       : {peak_dyn/1024:.1f} KiB")
    report.append(f"- Valeur optimale   : {dyn_val}")
    report.append(f"- Poids total       : {dyn_pds}")
    report.append("### Objets sélectionnés")
    for nom, p, v in dyn_sel:
        report.append(f"- {nom} (poids={p}, valeur={v})")
    report.append("")

    # Complexité
    report.append("## 3. Complexité")
    report.append("- Force brute : \(O(2^n)\)")
    report.append("- Dynamique : \(O(n\times W)\)") 

    # Écriture du rapport
    with open("rapport_exploitation.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print("➡️ Rapport généré : rapport_exploitation.md")

# Exécution du wrapper
generer_rapport(500, ele)