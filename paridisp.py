#Programma che verifica se un valore e' pari o dispari
valore=input("Inserisci un valore = ")
verifica=valore % 2

if verifica==0:
	print "Il valore ",valore," e' pari"
else:
	print "Il valore ",valore," e' dispari"
