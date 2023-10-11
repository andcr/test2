class Kitob:
    def __init__(self, muallif, nomi):
        self.muallif = muallif
        self.nomi = nomi

    def get_muallif(self):
        return self.muallif

    def get_nomi(self):
        return self.nomi

    def __str__(self):
        return f"{self.muallif}, {self.nomi}"


class Kitobhona:
    def __init__(self):
        self.qavatlar = {}

    def add(self,    qavat, shkaf, javon, kitob):
        if qavat not in self.qavatlar:
            self.qavatlar[qavat] = {}
        if shkaf not in self.qavatlar[qavat]:
            self.qavatlar[qavat][shkaf] = {}
        if javon not in self.qavatlar[qavat][shkaf]:
            self.qavatlar[qavat][shkaf][javon] = []
        self.qavatlar[qavat][shkaf][javon].append(kitob)

    def contains(self, qavat, shkaf, javon, kitob):
        if qavat in self.qavatlar and shkaf in self.qavatlar[qavat] and javon in self.qavatlar[qavat][shkaf]:
            return kitob in self.qavatlar[qavat][shkaf][javon]
        return False

    def get_books(self, qavat, shkaf):
        if qavat in self.qavatlar and shkaf in self.qavatlar[qavat]:
            result = []
            for javon, kitoblar in self.qavatlar[qavat][shkaf].items():
                result.append(f"Javon {javon}")
                for kitob in kitoblar:
                    result.append(str(kitob))
            return "\n".join(result)
        return "Shkaf topilmadi"


# Test qismi
kitob1 = Kitob("Muallif1", "Nomi1")
kitob2 = Kitob("Muallif2", "Nomi2")

kutubhona = Kitobhona()
kutubhona.add("Qavat1", "Shkaf1", "Javon1", kitob1)
kutubhona.add("Qavat1", "Shkaf1", "Javon1", kitob2)

print(kutubhona.contains("Qavat1", "Shkaf1", "Javon1", kitob1))  # True
print(kutubhona.contains("Qavat1", "Shkaf1", "Javon2", kitob1))  # False

print(kutubhona.get_books("Qavat1", "Shkaf1"))
print(kutubhona)
