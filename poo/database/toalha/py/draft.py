# Configurando obejto Towel

class Towel:
    def __init__(self, size: str, color: str) -> None:
        self.size: str = size.upper();
        self.color: str = color;
        self.wetness: int = 0;

    def __str__(self) -> str:
        return f"color: {self.color}, size: {self.size}, wetness: {self.wetness}";

    def getMaxWetness (self) -> int:
        if self.size == "P":
            return 10;
        if self.size == "M":
            return 20;
        if self.size == "G":
            return 30;
        return 0

    def dry (self, amount: int) -> None:
        self.wetness += amount;
        if self.wetness >= self.getMaxWetness():
            print('A toalha está encharcada');
            self.wetness = self.getMaxWetness();

    def isDry (self) -> bool:
        return self.wetness == 0;

    def wringOut (self) -> None:
        self.wetness = 0;

    def show (self):
        print(self);

# Contruindo função Main()

def main ():
    towel: Towel = Towel("", "");

    while True:
        line = input();
        args: list[str] = line.split(" ");
        
        if args[0] == "quit":
            break;
        
        elif args[0] == "new":
            print(f"${line}");
            towel.color = args[1];
            towel.size = args[2];

        elif args[0] == "dry":
            print(f"${line}");
            towel.dry(int(args[1]));
        
        elif args[0] == "isDry":
            print(f"${line}");
            print(towel.isDry());
        
        elif args[0] == "show":
            print(f"${line}");
            towel.show();
        
        elif args[0] == "wringOut":
            print(f"${line}");
            towel.wringOut();

        else:
            print(f"${line}");
            print(f"Error: \"{args[0]}\" não encontrado");

main();