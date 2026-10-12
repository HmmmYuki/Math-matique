import numpy as np      # convention : on l'abrège en "np"

entrees = np.array([2.0, 3.0])     # un tableau de 2 nombres
poids   = np.array([0.5, -1.0])    # les poids associés

# np.dot fait la somme pondérée d'un coup : (2*0.5) + (3*-1.0)
z = np.dot(entrees, poids)
print(z)        # affiche -2.0
