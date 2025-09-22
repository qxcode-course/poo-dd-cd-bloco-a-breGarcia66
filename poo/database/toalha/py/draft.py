print('Minha toalha é do Roblox :)')

#Criando toalha

class Towel:
    def __init__ (self, color: str, size: str): #consturctor
        self.color = "red with white" #atribute
        self.size = "M"               #atribute
        self.witness = 0              #atribute

    def getMaxWetness (self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30

    def __str__ (self) -> str:
        return f"Cor: {self.color}\nTam: {self.size}\nUmi: {self.witness}"

#reference
towel = Towel("green", "G") #object 
towel2 = Towel("Red", "M")  #object
extraTowel = towel2
superExtraTowel = towel2


# print(towel.color)
# towel.color = "white"toalha
# print(towel.size)
# print(towel.witness)

print(towel)