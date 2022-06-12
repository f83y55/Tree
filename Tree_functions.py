from Tree import *
##################################################################################################
# Pour générer des fichiers html contenant les arbres d'appel de plusieurs fonctions récursives, #
# Pour chaque fonction : la décorer avec '@make', et lancer un appel (ex : fibo(6) pour 6 en     #
# racine de l'arbre) après sa définition. Après la suite de fonctions décorés / appels, écrire   #
# Tree.do()                                                                                      #
##################################################################################################

@make
def fibo(n) :
    if n==0 or n==1 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

fibo(6)

@make
def sfibo(n) :
    if n==0 or n==1 :
        return 1
    else :
        s = 0
        for k in range(n) :
            s += sfibo(k)
        return s

sfibo(4)

@make
def somme_max(i, j) :
    T=[ [4, 1, 1, 3], [2, 0, 2, 1], [3, 1, 5, 1] ]
    if i==0 and j==0 :
        return T[0][0]
    elif i==0 :
        return T[0][j] + somme_max(0, j-1)
    elif j==0 :
        return T[i][0] + somme_max(i-1, 0)
    else :
        return T[i][j] + max( somme_max(i-1, j), somme_max(i, j-1) )

somme_max(2,3)

@make
def acker(m,n):
    if m == 0:             # Cas trivial
        return n+1
    if n == 0:             # Cas récursif
        return acker(m -1 ,1)
    return acker(m -1, acker(m, n -1))   # Cas récursif imbriqué

acker(2,3)


# Construction des arbres :
Tree.do()
