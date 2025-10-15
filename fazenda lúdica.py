class Animal:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = int(idade)

    def emitir_som(self):
        return "O animal emite um som."

    def apresentar(self):
        return f"Olá, sou {self.nome} e tenho {self.idade} anos."


class Cachorro(Animal):
    def __init__(self, nome: str, idade: int, raca: str):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "Au! Au!"


class Gato(Animal):
    def __init__(self, nome: str, idade: int, cor_pelo: str):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"


class Vaca(Animal):
    def __init__(self, nome: str, idade: int, producao_leite_litros: float):
        super().__init__(nome, idade)
        self.__producao_leite_litros = float(producao_leite_litros)

    def emitir_som(self):
        return "Muuu!"

    def obter_producao_leite(self):
        return self.__producao_leite_litros

    def registrar_ordenha(self, litros):
        try:
            litros = float(litros)
        except (TypeError, ValueError):
            raise ValueError("Litros deve ser um número (int ou float).")
        self.__producao_leite_litros = litros


class Fazenda:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def fazer_sons(self):
        for animal in self.animais:
            print(f"{animal.apresentar()} -> {animal.emitir_som()}")


if __name__ == "__main__":
    fazenda = Fazenda()

    cachorro = Cachorro("Rex", 5, "Vira-lata")
    gato = Gato("Mimi", 3, "Preto")
    vaca = Vaca("Mimosa", 4, 12.5)

    fazenda.adicionar_animal(cachorro)
    fazenda.adicionar_animal(gato)
    fazenda.adicionar_animal(vaca)

    fazenda.fazer_sons()

    print(f"Produção inicial de leite da {vaca.nome}: {vaca.obter_producao_leite()} litros")
    vaca.registrar_ordenha(15.2)
    print(f"Produção após ordenha: {vaca.obter_producao_leite()} litros")