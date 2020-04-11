from pymol import cmd, launch
import numpy as np


def calc_gc(filename, select):
    # IUPAC definition
    cmd.load(filename)
    cmd.hide('everything')

    model = cmd.get_model(select).atom
    center = np.array(cmd.centerofmass(select))

    pos = np.array([atom.coord for atom in model])
    pos_c = np.square(pos - center) # 重心からの座標
    pos_c_m = np.sum(pos_c, axis=1)  # x^2 + y^2 + z^2

    mass = np.array([atom.get_mass() for atom in model])
    upper = mass * pos_c_m

    total_upper = np.sum(upper)
    total_mass = np.sum(mass)

    return np.sqrt(total_upper/ total_mass)


# if __name__ == '__main__':
print(calc_gc("data/1buw.pdb", "chain A"))
