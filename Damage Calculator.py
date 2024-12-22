import random
import tkinter as tk
from tkinter import *
from Pokemons import Pokemon
# Pokemon are defined by Pokemon(Lvl,Atk,Def,Spatk,Spdef)
with open('Pokemon List.txt', 'r') as PL:
    Plist = []
    for line in PL:
        mon = line.strip().split()
        name, lvl, atk, defense, spatk, spdef = mon
        Plist.append(Pokemon(name, int(lvl), int(atk), int(defense), int(spatk), int(spdef)))   
def pfinder(Pokedex,name):
    for poke in Pokedex:
        if poke.Name == name:
            return poke
    return None
def damage(Lvl,atk,Def,dice,sb,eff,crit,misc):
    #Currently built to autoroll dice, just input the number of dice that should be rolled
    #Sb stands for stab, Use 1 for non stab, 1.2 for stab, and 2 for adaptability
    #Crit is a binary, 'y' for crit occured.
    dice = int(dice/5)
    x = 0
    if crit == 'y':
        for i in range(2*dice):
            x = x + random.randint(1,8)
    else:
        for i in range(dice):
            x = x + random.randint(1,8)
    print(x)
    return ((10*Lvl+10)/250*atk/Def*x)*sb*eff*misc
def main():
        '''Userinput = input('Attacker, Attack stages, P/S, Defender, Defense Stages, BP, Stab, Type effectiveness, Misc Mult, Crit: ')
        Inlist = Userinput.split(',')
        Atker, AtkUp, PS, Defer, Defup, BP, SB, Eff, misc, Cr = Inlist'''
        Atker = input("Who attack? ")
        AtkUp = input('(-6 to 6)')
        PS = input('Physical or Special (p,s)').lower()
        Defer = input('Who Def? ')
        Defup = input("-6 to 6")
        BP = input('Move Basepower? ')
        SB = input("stab multiplier (1, 1.5, etc)")
        Eff = input("type multiplier?")
        misc = input('Additional multipliers')
        Cr = input ('crit? (y,n)').lower()
        Atker = pfinder(Plist,Atker)
        Defer = pfinder(Plist,Defer)
        if PS.lower() == 'p':
            Atker.StatChange(int(AtkUp),'Atk')
            Defer.StatChange(int(Defup),'Def')
            print(damage(Atker.Level,Atker.Atk,Defer.defense,int(BP),float(SB),int(Eff),Cr,float(misc)))
        if PS.lower() == 's':
            Atker.StatChange(int(AtkUp),'Spatk')
            Defer.StatChange(int(Defup),'Spdef')
            print(damage(Atker.Level,Atker.Spatk,Defer.Spdef,BP,SB,Eff,Cr,misc))
main()