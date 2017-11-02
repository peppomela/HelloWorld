#Programma che calcola o il volume di un cubo o di una sfera
import math
print "calcolo del volume"
scelta=input("inserisci (1 per il cubo / 2 per la sfera) = ")

if scelta==1:
	print "--Hai scelto il cubo--"
	lato=input("Inserisci il lato = ")
	volume=lato*lato*lato
	print"Il volume e' = ",volume
elif scelta==2:
	print "----Hai scelto la sfera----"
	raggio=input("Inserisci il raggio = ")
	volume= 4. / 3. * math.pi * raggio * raggio * raggio
	print "IL volume e' = ",volume
else:
     print "Scelta sbagliata"

