#incollare con tasto destro il testo della canzone, lasciare una riga di spazio e cliccare CTRL+Z+INVIO
import sys
import tabulate 
testo = sys.stdin.read().strip()
parole = testo.lower().split()
print("--------------------------------------------------------")

vettore = []

for parola in parole:
    vettore.append(parola)

# creiamo un dizionario per contare le parole
conteggio = {}

for parola in vettore:
    if parola not in ["e","o","di","a","da","in","con","su","per","tra","fra","il","la","le","lo","i","gli","un","uno","una","del", "dei","che", "non","me","mi","te","ti","si","ne","ci","ce","vi","ve" ]:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1

parole_ordinate = sorted(conteggio, key=conteggio.get, reverse=True)

# crea la lista delle parole più frequenti
paroleTop5 = []
for i, parola in enumerate(parole_ordinate[:5]):
    paroleTop5.append([parola, conteggio[parola]])

# stampa la tabella
print("{:<10} {:<10}".format('Parola', 'Conteggio'))
print('-' * 20)
for parola, conteggio in paroleTop5:
    print("{:<10} {:<10}".format(parola, conteggio))


    


