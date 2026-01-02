from tabulate import tabulate
import sys

ls = []

while True:

    while True:
        nome = input("Inserisci Nome (oppure 'q' per uscire): ")
        if nome.strip().lower() == 'q':
            print("\n❌ USCITA DAL PROGRAMMA DURANTE INSERIMENTO NOME ❌")
            sys.exit()
        elif nome.strip() == "":
            print("⚠️ Inserisci un nome valido.")
        else:
            break

    while True:
        eta = input("Inserisci Età (oppure 'q' per uscire): ")
        if eta.strip().lower() == 'q':
            print("\n❌ USCITA DAL PROGRAMMA DURANTE INSERIMENTO ETÀ ❌")
            sys.exit()
        elif eta.strip() == "":
            print("⚠️ Età non valida.")
        else:
            break

    while True:
        lavoro = input("Inserisci Professione (oppure 'q' per uscire): ")
        if lavoro.strip().lower() == 'q':
            print("\n❌ USCITA DAL PROGRAMMA DURANTE INSERIMENTO PROFESSIONE ❌")
            sys.exit()
        elif lavoro.strip() == "":
            print("⚠️ Professione non valida.")
        else:
            break

    data = [nome, eta, lavoro]
    ls.append(data)

    print("\n✅ DATI OK -- CREAZIONE TABELLA ✅\n")
    hds = ['Nome', 'Età', 'Professione']
    print(tabulate(ls, headers=hds, tablefmt="grid"))

    print("\n🚪 CHIUSURA \n")

    cnt = input('Continuare? (y / n)')

    if cnt.strip().lower() == 'y' :
        continue
    else :
        print("\n🚪 CHIUSURA -- BYE BYE! \n")
        break


