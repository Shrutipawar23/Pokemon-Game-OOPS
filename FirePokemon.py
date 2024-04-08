from data_models.Pokemon import Pokemon
class Firepokemon(Pokemon):
    def __init__(self,name,pokedexId,level,living_points,attacking_points,defense_points,attack):
        super().__init__(name,pokedexId,level,living_points,attacking_points,defense_points,attack)
        self.type: Poketype = Poketype(1)

    def lvlUp(self)->Pokemon:
        pass