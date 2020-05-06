"""
予測の良い化合物と悪い化合物をそれぞれ10個ずつ描画する
"""
import sys

sys.path.append("../")
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw


def imgs_from_smiles(df, save_path="result/test.png"):
    mols= [Chem.MolFromSmiles(smiles) for smiles in df["SMILES"]]
    img = Draw.MolsToGridImage(mols)
    img.save(save_path)
    return img


if __name__ == '__main__':
    df = pd.read_csv("result/diff_sorted_test.csv")
    imgs_from_smiles(df.head(10), "result/diff_test/4_8_good.png")
    imgs_from_smiles(df.tail(10), "result/diff_test/4_8_bad.png")




