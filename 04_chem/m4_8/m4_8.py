"""
4_7~ 4_8までの結果で最も良かったのは2D記述子によって学習させたLightBGMで
ハイパーパラメーターは
{'learning_rate': 0.05, 'max_depth': 25, 'n_estimators': 200, 'num_leaves': 100}
であった

結果について考察をする
1.LogP_appについて予測があたっていたものと外れていたものについて比べるために
差の絶対値を取って並び替えるー＞result/diff_sorted_test.csv

2.良いものと悪いものについて出処に差があったかを調べる

3.化合物を記述してみて見た目でなにか違いがあるかを調べる
　なさそう

"""
import sys
sys.path.append("../")

from sklearn.model_selection import train_test_split
import pandas as pd
import lightgbm as lgb
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
from m4_6.regression import prepare_dataset


def get_sorted_diff(y_true, y_pred, x_test):
    df_ex = pd.read_csv("data/fukunishi_data.csv")
    y_diff = [abs(y_p - y_t) for y_p, y_t in zip(y_pred, y_true)]
    ar = np.array([y_diff, y_pred, y_true]).T

    df_diff = pd.DataFrame(ar, index=x_test.index, columns=["diff", "Log_app(pred)", "Log_app(true)"])
    df_diff = pd.concat([df_diff, df_ex[["Assay ID", "SMILES"]]], join="inner", axis=1)
    df_s = df_diff.sort_values('diff')
    return df_s


def count_assayID(df, num=50):
    print("all")
    print(df['Assay ID'].value_counts())
    good_one = df.head(num)['Assay ID']
    print("good_one")
    print(good_one.value_counts())
    bad_one = df.tail(num)['Assay ID']
    print("bad_one")
    print(bad_one.value_counts())


if __name__ == '__main__':
    best_param = {'learning_rate': 0.05, 'max_depth': 25, 'n_estimators': 200, 'num_leaves': 100}

    X, Y = prepare_dataset("data/2d_desc.csv", "data/fukunishi_data.csv")
    X = pd.DataFrame(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, shuffle=True)

    # モデルを学習させる
    pipe_model = make_pipeline(StandardScaler(), lgb.LGBMRegressor(**best_param))
    pipe_model.fit(X_train, Y_train)
    y_pred = pipe_model.predict(X_test)

    # 予測値と測定値の差の絶対値で並び替え
    df_diff = get_sorted_diff(Y_test, y_pred, X_test)

    print(df_diff.head())
    count_assayID(df_diff, 25)

    df_diff.to_csv("result/diff_sorted_test.csv")
