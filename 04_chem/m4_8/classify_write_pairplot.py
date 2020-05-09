"""
SBSで調べたcolumnsを利用してpairplotのグラフを描画する
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from classify_dataprepare import drop_from_std


def search_0_1(df):
    """
    unique数が10以下のcolumnsを調べる
    :param df:
    :return:
    """
    print(df.astype("str").describe())
    df_desc = df.astype("str").describe()
    df_sample = df_desc.loc[: , df_desc.loc["unique"] < 10]
    print(df_sample)


if __name__ == '__main__':

    df = pd.read_csv("data/classify/2d_param_classify.csv")
    print(df.shape)
    df = drop_from_std(df)
    print(df.shape)

    search_0_1(df)

    #SBSを利用して抽出したカラム（あまり良くない）

    label = ['MinEStateIndex', 'MolWt', 'ExactMolWt', 'NumValenceElectrons',
     'MinPartialCharge', 'Chi0n', 'PEOE_VSA14', 'SlogP_VSA7',
     'fr_aryl_methyl', 'fr_sulfide', 'compare']
    #

    # label = ['MaxEStateIndex', 'MinEStateIndex', 'MaxAbsEStateIndex', 'qed', 'MolWt',
    #  'HeavyAtomMolWt', 'ExactMolWt', 'NumValenceElectrons',
    #  'NumRadicalElectrons', 'MaxPartialCharge', 'MinPartialCharge',
    #  'MaxAbsPartialCharge', 'MinAbsPartialCharge', 'FpDensityMorgan1',
    #  'FpDensityMorgan2', 'BertzCT', 'Chi0', 'Chi0n', 'Chi0v', 'Chi1',
    #  'Chi1n', 'Chi1v', 'Chi2n', 'PEOE_VSA10', 'compare']

    label = ['MaxEStateIndex', 'MinEStateIndex', 'MaxAbsEStateIndex', 'MolWt',
    'HeavyAtomMolWt', 'ExactMolWt', 'NumValenceElectrons',
    'NumRadicalElectrons', 'MaxPartialCharge', 'MinPartialCharge',
    'MaxAbsPartialCharge', 'MinAbsPartialCharge', 'FpDensityMorgan1',
    'FpDensityMorgan2', 'FpDensityMorgan3', 'BalabanJ', 'BertzCT', 'Chi0',
    'Chi0v', 'Kappa2', 'Kappa3', 'PEOE_VSA1', 'PEOE_VSA10', 'PEOE_VSA11', 'compare']

    sns.pairplot(df[label], hue="compare")
    plt.tight_layout()
    plt.savefig("data/classify/pairplot.png")
    plt.show()
    #

