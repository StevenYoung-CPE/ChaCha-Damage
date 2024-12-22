from tkinter import *
import tkinter as tk
from tkinter import messagebox, simpledialog
from Pokemons import Pokemon

def pfinder(Pokedex,name):
    for poke in Pokedex:
        if poke.Name == name:
            return poke
with open('Pokemon List.txt', 'r') as PL:
    Plist = []
    for line in PL:
        mon = line.strip().split()
        name, lvl, atk, defense, spatk, spdef = mon
        Plist.append(Pokemon(name, int(lvl), int(atk), int(defense), int(spatk), int(spdef)))
with open('Relevant Mons.txt', 'r') as Pokedex:
    Rlist = []
    for line in Pokedex:
        mon = line.strip()
        Rlist.append(mon)

def exit():
    root.destroy()
def create_menu():
    global root
    root = tk.Tk()
    root.title('ChaCha Damage Sim')
    root.geometry('450x370')
   
    Samon = StringVar(root)
    Samon.set(Rlist[0])
    Sdmon = StringVar(root)
    Sdmon.set(Rlist[0])
    
    BP = IntVar(root)
    BP.set(1)
    SB = StringVar(root)
    SB.set(1)
    Misc = StringVar(root)
    Misc.set(1)
    Crit = IntVar(root)
    Crit.set(0)
    Eff = StringVar(root)
    Eff.set(1)
    Stages = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
    Stagea = IntVar()
    Stagea.set(Stages[6])
    Staged = IntVar()
    Staged.set(Stages[6])
    PS = StringVar()
    PS.set('Physical')
    def damage():
        if Crit.get() == 0:
            Tcrit = 1
        if Crit.get() == 1:
            Tcrit = 1.5
        Atker = Samon.get()
        Dfer = Sdmon.get()
        Atker = pfinder(Plist,Atker)
        Dfer = pfinder(Plist,Dfer)
        if PS.get() == 'Physical':
            Atker.StatChange(Stagea.get(),'Atk')
            Dfer.StatChange(Staged.get(),'Def')
            print(Misc.get())
            Damage = (10*Atker.Level+10)/250*Atker.Atk/Dfer.defense*BP.get()*float(SB.get())*float(Eff.get())*float(Misc.get())*Tcrit
            messagebox.showinfo("Damage Report",(f'{Dfer.Name} takes {Damage}'))
            Atker.StatChange(-1*Stagea.get(),'Atk')
            Dfer.StatChange(-1*Staged.get(),'Def')
            print(Atker.Atk)
        if PS.get() == 'Special':
            Atker.StatChange(Stagea.get(),'Spatk')
            Dfer.StatChange(Staged.get(),'Spdef')
            Damage = (10*Atker.Level+10)/250*Atker.Spatk/Dfer.Spdef*BP.get()*float(SB.get())*float(Eff.get())*float(Misc.get())*Tcrit
            messagebox.showinfo("Damage Report",(f'{Dfer.Name} takes {Damage}'))
            Atker.StatChange(-1*Stagea.get(),'Spatk')
            Dfer.StatChange(-1*Staged.get(),'Spdef')

    title_label = tk.Label(root, text = "ChaCha Damage Sim", font=("Impact",16))

    Attacker_label = tk.Label(root, text="Attacker", font=("Arial",10))

    Defender_label = tk.Label(root, text="Defender", font=("Arial",10))

    Stab_label = tk.Label(root, text="Stab Mult", font=("Arial",10))

    DamageRoll_label = tk.Label(root, text="Damage Roll?", font=("Arial",10))

    Miscil_label = tk.Label(root, text="Misc Mult", font=("Arial",10))

    Statchangea_label = tk.Label(root, text="+/- Offensive Stage", font=("Arial",10))
    
    Statchanged_label = tk.Label(root, text="+/- Defensive Stage", font=("Arial",10))

    Eff_label = tk.Label(root,text='Type Effectiveness Mult?',font=("Arial",10))

    paselect = OptionMenu(root,Samon,*Rlist)

    pdselect = OptionMenu(root,Sdmon,*Rlist)
    

    Critter = tk.Checkbutton(root,text='Crit?',variable=Crit)
    
    
    DamageRoll = tk.Entry(root,textvariable = BP,font = ('impact',10))

    
    Stab = tk.Entry(root,textvariable = SB,font = ('Impact',10))

    
    Miscil = tk.Entry(root,textvariable = Misc,font =('Impact',10))

    
    Effective = tk.Entry(root,textvariable = Eff,font =('Impact',10))

    exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=exit)

    P = Radiobutton(root,text="Physical",variable = PS,value='Physical')
    
    S= Radiobutton(root,text=" Special",variable = PS, value='Special')

    Statchangea = OptionMenu(root,Stagea,*Stages)

    StatChanged = OptionMenu(root,Staged,*Stages)
     
    Damage_Button = tk.Button(root,text="Damage",font=("Arial",12), command=damage)

    Attacker_label.grid(column=0,row=1)
    paselect.grid(column=0,row=2)
    Statchangea_label.grid(column=0,row=3)
    Statchangea.grid(column=0,row=4)
    DamageRoll_label.grid(column=0,row=6)
    DamageRoll.grid(column=0,row=7)
    Stab_label.grid(column=0,row=8)
    Stab.grid(column=0,row=9)
    Eff_label.grid(column=0,row=10)
    Effective.grid(column=0,row=11)
    Miscil_label.grid(column=0,row=12)
    Miscil.grid(column=0,row=13)

    title_label.grid(column=1,row=0)
    Critter.grid(column=1,row=12)
    P.grid(column=1,row=10)
    S.grid(column=1,row=11)
    Damage_Button.grid(column=1,row=6)
    exit_button.grid(column=1,row=15)

    Defender_label.grid(column=2,row=1)
    pdselect.grid(column=2,row=2)
    Statchanged_label.grid(column=2,row=3)
    StatChanged.grid(column=2,row=4)

    root.mainloop()
   
if __name__ == "__main__":
    create_menu()