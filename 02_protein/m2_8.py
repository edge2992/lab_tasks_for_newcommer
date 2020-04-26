from pymol import cmd
from m2_7 import calc_gc
filename = "data/1buw.pdb"
cmd.load(filename)
cmd.hide("everything")
c = cmd.centerofmass("chain A")
cmd.origin(position=c)
cmd.center('origin')
print(cmd.get_position())
cmd.select("inside", "chain A within {:.2f} of origin".format(calc_gc(filename, "chain A")))
cmd.select("outside", "not inside")

cmd.color("red", "inside")
cmd.color("blue", "outside")

cmd.show("sphere", "inside")
cmd.show("sphere", "outside")


