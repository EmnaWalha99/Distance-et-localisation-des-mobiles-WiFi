import math

def calculate_distance(P0, Pr, n):
    """
    Calculate the distance based on RSSI values and path loss exponent.
    
    P0: RSSI at 1 meter (dBm)
    Pr: RSSI at the current distance (dBm)
    n: Path loss exponent (typical values are 2-4)
    """
    distance = 10 ** ((P0 - Pr) / (10 * n))
    return distance

# Example values
P0 = -50    # Reference signal power at 1 meter, in dBm
Pr = -70    # Measured RSSI at a certain distance, in dBm
n = 3       # Path loss exponent for indoor environment with walls

# Calculate distance
distance = calculate_distance(P0, Pr, n)
print(f"Estimated distance from the AP: {distance:.2f} meters")
