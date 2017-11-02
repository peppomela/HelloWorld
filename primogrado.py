#programma che risolve equazioni di primo grado
print "Equazioni di primo grado"
print "      Ax + B = 0\n"
A = input('A: ')
B = input('B: ')

if A==0 and B==0:
    print "L'equazione 0 = 0 ammette infite soluzioni"
elif A==0:
    print "L'equazione", B,"=0 non ammette soluzioni"
else:
    x = -float(B) / float(A)
    print "L'equazione ammette soluzione :",x
