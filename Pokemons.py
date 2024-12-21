class Pokemon:
    def __init__(self,Name,Lvl,Atk,Def,Spatk,Spdef):
        self.Level = Lvl
        self.Atk = Atk
        self.defense = Def
        self.Spatk = Spatk
        self.Spdef = Spdef
        self.Name = Name
    def StatChange(self,num,stat):
        StageList = [2/8,2/7,2/6,2/5,2/4,2/3,2/2,3/2,4/2,5/2,6/2,7/2,8/2]
        mult = StageList[6+num]
        if stat == 'Atk':
            self.Atk = self.Atk*mult
        if stat == 'Def':
            self.defense = self.defense*mult
        if stat == 'Spatk':
            self.Spatk = self.Spatk*mult
        if stat == 'Spdef':
            self.Spdef = self.Spdef*mult
        return self
    def __repr__(self):
        return f"{self.Name} (Lvl: {self.Level}, Atk: {self.Atk}, Def: {self.defense}, SpAtk: {self.Spatk}, SpDef: {self.Spdef})"