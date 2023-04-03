import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Lire les données
data = pd.read_csv('data.csv')

# Calculer les statistiques
mean = np.mean(data['values'])
std = np.std(data['values'])
min_value = np.min(data['values'])
max_value = np.max(data['values'])

# Afficher les statistiques
print('Moyenne :', mean)
print('Écart type :', std)
print('Minimum :', min_value)
print('Maximum :', max_value)

# Afficher l'histogramme des données
plt.hist(data['values'], bins=10)
plt.title('Histogramme des données')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.show()

# Enregistrer l'histogramme des données
plt.hist(data['values'], bins=10)
plt.title('Histogramme des données')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')
plt.savefig('histogramme.png')

# Afficher le graphique en boîte des données
plt.boxplot(data['values'])
plt.title('Graphique en boîte des données')
plt.ylabel('Valeurs')
plt.show()

# Enregistrer le graphique en boîte des données
plt.boxplot(data['values'])
plt.title('Graphique en boîte des données')
plt.ylabel('Valeurs')
plt.savefig('graphique_en_boite.png')
