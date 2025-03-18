import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type.upper()
        self.alleles = self.get_alleles()

    def get_alleles(self):
        if self.blood_type == "A":
            return ["A", random.choice(["A", "O"])]
        elif self.blood_type == "B":
            return ["B", random.choice(["B", "O"])]
        elif self.blood_type == "AB":
            return ["A", "B"]
        elif self.blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah tidak valid")

class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type.upper()
        self.alleles = self.get_alleles()

    def get_alleles(self):
        if self.blood_type == "A":
            return ["A", random.choice(["A", "O"])]
        elif self.blood_type == "B":
            return ["B", random.choice(["B", "O"])]
        elif self.blood_type == "AB":
            return ["A", "B"]
        elif self.blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah tidak valid")

class Child:
    def __init__(self, father, mother):
        self.father_allele = random.choice(father.alleles)
        self.mother_allele = random.choice(mother.alleles)
        self.blood_type = self.determine_blood_type()

    def determine_blood_type(self):
        alleles = sorted([self.father_allele, self.mother_allele])
        if alleles == ["A", "A"] or alleles == ["A", "O"]:
            return "A"
        elif alleles == ["B", "B"] or alleles == ["B", "O"]:
            return "B"
        elif alleles == ["A", "B"]:
            return "AB"
        elif alleles == ["O", "O"]:
            return "O"

father_blood = input("Masukkan golongan darah ayah (A, B, AB, O): ")
mother_blood = input("Masukkan golongan darah ibu (A, B, AB, O): ")

father = Father(father_blood)
mother = Mother(mother_blood)

child = Child(father, mother)

print(f"Golongan darah anak: {child.blood_type}")
