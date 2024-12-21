import random
from Pokemons import Pokemon
# Pokemon are defined by Pokemon(Lvl,Atk,Def,Spatk,Spdef), For sure for sure
with open('Pokemon List.txt','r') as PL:
    print(PL.read())
    for line in PL:
        mon = PL.readline()
        mon = mon.split(' ')
        print(mon)

def damage(Lvl,atk,Def,dice,sb,eff,crit,misc):
    #Currently built to autoroll dice, just input the number of dice that should be rolled
    #Sb stands for stab, Use 1 for non stab, 1.2 for stab, and 2 for adaptability
    #Crit is a binary, 'y' for crit occured.
    x = 0
    if crit == 'y':
        for i in range(2*dice):
            x = x + random.randint(1,8)
            print(x)
    else:
        for i in range(dice):
            x = x + random.randint(1,8)
            print(x)
    return ((10*Lvl+10)/250*atk/Def*x)*sb*eff*misc
#print(damage(1,1,1,5,1.5,1,1,'n'))
def main():
    battle = 0
    while battle == 0:
        Atker = input('Who is attacking?')
        PS = input('Physical Or Special (P/S)') #Respond with p or s
        if PS == 'p':
            pass