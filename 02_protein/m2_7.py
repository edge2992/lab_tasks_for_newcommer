from pymol import cmd, launch
import numpy as np


def calc_gc(filename, select):
    # IUPAC definition
    cmd.load(filename)
    cmd.hide('everything')

    model = cmd.get_model(select).atom
    center = np.array(cmd.centerofmass(select))

    pos = np.array([atom.coord for atom in model])
    pos_c_m = np.linalg.norm(pos - center, axis=1)

    mass = np.array([atom.get_mass() for atom in model])
    upper = mass * np.square(pos_c_m)    # m * r^2

    total_upper = np.sum(upper)
    total_mass = np.sum(mass)

    return np.sqrt(total_upper/ total_mass)


# if __name__ == '__main__':
print(calc_gc("data/1buw.pdb", "chain A"))
