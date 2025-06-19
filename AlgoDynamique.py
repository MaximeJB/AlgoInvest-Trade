import pandas as pd
import csv

def Algo_dynamique(capacite, elements):
    matrice = [[0 for _ in range(capacite +1)] for _ in range(len(elements)+1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite +1):
            if elements[i-1][1] <= w:
                    element_int = int(elements[i-1][1])
                    second_value = matrice[i-1][w-element_int]
                    first_value = elements[i-1][2] + second_value
                    matrice[i][w] = max(first_value, matrice[i-1][w])
            else : 
                    matrice[i][w] = matrice[i-1][w]
    
    w = capacite
    n = len(elements)
    elements_selection  = []

    while n >= 0:
        print(f" === n={n}, w={w}, matrice[n][w]={matrice[n][w]} ===")
        objet = elements[n-1]
        poids = int(objet[1])
        if matrice[n][w] == matrice[n-1][w - poids] + objet[2]:

            #Print pour voir l'objet sélectionné et le poids restant. 
            print(f"  -> On sélectionne {objet[0]} (poids={poids}, bénéfice={objet[2]})") 

            elements_selection.append(objet)
            w -= poids
        n -= 1
        print(n) #Ici print pour voir la matrice descendre
    return matrice[-1][-1], elements_selection

FACTEUR = 100
def read_dataset(path_file, facteur = FACTEUR):
    df = pd.read_csv(path_file, sep=None, engine='python')
    
    df.columns = ['Action', 'Cout', 'Benefice']

    df['Benefice'] = df['Cout'] * df['Benefice'] / FACTEUR
    df['Cout'] = (df['Cout'] * facteur).round().astype(int)
    df['Benefice'] = (df['Benefice'] * facteur).round().astype(int)

    df = df[df['Cout'] >= 0]
    df = df.drop(df[df['Action'] == 'Share-JNGS'].index)
    df = df[df["Cout"] != 0]
    
    return df

file_name = r"C:\Users\maxym\Documents\GitHub\Algo\dataset2_Python+P7.csv"
data_ready = read_dataset(file_name, FACTEUR)
elements = data_ready[['Action', 'Cout', 'Benefice']].values.tolist()
capacite = int(500 * FACTEUR)


resultat_int, selection_int = Algo_dynamique(capacite, elements)

benefice_optimal = resultat_int / FACTEUR
poids_selection = sum(obj[1] for obj in selection_int) / FACTEUR
selection = [(obj[0], obj[1]/FACTEUR, obj[2]/FACTEUR) for obj in selection_int]

print(f"coût total : {poids_selection}")
print(f"profit : {benefice_optimal}")
print("Actions choisies :", selection)

# print("Valeur max :", resultat)
# print("bénéfice recompté : ", sum(e[2] for e in selection))
# print("Actions choisies :", sum(objet[1] for objet in selection))

