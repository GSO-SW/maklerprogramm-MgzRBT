# Im folgenden ein Python Programm zur Markler PAP Aufgabe von Nico Ohlig, Abdullah Karagöz, Patric Peter

# Variablen festlegen bzw. definieren
raumAnzahl = int(input("Wie viele Räume gibt es?: "))
aktuellerRaum = 1
raumListe = []
gesamteWohnungsGroesse = 0

# Klassen definieren
class Raum: 
    def __init__(self, name):
        self._name = name 

    def getGroesse(self):
        return self._groesse

    def getName(self):
        return self._name
        
    def setGroesse(self,groesse):
        self._groesse = groesse

# Hier startet das Programm
while(aktuellerRaum <= raumAnzahl): 
    print("----------------------------------------------------")
    tempNeuerRaum = Raum(input("Wie soll der Raum " + str(aktuellerRaum) + " heißen?: "))
    print("----------------------------------------------------")
    temp_Grundflaeche = float(input("Länge des Raums: ")) * float(input("Breite des Raums: "))
    print("----------------------------------------------------")
    temp_HatEinkerbung = input("Hat der Raum eine Einkerbung? ja or nein: ")

    if(temp_HatEinkerbung == "ja"): 
        temp_Einkerbung =  float(input("Länge der Einkerbung: ")) * float(input("Breite der Einkerbung: "))
        temp_Gesamtflaeche = temp_Grundflaeche - temp_Einkerbung    
        tempNeuerRaum.setGroesse(temp_Gesamtflaeche) 

    if(temp_HatEinkerbung == "nein"): 
        tempNeuerRaum.setGroesse(temp_Grundflaeche)

    raumListe.append(tempNeuerRaum)
    aktuellerRaum += 1

print("----------------------------------------------------")

#Berechnung der Gesamtgroesse
for raum in raumListe: 
    print("Der Raum " + str(raum.getName()) + " hat die Groesse: " + str(raum.getGroesse()))
    gesamteWohnungsGroesse += raum.getGroesse()

print("Die Gesamtgroesse beträgt: " + str(gesamteWohnungsGroesse))