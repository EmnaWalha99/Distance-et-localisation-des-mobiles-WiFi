import math

def calculate_distance(P0, Fm, Pr, n, f):
    """
    P0 -- Puissance de référence à 1 mètre du point d'accès (en dBm)
    Fm -- Marge de défaillance (fading margin) en dB
    Pr -- Puissance du signal reçu (RSSI) en dBm
    n -- Facteur d'atténuation de l'environnement
    f -- Fréquence du signal en MHz

    """
    distance = 10 ** ((P0 - Fm - Pr - 10 * n * math.log10(f) + 30 * n - 32.44) / (10 * n))
    return distance

"""
P0 = -65   
Fm = 3     
Pr = -80      # Puissance du signal reçu (en dBm)
n = 2.5        # Facteur d'atténuation pour un environnement intérieur
f = 5800     # Fréquence WiFi en MHz (pour du WiFi 2.4 GHz)
"""

#distance = calculate_distance(P0=-65, Fm=3, Pr=-80, n=2.5, f=5800)
#print(f"La distance estimee entre le mobile et le point d'accès est de : {distance:.2f} mètres")
