from enum import Enum
class PokeType(Enum):
    AQUA=0
    FIRE=1
    GRASS=2
    def __eq__(self, other):
        return True if  self.name == other.name else False
    def __ne__(self,other):
        return True if self.name != other.name else False
    def __lt__(self, other):
        if self.name==other.name:
            return False
        if self.name=="Grass" and other.name=="Fire":
            return True
        elif self.name=="Grass" and other.name=="Aqua":
            return False
        elif self.name=="Aqua" and other.name=="Grass":
            return True
        elif self.name=="Aqua" and other.name=="Fire":
            return False
        elif self.name=="Fire" and other.name=="Aqua":
            return True
        elif self.name=="Fire" and other.name=="Grass":
            return False
    def __gt__(self, other):
        return self.__lt__(other)