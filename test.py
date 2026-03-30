import module as tr

# ==============================================================================
# FICHIER DE TEST — MODULE tri_recherche_2d
# ==============================================================================
# Ce fichier teste tous les algorithmes de tri et de recherche du module
# sur une table à deux dimensions initialisée aléatoirement.
# ==============================================================================


# ------------------------------------------------------------------------------
# GÉNÉRATION DE LA TABLE DE TEST
# ------------------------------------------------------------------------------

print("=" * 60)
print("       TEST DU MODULE tri_recherche_2d")
print("=" * 60)

# On génère une table 3x5 aléatoire qui servira de base pour tous les tests
table_originale = tr.generer_table(nb_lignes=3, nb_colonnes=5)
tr.afficher_table(table_originale, "Table originale (aléatoire)")


# ==============================================================================
# TESTS DES ALGORITHMES DE TRI
# ==============================================================================

print("=" * 60)
print("               ALGORITHMES DE TRI")
print("=" * 60)

# ------------------------------------------------------------------------------
# TRI PAR SÉLECTION
# ------------------------------------------------------------------------------
print("\n[ TRI PAR SÉLECTION ]")
print("Principe : à chaque étape, on cherche le minimum dans la partie")
print("non triée et on le place à sa position définitive.\n")

# On fait une copie pour ne pas modifier la table originale
import copy
table_test = copy.deepcopy(table_originale)
tr.afficher_table(table_test, "Avant tri par sélection")
resultat = tr.tri_selection_table(table_test)
tr.afficher_table(resultat, "Après tri par sélection")


# ------------------------------------------------------------------------------
# TRI À BULLE
# ------------------------------------------------------------------------------
print("\n[ TRI À BULLE ]")
print("Principe : on compare les voisins et on fait remonter les grands")
print("éléments vers la fin, comme des bulles.\n")

table_test = copy.deepcopy(table_originale)
tr.afficher_table(table_test, "Avant tri à bulle")
resultat = tr.tri_bulle_table(table_test)
tr.afficher_table(resultat, "Après tri à bulle")


# ------------------------------------------------------------------------------
# TRI PAR INSERTION
# ------------------------------------------------------------------------------
print("\n[ TRI PAR INSERTION ]")
print("Principe : on insère chaque élément à sa bonne place dans la")
print("partie déjà triée, comme on trie des cartes à jouer.\n")

table_test = copy.deepcopy(table_originale)
tr.afficher_table(table_test, "Avant tri par insertion")
resultat = tr.tri_insertion_table(table_test)
tr.afficher_table(resultat, "Après tri par insertion")


# ------------------------------------------------------------------------------
# TRI RAPIDE (QUICKSORT)
# ------------------------------------------------------------------------------
print("\n[ TRI RAPIDE (QUICKSORT) ]")
print("Principe : on choisit un pivot, on sépare les éléments plus petits")
print("et plus grands, puis on répète récursivement sur chaque partie.\n")

table_test = copy.deepcopy(table_originale)
tr.afficher_table(table_test, "Avant tri rapide")
resultat = tr.quicksort_2d(table_test)
tr.afficher_table(resultat, "Après tri rapide")


# ------------------------------------------------------------------------------
# TRI PAR FUSION
# ------------------------------------------------------------------------------
print("\n[ TRI PAR FUSION ]")
print("Principe : on divise le tableau en deux moitiés, on trie chacune")
print("récursivement, puis on fusionne les deux moitiés triées.\n")

table_test = copy.deepcopy(table_originale)
tr.afficher_table(table_test, "Avant tri par fusion")
resultat = tr.merge_sort_2d(table_test)
tr.afficher_table(resultat, "Après tri par fusion")


# ------------------------------------------------------------------------------
# VÉRIFICATION : tous les tris donnent le même résultat
# ------------------------------------------------------------------------------
print("\n[ VÉRIFICATION : cohérence des 5 tris ]")

t1 = tr.tri_selection_table(copy.deepcopy(table_originale))
t2 = tr.tri_bulle_table(copy.deepcopy(table_originale))
t3 = tr.tri_insertion_table(copy.deepcopy(table_originale))
t4 = tr.quicksort_2d(copy.deepcopy(table_originale))
t5 = tr.merge_sort_2d(copy.deepcopy(table_originale))

if t1 == t2 == t3 == t4 == t5:
    print("Tous les algorithmes produisent le même résultat trié.")
else:
    print("Attention : les résultats diffèrent entre les algorithmes !")


# ==============================================================================
# TESTS DES ALGORITHMES DE RECHERCHE
# ==============================================================================

print("\n" + "=" * 60)
print("            ALGORITHMES DE RECHERCHE")
print("=" * 60)

# On utilise la table triée comme base de recherche
# et on choisit une valeur qui existe dans la table
table_triee = tr.tri_selection_table(copy.deepcopy(table_originale))
tr.afficher_table(table_triee, "Table utilisée pour la recherche")

# On récupère une valeur qui existe à coup sûr (premier élément de la table)
valeur_existante = table_triee[0][0]
# On choisit une valeur qui n'existe probablement pas
valeur_absente = 999

print(f"  Valeur recherchée (existante) : {valeur_existante}")
print(f"  Valeur recherchée (absente)   : {valeur_absente}\n")


# ------------------------------------------------------------------------------
# RECHERCHE LINÉAIRE
# ------------------------------------------------------------------------------
print("\n[ RECHERCHE LINÉAIRE ]")
print("Principe : on parcourt chaque case une par une jusqu'à trouver")
print("la valeur. Fonctionne sur une table non triée.\n")

# Test avec valeur existante
res = tr.recherche_lineaire(table_triee, valeur_existante)
if res["trouve"]:
    print(f" Valeur {valeur_existante} trouvée en position {res['position']} "
          f"en {res['etapes']} étape(s).")
else:
    print(f" Valeur {valeur_existante} non trouvée après {res['etapes']} étape(s).")

# Test avec valeur absente
res = tr.recherche_lineaire(table_triee, valeur_absente)
if res["trouve"]:
    print(f" Valeur {valeur_absente} trouvée en position {res['position']} "
          f"en {res['etapes']} étape(s).")
else:
    print(f" Valeur {valeur_absente} non trouvée après {res['etapes']} étape(s).")


# ------------------------------------------------------------------------------
# RECHERCHE BINAIRE (itérative)
# ------------------------------------------------------------------------------
print("\n[ RECHERCHE BINAIRE — itérative ]")
print("Principe : on divise l'intervalle de recherche par deux à chaque")
print("étape (itératif). Nécessite une liste triée.\n")

# Test avec valeur existante
res = tr.recherche_binaire(table_triee, valeur_existante)
if res["trouve"]:
    print(f"Valeur {valeur_existante} trouvée à l'indice {res['indice_liste']} "
          f"dans la liste triée en {res['etapes']} étape(s).")
    print(f"     Liste triée utilisée : {res['liste_triee']}")
else:
    print(f"Valeur {valeur_existante} non trouvée après {res['etapes']} étape(s).")

# Test avec valeur absente
res = tr.recherche_binaire(table_triee, valeur_absente)
if res["trouve"]:
    print(f"Valeur {valeur_absente} trouvée à l'indice {res['indice_liste']} "
          f"en {res['etapes']} étape(s).")
else:
    print(f"Valeur {valeur_absente} non trouvée après {res['etapes']} étape(s).")


# ------------------------------------------------------------------------------
# RECHERCHE PAR DICHOTOMIE (récursive)
# ------------------------------------------------------------------------------
print("\n[ RECHERCHE PAR DICHOTOMIE — récursive ]")
print("Principe : même logique que la binaire, mais avec des appels")
print("récursifs au lieu d'une boucle. Nécessite une liste triée.\n")

# Test avec valeur existante
res = tr.recherche_dichotomie(table_triee, valeur_existante)
if res["trouve"]:
    print(f"Valeur {valeur_existante} trouvée à l'indice {res['indice_liste']} "
          f"dans la liste triée en {res['etapes']} appel(s) récursif(s).")
    print(f"     Liste triée utilisée : {res['liste_triee']}")
else:
    print(f"Valeur {valeur_existante} non trouvée après {res['etapes']} appel(s).")

# Test avec valeur absente
res = tr.recherche_dichotomie(table_triee, valeur_absente)
if res["trouve"]:
    print(f"Valeur {valeur_absente} trouvée à l'indice {res['indice_liste']} "
          f"en {res['etapes']} appel(s).")
else:
    print(f"Valeur {valeur_absente} non trouvée après {res['etapes']} appel(s).")


# ------------------------------------------------------------------------------
# COMPARAISON DU NOMBRE D'ÉTAPES ENTRE LES 3 RECHERCHES
# ------------------------------------------------------------------------------
print("\n[ COMPARAISON DU NOMBRE D'ÉTAPES ]")
print("On compare le nombre de comparaisons effectuées par chaque")
print(f"algorithme pour rechercher la valeur {valeur_existante}.\n")

etapes_lin  = tr.recherche_lineaire(table_triee, valeur_existante)["etapes"]
etapes_bin  = tr.recherche_binaire(table_triee, valeur_existante)["etapes"]
etapes_dich = tr.recherche_dichotomie(table_triee, valeur_existante)["etapes"]

print(f"  Recherche linéaire   : {etapes_lin} étape(s)")
print(f"  Recherche binaire    : {etapes_bin} étape(s)")
print(f"  Recherche dichotomie : {etapes_dich} étape(s)")
print()
print("  → Binaire et dichotomie sont plus rapides que la linéaire")
print("    car elles divisent l'espace de recherche par deux à chaque étape.")

print("\n" + "=" * 60)
print("               FIN DES TESTS")
print("=" * 60)
