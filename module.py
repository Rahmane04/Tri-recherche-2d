import random  # On importe le module random pour générer des nombres aléatoires

# ==============================================================================
# GÉNÉRATION ET AFFICHAGE
# ==============================================================================

def generer_table(nb_lignes=3, nb_colonnes=5, valeur_min=0, valeur_max=99):
    """Génère une table 2D remplie de valeurs aléatoires."""
    return [
        [random.randint(valeur_min, valeur_max) for _ in range(nb_colonnes)]
        for _ in range(nb_lignes)
    ]


def afficher_table(table, titre="Table"):
    """Affiche la table avec un format lisible."""
    print(f"\n--- {titre} ---")
    for i, ligne in enumerate(table):
        print(f"  Ligne {i} : {ligne}")
    print()


# ==============================================================================
# FONCTIONS UTILITAIRES COMMUNES AUX 5 TRIS
# ==============================================================================

def aplatir(tableau_2d):
    """
    Convertit un tableau 2D en tableau 1D.
    Ex: [[5, 3, 8], [1, 9, 2]] → [5, 3, 8, 1, 9, 2]
    """
    tableau_1d = []
    for ligne in tableau_2d:
        for element in ligne:
            tableau_1d.append(element)
    return tableau_1d


def reconstruire(tableau_1d, nb_lignes, nb_colonnes):
    """
    Reconstruit un tableau 2D à partir d'un tableau 1D trié,
    en conservant les dimensions d'origine.
    Ex: [1, 2, 3, 5, 8, 9] avec lignes=2, colonnes=3
      → [[1, 2, 3], [5, 8, 9]]
    """
    tableau_2d = []
    index = 0
    for i in range(nb_lignes):
        ligne = []
        for j in range(nb_colonnes):
            ligne.append(tableau_1d[index])
            index += 1
        tableau_2d.append(ligne)
    return tableau_2d


# ==============================================================================
# TRI PAR SÉLECTION
# ==============================================================================

def tri_selection_ligne(ligne):
    """
    PRINCIPE DU TRI PAR SÉLECTION :

    1. On parcourt la liste position par position.
    2. Pour chaque position i, on suppose que l'élément à i est le minimum.
    3. On cherche ensuite dans le reste de la liste (i+1 à fin)
       s'il existe un élément plus petit.
    4. Si on trouve un plus petit élément, on met à jour son indice.
    5. À la fin du parcours, on échange le minimum trouvé avec la position i.
    6. On répète jusqu'à trier toute la liste.

    Exemple :
    [5, 2, 8, 1]
    → Étape 1 : minimum = 1 → échange avec 5 → [1, 2, 8, 5]
    → Étape 2 : minimum = 2 → déjà bien placé
    → Étape 3 : minimum = 5 → échange avec 8 → [1, 2, 5, 8]
    """

    n = len(ligne)

    for i in range(n - 1):
        indice_min = i  # On suppose que le minimum est à la position i

        # Recherche du plus petit élément dans le reste de la liste
        for j in range(i + 1, n):
            if ligne[j] < ligne[indice_min]:
                indice_min = j

        # Échange si nécessaire
        if indice_min != i:
            ligne[i], ligne[indice_min] = ligne[indice_min], ligne[i]

    return ligne


def tri_selection_table(table):
    """
    Applique le tri par sélection sur le tableau 2D complet.

    Stratégie :
    1. On aplatit le tableau 2D en un tableau 1D.
    2. On trie ce tableau 1D avec l'algorithme de sélection.
    3. On reconstruit le tableau 2D trié avec les mêmes dimensions.

    Exemple :
    [[8, 3, 5],        aplatir →  [8, 3, 5, 1, 9, 2]
     [1, 9, 2]]        trier   →  [1, 2, 3, 5, 8, 9]
                       reconstruire → [[1, 2, 3],
                                        [5, 8, 9]]
    """
    nb_lignes = len(table)
    nb_colonnes = len(table[0])

    # Étape 1 : aplatir le tableau 2D en tableau 1D
    tableau_1d = aplatir(table)

    # Étape 2 : trier le tableau 1D avec le tri par sélection
    tri_selection_ligne(tableau_1d)

    # Étape 3 : reconstruire le tableau 2D à partir du tableau 1D trié
    return reconstruire(tableau_1d, nb_lignes, nb_colonnes)


# ==============================================================================
# TRI À BULLE
# ==============================================================================

def tri_bulle_ligne(ligne):
    """
    PRINCIPE DU TRI À BULLE :

    1. On parcourt la liste plusieurs fois.
    2. À chaque passage, on compare les éléments voisins.
    3. Si deux éléments sont mal ordonnés, on les échange.
    4. Les plus grands éléments "remontent" progressivement vers la fin.
    5. À chaque tour, la plus grande valeur restante se place à la fin.
    6. On répète jusqu'à ce que toute la liste soit triée.

    Exemple :
    [5, 3, 1]
    → Passage 1 : [3, 1, 5]
    → Passage 2 : [1, 3, 5]
    """

    n = len(ligne)

    for i in range(n - 1):
        for j in range(n - 1 - i):

            # Comparaison de deux éléments voisins
            if ligne[j] > ligne[j + 1]:
                # Échange si mal ordonné
                ligne[j], ligne[j + 1] = ligne[j + 1], ligne[j]

    return ligne


def tri_bulle_table(table):
    """
    Applique le tri à bulle sur le tableau 2D complet.

    Stratégie :
    1. On aplatit le tableau 2D en un tableau 1D.
    2. On trie ce tableau 1D avec l'algorithme à bulle.
    3. On reconstruit le tableau 2D trié avec les mêmes dimensions.

    Exemple :
    [[8, 3, 5],        aplatir →  [8, 3, 5, 1, 9, 2]
     [1, 9, 2]]        trier   →  [1, 2, 3, 5, 8, 9]
                       reconstruire → [[1, 2, 3],
                                        [5, 8, 9]]
    """
    nb_lignes = len(table)
    nb_colonnes = len(table[0])

    # Étape 1 : aplatir le tableau 2D en tableau 1D
    tableau_1d = aplatir(table)

    # Étape 2 : trier le tableau 1D avec le tri à bulle
    tri_bulle_ligne(tableau_1d)

    # Étape 3 : reconstruire le tableau 2D à partir du tableau 1D trié
    return reconstruire(tableau_1d, nb_lignes, nb_colonnes)


# ==============================================================================
# TRI PAR INSERTION
# ==============================================================================

def tri_insertion_ligne(ligne):
    """
    PRINCIPE DU TRI PAR INSERTION :

    1. On considère que le premier élément est déjà trié.
    2. On prend le deuxième élément et on le compare avec le précédent.
    3. On le décale vers la gauche jusqu'à trouver sa bonne position.
    4. On répète ce processus pour chaque élément suivant.

    Exemple :
    [5, 2, 4]
    → Étape 1 : [2, 5, 4]
    → Étape 2 : [2, 4, 5]
    """

    for i in range(1, len(ligne)):
        element = ligne[i]
        j = i - 1

        # Décalage des éléments plus grands
        while j >= 0 and ligne[j] > element:
            ligne[j + 1] = ligne[j]
            j -= 1

        # Insertion à la bonne position
        ligne[j + 1] = element

    return ligne


def tri_insertion_table(table):
    """
    Applique le tri par insertion sur le tableau 2D complet.

    Stratégie :
    1. On aplatit le tableau 2D en un tableau 1D.
    2. On trie ce tableau 1D avec l'algorithme par insertion.
    3. On reconstruit le tableau 2D trié avec les mêmes dimensions.

    Exemple :
    [[8, 3, 5],        aplatir →  [8, 3, 5, 1, 9, 2]
     [1, 9, 2]]        trier   →  [1, 2, 3, 5, 8, 9]
                       reconstruire → [[1, 2, 3],
                                        [5, 8, 9]]
    """
    nb_lignes = len(table)
    nb_colonnes = len(table[0])

    # Étape 1 : aplatir le tableau 2D en tableau 1D
    tableau_1d = aplatir(table)

    # Étape 2 : trier le tableau 1D avec le tri par insertion
    tri_insertion_ligne(tableau_1d)

    # Étape 3 : reconstruire le tableau 2D à partir du tableau 1D trié
    return reconstruire(tableau_1d, nb_lignes, nb_colonnes)


# ==============================================================================
# TRI RAPIDE
# ==============================================================================

def quicksort_1d(tableau):
    """
    FONCTIONNEMENT DU TRI RAPIDE (QUICKSORT) SUR UN TABLEAU 1D :

    1. Pivot : On choisit un élément 'pivot' dans le tableau (ici, l'élément du milieu).
    2. Partitionnement : On compare chaque élément par rapport au pivot.
       - 'gauche' contiendra les éléments < pivot.
       - 'milieu' contiendra les éléments == pivot.
       - 'droite' contiendra les éléments > pivot.
    3. Récursion : On répète l'opération sur 'gauche' et 'droite' jusqu'à ce que
       les sous-tableaux aient une taille de 0 ou 1 (déjà triés).
    4. Fusion : On recalle les morceaux : gauche + milieu + droite.

    Exemple :
    [5, 3, 8, 1, 9, 2]  →  pivot = 1 (milieu)
    gauche=[],  milieu=[1],  droite=[5, 3, 8, 9, 2]
    → récursion sur droite → [2, 3, 5, 8, 9]
    → résultat final : [1, 2, 3, 5, 8, 9]
    """
    if len(tableau) <= 1:
        return tableau

    # Choix du pivot : l'élément au milieu du tableau
    pivot = tableau[len(tableau) // 2]

    gauche = [x for x in tableau if x < pivot]
    milieu = [x for x in tableau if x == pivot]
    droite = [x for x in tableau if x > pivot]

    return quicksort_1d(gauche) + milieu + quicksort_1d(droite)


def quicksort_2d(table):
    """
    Applique le tri rapide sur le tableau 2D complet.

    Stratégie :
    1. On aplatit le tableau 2D en un tableau 1D.
    2. On trie ce tableau 1D avec l'algorithme quicksort.
    3. On reconstruit le tableau 2D trié avec les mêmes dimensions.

    Exemple :
    [[8, 3, 5],        aplatir →  [8, 3, 5, 1, 9, 2]
     [1, 9, 2]]        trier   →  [1, 2, 3, 5, 8, 9]
                       reconstruire → [[1, 2, 3],
                                        [5, 8, 9]]
    """
    nb_lignes = len(table)
    nb_colonnes = len(table[0])

    # Étape 1 : aplatir le tableau 2D en tableau 1D
    tableau_1d = aplatir(table)

    # Étape 2 : trier le tableau 1D avec le tri rapide
    tableau_1d_trie = quicksort_1d(tableau_1d)

    # Étape 3 : reconstruire le tableau 2D à partir du tableau 1D trié
    return reconstruire(tableau_1d_trie, nb_lignes, nb_colonnes)


# ==============================================================================
# TRI PAR FUSION
# ==============================================================================

def merge_sort_2d(tableau_2d):
    """
    Tri par fusion pour un tableau à deux dimensions.
    Le principe :
    1. Aplatir le tableau 2D en tableau 1D
    2. Appliquer le tri par fusion sur le tableau 1D
    3. Reconstruire le tableau 2D trié
    """

    # Vérification : si le tableau est vide ou si la première ligne est vide,
    # on retourne le tableau tel quel (cas limite)
    if not tableau_2d or not tableau_2d[0]:
        return tableau_2d

    # Récupération des dimensions du tableau 2D original
    # Ex: pour [[5, 3, 8], [1, 9, 2]], lignes=2 et colonnes=3
    nb_lignes = len(tableau_2d)
    nb_colonnes = len(tableau_2d[0])

    # ÉTAPE 1 : APLATIR le tableau 2D en un tableau 1D
    # On parcourt chaque cellule [i][j] du tableau 2D et on l'ajoute
    # à la suite dans un tableau 1D.
    # Ex: [[5, 3, 8], [1, 9, 2]] → [5, 3, 8, 1, 9, 2]
    tableau_1d = aplatir(tableau_2d)

    # ÉTAPE 2 : TRIER le tableau 1D avec le tri par fusion
    # On confie le tableau 1D à tri_fusion() qui le divise, trie
    # chaque moitié récursivement, puis fusionne les moitiés triées.
    # Ex: [5, 3, 8, 1, 9, 2] → [1, 2, 3, 5, 8, 9]
    tableau_1d_trie = tri_fusion(tableau_1d)

    # ÉTAPE 3 : RECONSTRUIRE le tableau 2D à partir du tableau 1D trié
    # On relit les valeurs triées une par une et on les replace
    # dans un nouveau tableau 2D ayant les mêmes dimensions que l'original.
    # Ex: [1, 2, 3, 5, 8, 9] (lignes=2, colonnes=3)
    #   → [[1, 2, 3], [5, 8, 9]]
    return reconstruire(tableau_1d_trie, nb_lignes, nb_colonnes)


def tri_fusion(tableau):
    """
    Algorithme de tri par fusion classique (récursif) pour un tableau 1D.

    Principe du tri par fusion :
    1. DIVISER  : couper le tableau en deux moitiés
    2. CONQUÉRIR: trier chaque moitié récursivement
    3. COMBINER : fusionner les deux moitiés triées en un seul tableau trié
    """

    # CAS DE BASE
    # Un tableau de 0 ou 1 élément est déjà trié par définition.
    # C'est la condition d'arrêt de la récursion.
    # Ex: tri_fusion([7]) → [7]  (rien à faire)
    if len(tableau) <= 1:
        return tableau

    # ÉTAPE 1 : DIVISER
    # On coupe le tableau en deux moitiés à partir de l'indice du milieu.
    # Ex: [5, 3, 8, 1, 9, 2]
    #       milieu = 6 // 2 = 3
    #       gauche = [5, 3, 8]   (indices 0 à milieu-1)
    #       droite = [1, 9, 2]   (indices milieu à fin)
    milieu = len(tableau) // 2
    gauche = tableau[:milieu]   # Première moitié
    droite = tableau[milieu:]   # Deuxième moitié

    # ÉTAPE 2 : CONQUÉRIR (appels récursifs)
    # On trie chaque moitié indépendamment par le même algorithme.
    # Chaque appel redivise encore le sous-tableau jusqu'au cas de base.
    # Ex: tri_fusion([5, 3, 8]) → [3, 5, 8]
    #     tri_fusion([1, 9, 2]) → [1, 2, 9]
    gauche_triee = tri_fusion(gauche)
    droite_triee = tri_fusion(droite)

    # ÉTAPE 3 : COMBINER
    # On fusionne les deux moitiés déjà triées en un seul tableau trié.
    # Ex: fusionner([3, 5, 8], [1, 2, 9]) → [1, 2, 3, 5, 8, 9]
    return fusionner(gauche_triee, droite_triee)


def fusionner(gauche, droite):
    """
    Fusionne deux tableaux DÉJÀ TRIÉS en un seul tableau trié.

    Principe :
    - On avance simultanément dans les deux tableaux avec deux indices i et j.
    - À chaque étape on compare gauche[i] et droite[j] et on copie
      le plus petit dans le résultat, puis on avance l'indice correspondant.
    - Quand l'un des deux tableaux est épuisé, on copie le reste de l'autre.
    """

    resultat = []
    i = j = 0  # i : curseur dans gauche | j : curseur dans droite

    # PHASE DE COMPARAISON : tant qu'il reste des éléments des deux côtés
    # Ex: gauche=[3,5,8], droite=[1,2,9]
    #   Tour 1 : 3 > 1  → on prend droite[0]=1,  j=1,  résultat=[1]
    #   Tour 2 : 3 > 2  → on prend droite[1]=2,  j=2,  résultat=[1,2]
    #   Tour 3 : 3 <= 9 → on prend gauche[0]=3,  i=1,  résultat=[1,2,3]
    #   Tour 4 : 5 <= 9 → on prend gauche[1]=5,  i=2,  résultat=[1,2,3,5]
    #   Tour 5 : 8 <= 9 → on prend gauche[2]=8,  i=3,  résultat=[1,2,3,5,8]
    #   → gauche épuisée, on sort de la boucle
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            # L'élément de gauche est plus petit (ou égal) : on le prend
            resultat.append(gauche[i])
            i += 1
        else:
            # L'élément de droite est plus petit : on le prend
            resultat.append(droite[j])
            j += 1

    # PHASE DE VIDAGE : copier les éléments restants
    # Un seul des deux tableaux peut encore avoir des éléments non copiés.
    # Ces éléments sont forcément plus grands que tout ce qui est déjà dans
    # résultat (car les tableaux étaient triés), on les ajoute tels quels.

    # Éléments restants dans gauche (droite est épuisée)
    # Ex (suite): droite épuisée, il reste droite[2]=9 → résultat=[1,2,3,5,8,9]
    while i < len(gauche):
        resultat.append(gauche[i])
        i += 1

    # Éléments restants dans droite (gauche est épuisée)
    while j < len(droite):
        resultat.append(droite[j])
        j += 1

    return resultat


# ==============================================================================
# RECHERCHE
# ==============================================================================

def table_vers_liste_triee(table):
    """Aplatit la table 2D en une liste 1D triée (utilisé en interne)."""
    liste = []
    for ligne in table:
        liste.extend(ligne)
    liste.sort()
    return liste


# ==============================================================================
# RECHERCHE LINÉAIRE
# ==============================================================================
#
# Principe :
#   On parcourt la table case par case, ligne par ligne, et on compare
#   chaque élément avec la valeur cherchée.
#   Aucune contrainte : la table peut être non triée.
#   Complexité : O(n * m) dans le pire cas (toute la table parcourue).
#
# Exemple :
#   table = [[12, 45,  7],
#            [33, 21,  8],
#            [19, 42,  5]]
#   valeur = 21
#
#   → ligne 0 : 12 ≠ 21, 45 ≠ 21, 7 ≠ 21
#   → ligne 1 : 33 ≠ 21, 21 == 21  ✓  trouvé en (1, 4)
#
# Retourne :
#   - "trouve"   : True ou False
#   - "position" : (ligne, colonne) si trouvé, sinon None
#   - "etapes"   : nombre de comparaisons effectuées
# ==============================================================================

def recherche_lineaire(table, valeur):
    etapes = 0

    for i, ligne in enumerate(table):
        for j, element in enumerate(ligne):
            etapes += 1

            if element == valeur:
                return {"trouve": True, "position": (i, j), "etapes": etapes}

    return {"trouve": False, "position": None, "etapes": etapes}


# ==============================================================================
# RECHERCHE BINAIRE  (itérative)
# ==============================================================================
#
# Principe :
#   La table est d'abord aplatie et triée en une liste 1D.
#   On définit deux bornes (gauche et droite) qui encadrent l'intervalle
#   de recherche. À chaque tour de boucle :
#     1. On calcule l'indice du milieu : milieu = (gauche + droite) // 2
#     2. On compare liste[milieu] avec la valeur cherchée :
#          - égal       → trouvé !
#          - trop petit → on cherche à droite  (gauche = milieu + 1)
#          - trop grand → on cherche à gauche  (droite = milieu - 1)
#   On répète jusqu'à trouver ou jusqu'à ce que gauche > droite.
#   Complexité : O(log n)  — beaucoup plus rapide que la recherche linéaire.
#
# Exemple :
#   liste_triee = [5, 7, 8, 12, 19, 21, 33, 42, 45]
#   valeur = 21
#
#   Étape 1 : gauche=0, droite=8, milieu=4 → liste[4]=19 < 21 → gauche=5
#   Étape 2 : gauche=5, droite=8, milieu=6 → liste[6]=33 > 21 → droite=5
#   Étape 3 : gauche=5, droite=5, milieu=5 → liste[5]=21 == 21  ✓  trouvé !
#
# Retourne :
#   - "trouve"       : True ou False
#   - "indice_liste" : indice dans la liste triée si trouvé, sinon None
#   - "liste_triee"  : la liste 1D triée utilisée
#   - "etapes"       : nombre de comparaisons effectuées
# ==============================================================================

def recherche_binaire(table, valeur):
    liste = table_vers_liste_triee(table)
    gauche = 0
    droite = len(liste) - 1
    etapes = 0

    while gauche <= droite:
        etapes += 1
        milieu = (gauche + droite) // 2

        if liste[milieu] == valeur:
            return {"trouve": True, "indice_liste": milieu, "liste_triee": liste, "etapes": etapes}
        elif liste[milieu] < valeur:
            gauche = milieu + 1  # on cherche dans la moitié droite
        else:
            droite = milieu - 1  # on cherche dans la moitié gauche

    return {"trouve": False, "indice_liste": None, "liste_triee": liste, "etapes": etapes}


# ==============================================================================
# RECHERCHE PAR DICHOTOMIE  (récursive)
# ==============================================================================
#
# Principe :
#   Même logique que la recherche binaire (diviser l'intervalle par deux),
#   mais implémentée de façon RÉCURSIVE : la fonction s'appelle elle-même
#   avec un intervalle réduit à chaque appel.
#
#   Cas de base (arrêt de la récursion) :
#     - gauche > droite       → valeur absente, on retourne -1
#     - liste[milieu] == valeur → trouvé, on retourne l'indice
#
#   Cas récursifs :
#     - liste[milieu] < valeur → appel sur [milieu+1 .. droite]
#     - liste[milieu] > valeur → appel sur [gauche .. milieu-1]
#
#   Complexité : O(log n) — identique à la binaire itérative.
#
# Différence avec la recherche binaire :
#   Binaire    → boucle while  (itératif)
#   Dichotomie → appels récursifs (récursif)
#
# Exemple :
#   liste_triee = [5, 7, 8, 12, 19, 21, 33, 42, 45]
#   valeur = 8
#
#   Appel 1 : intervalle [0..8], milieu=4, liste[4]=19 > 8 → appel sur [0..3]
#   Appel 2 : intervalle [0..3], milieu=1, liste[1]=7  < 8 → appel sur [2..3]
#   Appel 3 : intervalle [2..3], milieu=2, liste[2]=8 == 8  ✓  trouvé !
#
# Retourne :
#   - "trouve"       : True ou False
#   - "indice_liste" : indice dans la liste triée si trouvé, sinon None
#   - "liste_triee"  : la liste 1D triée utilisée
#   - "etapes"       : nombre d'appels récursifs effectués
# ==============================================================================

def _dichotomie_recursive(liste, valeur, gauche, droite, etapes):
    """Fonction interne récursive — ne pas appeler directement."""
    if gauche > droite:
        return -1  # cas de base : valeur absente

    etapes[0] += 1
    milieu = (gauche + droite) // 2

    if liste[milieu] == valeur:
        return milieu  # cas de base : trouvé
    elif liste[milieu] < valeur:
        return _dichotomie_recursive(liste, valeur, milieu + 1, droite, etapes)
    else:
        return _dichotomie_recursive(liste, valeur, gauche, milieu - 1, etapes)


def recherche_dichotomie(table, valeur):
    liste = table_vers_liste_triee(table)
    etapes = [0]  # liste pour passer le compteur par référence entre les appels récursifs

    indice = _dichotomie_recursive(liste, valeur, 0, len(liste) - 1, etapes)

    if indice != -1:
        return {"trouve": True, "indice_liste": indice, "liste_triee": liste, "etapes": etapes[0]}
    else:
        return {"trouve": False, "indice_liste": None, "liste_triee": liste, "etapes": etapes[0]}
