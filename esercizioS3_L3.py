def Calcolaperquad():
    print("Inserisci valore del lato:")
    lato = input()
    print("Il perimetro del quadrato è: " + str(int(lato) * 4))

def Calcolocirconfer():
    print("Inserisci valore del raggio:")
    raggio = input()
    print("La circonferenza è: " + str(int(raggio) * 2 * 3.14)) 

def Calcoloperim():
    print("Inserisci valore della base ed altezza:")
    base = input()
    altezza = input()
    print("Il valore del perimetro è: " + str(int(base) * 2 + int(altezza) * 2))

print("Benvenuto in questo programma")
print("Per avviare, premi:")
print("1 -> per il perimetro del quadrato")
print("2 -> per la circonferenza")
print("3 -> per il perimetro del rettangolo")

scelta = input()
if int(scelta) == 1:
    Calcolaperquad()
elif int(scelta) == 2:
    Calcolocirconfer()
elif int(scelta) == 3:
    Calcoloperim()
else:
    print("Ritenta sarai più fortunato!!!")
    
                  
                 
            
    