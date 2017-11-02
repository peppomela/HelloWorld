#programma che calcola superficie e volume di una sfera
import math
print "Inserisci il raggio della sfera"
raggio=input()
superficie= 4. * math.pi * raggio * raggio
volume = 4. / 3. * math.pi * raggio * raggio * raggio

print "La sfera ha la superficie di =", superficie, "e il volume di =", volume
