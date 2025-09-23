class Towel:
  def __init__ (self, color: str, size: str) -> None:
    self.color: str   = color;
    self.size: str    = size;
    self.wetness: int = 0;

  def __str__(self) -> str:
    return f"Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}";

  def show (self) -> None:
    print(self);

  def getMaxWetness (self) -> int:
    if self.size == "P":
      return 10;
  
    if self.size == "M":
      return 20;
  
    if self.size == "G":
      return 30
    
    return 0;

  def dry (self, amount: int) -> None:
    self.wetness += amount;

    if self.wetness >= self.getMaxWetness():
      print('toalha encharcada');
      self.wetness = self.getMaxWetness();

  def isDry (self) -> bool:
    return self.wetness == 0;

  def wringOut (self) -> None:
    self.wetness = 0;

# --------------------------------------------------------------------------------- #

def main () -> None:
  towel: Towel = Towel("", "");
  
  while True:
    line: str = input();
    args: list[str] = line.split(" ");

    if args[0] == "end":
      print(f"${line}");
      break;
    
    elif args[0] == "criar":
      print(f"${line}");
      towel.color = args[1];
      towel.size  = args[2];

    elif args[0] == "seca":
      print(f"${line}");
      print("sim" if towel.isDry() else "nao");
    
    elif args[0] == "enxugar":
      print(f"${line}");
      towel.dry(int(args[1]));
    
    elif args[0] == "torcer":
      print(f"${line}");
      towel.wringOut();
    
    elif  args[0] == "mostrar":
      print(f"${line}");
      towel.show();

    else:
      print(f"${line}");
      print(f"Erro: \"{line}\" não encontrado");

main();