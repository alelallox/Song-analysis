#paste with the right_click, leave a space line and click CTRL+Z+ENTER
import sys
import tabulate 
#reads the copied text and divides it word by word 
testo = sys.stdin.read().strip()
parole = testo.lower().split()
print("--------------------------------------------------------")

vettore = []

for parola in parole:
    vettore.append(parola)

#creation of a dictionary to count words
conteggio = {}

for parola in vettore:
    #exclude not important words like conjunctions and prepositions
    if parola not in ["e","o","di","a","da","in","con","su","per","tra","fra","il","la","le","lo","i","gli","un","uno","una","del", "dei","che", "non","me","mi","te","ti","si","ne","ci","ce","vi","ve" ]:
        #adds words to the dictionary, if they are already present adds an int value (word count)
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1

parole_ordinate = sorted(conteggio, key=conteggio.get, reverse=True)

#create the most frequent word list
paroleTop5 = []
for i, parola in enumerate(parole_ordinate[:5]):
    paroleTop5.append([parola, conteggio[parola]])

#print the table
print("{:<10} {:<10}".format('Parola', 'Conteggio'))
print('-' * 20)
for parola, conteggio in paroleTop5:
    print("{:<10} {:<10}".format(parola, conteggio))


    


