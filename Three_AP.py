import matplotlib.pyplot as plt
import math
import distance_mobile



# Coordonnées des trois points d'accès
access_point_1 = (5, 5)  # Premier point d'accès
access_point_2 = (10, 10)  # Deuxième point d'accès
access_point_3 = (15, 13)  # Troisième point d'accès

# RSSI mesurés pour chaque point d'accès (en dBm)
rssi_1 = -80  # RSSI mesuré au point d'accès 1
rssi_2 = -85  # RSSI mesuré au point d'accès 2
rssi_3 = -90  # RSSI mesuré au point d'accès 3

# Paramètres de la formule de calcul de distance
P0 = -65   # Puissance de référence à 1 mètre (en dBm)
Fm = 3     # Marge de défaillance (fading margin) en dB
n = 2.5    # Facteur d'atténuation pour un environnement intérieur
f = 5800   # Fréquence WiFi en MHz (pour du WiFi 5 GHz)

# Calculer les distances en fonction du RSSI
d1 = distance_mobile.calculate_distance(P0, Fm, rssi_1, n, f)  # Distance au point d'accès 1
d2 =  distance_mobile.calculate_distance(P0, Fm, rssi_2, n, f)  # Distance au point d'accès 2
d3 =  distance_mobile.calculate_distance(P0, Fm, rssi_3, n, f)  # Distance au point d'accès 3

plt.figure()

# Limites des axes pour le tracé
plt.axis([0, 20, 0, 20])
plt.axis("equal")

# Dessiner les points d'accès
plt.plot(access_point_1[0], access_point_1[1], 'ro', label="Point d'accès 1")
plt.plot(access_point_2[0], access_point_2[1], 'go', label="Point d'accès 2")
plt.plot(access_point_3[0], access_point_3[1], 'bo', label="Point d'accès 3")

# Ajouter les cercles représentant les distances du mobile
circle1 = plt.Circle(access_point_1, radius=d1, color='r')
circle2 = plt.Circle(access_point_2, radius=d2, color='g')
circle3 = plt.Circle(access_point_3, radius=d3, color='b')

ax = plt.gca()
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

plt.legend()
plt.title("Détermination de la position d'un mobile par RSSI")

# Calculer la position du mobile par intersection (simple estimation)
# Pour simplifier, calculons un point proche du centre des trois cercles (moyenne pondérée par les distances). 

mobile_x = (access_point_1[0] * d1 + access_point_2[0] * d2 + access_point_3[0] * d3) / (d1 + d2 + d3)
mobile_y = (access_point_1[1] * d1 + access_point_2[1] * d2 + access_point_3[1] * d3) / (d1 + d2 + d3)

# Dessiner le mobile estimé
plt.plot(mobile_x, mobile_y, 'ko', label="Position estimée du mobile")

plt.show()

print(f"Distance au point d'accès 1: {d1:.2f} m")
print(f"Distance au point d'accès 2: {d2:.2f} m")
print(f"Distance au point d'accès 3: {d3:.2f} m")
