Welcome to the Chambers And Charizards Damage Simulator!
This doccument will outline the infrastructure that the program uses, and help clarify how it is intended to be used

Pokemon List is a text File that contains the information needed to run the damage calculation for all pokemon in your campaign (you will need to input this)

The formating is Name LVL ATK DEF SPATK SPDEF. This information must be sepperated by spaces, and must be in this order, with no other text (The name can contain no spaces)

EX: My characters Bisharp is level 9 with 128 atk, 113 def, 69 spatk, 76 spdef. You could represent this with: Allen_Bisharp 9 128 113 69 76

Note that the stats are the raw stats, not the base stats

The Relevent Mons text file exists to cut down on bloat in the drop down menu. It contains only name information of pokemon who's information you would like to use

Relevent mons names must identically match the names of pokemon in the Pokemon List

If changes are made to the Relevent Mons text file, the menu must be reloaded for the changes to appear

The Relevent Mons list will appear sorted by ASCII number in the drop down menu. Be consistent with Capitalization, or else the sorting will appear weird.

**Factors not natively supported:**

Changes to Crit mult (Don't check crit, put correct mult in Misc Mult)

Crits piercing through defensive stat changes (simply set defensive stage to 0 when crits occur)

Moves like Psyshock (Create a sepperate pokemon with flipped attacking stats)

Any abilities which alter damage (should be contained within misc mult)

If, after understanding the above, you encounter a bug or have a simple feature you would like to see, you can dm me on discord
@failureincarnate
