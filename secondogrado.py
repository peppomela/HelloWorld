#Programma che risolve le equazioni di secondo grado
import math
print "Risolvi l'equazione di secondo grado"
print "        Ax^2 + Bx + C = 0 \n"

a=input('A= ')
b=input('B= ')
c=input('C= ')

if a==0 and b==0 and c==0:
     print "L'equazione ammette infinite soluzioni!"

elif a==0 and b==0:
     print "L'equazione",c,"=0 non ammette soluzioni!"

elif a==0:
     print "L'equazione e' di primo grado"
     print "La soluzione e' = ", -float(c)/float(b)

else:
     delta = b*b-4*a*c
     if delta<0:
          print "L'equazione non ammette soluzioni reali"

     elif delta == 0:
	  print "Delta uguale a zero l'equazione ha due soluzioni coincidenti"
	  var=-float(b)/(2.0*float(a))
	  print "x1,2 =",var
     else:
	  print"L'equazione ammette due soluzioni"
	  radice=math.sqrt(delta)
	  x1=(-float(b) - radice)/(2.0 * float(a))
	  x2=(-float(b) + radice)/(2.0 * float(a))
	  print"x1 = ",x1
	  print"\nx2 = ",x2
