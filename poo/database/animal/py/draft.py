# Criando classe Animal

class Animal: 
  def __init__ (self, species: str, sound: str) -> None:
    self.species: str = species;
    self.sound:   str = sound;
    self.age = 0;

  def __str__ (self) -> str:
    return f"{self.species}:{self.age}:{self.sound}";

  def makeSound (self) -> str:
    match self.age:
      case 0:
        return "---";
      
      case 4:
        return "RIP";
      
      case _:
        return self.sound;

  def ageBy(self, increment: int) -> None:
    self.age += increment;

    if self.age >= 4:
      print(f"warning: {self.species} morreu");
      self.age = 4;

# Criando método main ()

# Comando para serem implementados:
  #  init {animal} {som}  - feito
	# 	- Criar um animal

	# show  -feito
	# 	- Mostrar dados do animal
	
  # grow {somar estágio}
	# 	- Aumentar estágio da vida
	
  # noise
	# 	- Fazer barulho do animal

def main () -> None:
  animal: Animal = Animal("", "");
  while True:
    line: str = input();
    args: list[str] = line.split(" ");

    print(f"${line}");
    
    match args[0]:
      case "end":
        if len(args) == 1:
          break;
        
        elif len(args) != 1:
          print("Erro: comando \"end\" não precisa de argumentos");

      case "init":
        if len(args) == 3:
          animal.species = args[1];
          animal.sound   = args[2];
          animal.age     = 0;

        elif len(args) != 3:
          print("Erro: comando \"init\" necessita de, somente, dois parâmetros \"init {spécie} {som}\"");

      case "show":
        if len(args) == 1:
          print(animal);

        elif len(args) != 1:
          print("Erro: comando \"show\" não precisa de argumentos");
      
      case "grow":
        if len(args) == 2:
          animal.ageBy(int(args[1]));
        
        elif len(args) != 2:
          print("Erro: comando \"grow\" necessita de, somente, um parâmetro \"grow {valor}\"");
      
      case "noise":
        if len(args) == 1:
          print(animal.makeSound());
      
        elif len(args) != 1:
          print("Erro: comando \"noise\" não precisa de argumentos");

      case _:
        print(f"Erro: {args[0]} não encontrado");

main();