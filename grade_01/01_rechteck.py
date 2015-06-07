#Aendere dieses Programm, damit es den Flaecheninhalt eines Rechecks ausgibt.

class Rechteck:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def umfang(self):
        return self.a * 2 + self.b * 2

    def flaeche(self):
        # Hier bitte Deine Loesung einfuegen
        return 0


a = int(raw_input("Laenge Seite a:"))
b = int(raw_input("Laenge Seite b:"))
r = Rechteck(a,b)
print "Umfang: " + str(r.umfang())
print "Flaeche: " + str(r.flaeche())

