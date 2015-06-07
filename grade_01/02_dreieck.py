# Aendere dieses Programm, damit es den Flaecheninhalt und Umfang
# eines Rechtwinkligen Dreiecks berechnet. 
#
# Hinweis: Die Katheten sind die Seiten, zwischen denen der rechte Winkel ist
#          Die Hypothenuse ist die Seite, die dem rechten Winkel gegenueber 
#          liegt
#         
#          Wenn Du nicht weiter kommst, schaue nochmal in dem Rechteck-Programm
#          nach

class Dreieck:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def umfang(self):
        return 0

    def flaeche(self):
        # Hier bitte Deine Loesung einfuegen
        return 0


a = int(raw_input("Laenge Kathete a:"))
b = int(raw_input("Laenge Kathete b:"))
c = int(raw_input("Laenge Hypothenuse c:"))

d = Dreieck(a,b)
print "Umfang: " + str(d.umfang())
print "Flaeche: " + str(d.flaeche())

