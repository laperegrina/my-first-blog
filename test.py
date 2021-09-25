from typing import get_origin


a = 5
x = 3

print(a + x)
print("mein text")
print(type(a))


meine_liste = ["Birke", "Buche", "Pflanze", 28]
print(type(meine_liste))
print(meine_liste[2])
print(meine_liste[3]+2)

# Blaues Haus mit Garten und 3 Zimmern
mein_haus = ["blau", "garten",3]
print(mein_haus[0])

beispiel_dictionary = {"Farbe": "blau", "Hat Garten?": "ja", "Anzahl Zimmer" : 3, }

print(beispiel_dictionary["Anzahl Zimmer"])
print(beispiel_dictionary["Hat Garten?"])
anas_haus = {"Farbe": "rosa", "Hat Garten?": "ja", "Anzahl Zimmer" : 3, }
peres_haus = {"Farbe": "olivgrün", "Hat Garten?": "ja", "Anzahl Zimmer" : 4, }
sophias_haus = {"Farbe":"lila", "Hat Garten?": "ja", "Anzahl Zimmer" : 5, }

if anas_haus["Anzahl Zimmer"] > 3:
    print("Anas Haus ist groß")
else:
   print("Anas Haus ist klein")