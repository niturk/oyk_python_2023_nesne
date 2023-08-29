class Hayvan:
    ad = ""

    def adin_ne(self):
        print("Hayvanın adı bilinmiyor.")

    def konus(self):
        adi = self.ad
        print(f"{adi} konuşuyor.")

    def oyna(self, arkadas):
        print(f"{self.ad},{arkadas.ad} ile oynuyor")

    def oyuncakla_oyna(self, oyuncak):
        print(f"{self.ad}, {oyuncak} ile oynuyor.")


rodi = Hayvan()
rodi.ad = "Rodi"
maya = Hayvan()
maya.ad = "Maya"

# Hayvan.konus(rodi)
rodi.konus()
maya.konus()


# rodi.oyna = lambda arkadas: print(f"Rodi, {arkadas.ad} ile oynuyor.")
rodi.oyna(maya)  # Rodi, Maya ile oynuyor.

maya.oyna(rodi)


oyuncak = "ayicik"

rodi.oyuncakla_oyna(oyuncak)  # Rodi, top ile oynuyor.
maya.oyuncakla_oyna(oyuncak)  # Maya, top ile oynuyor.

# Hayvan.oyuncakla_oyna(rodi, oyuncak)
