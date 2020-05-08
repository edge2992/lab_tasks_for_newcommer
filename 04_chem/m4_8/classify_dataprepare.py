"""
pred > true  　
pred = true
pred < true
の三種類でラベルをつけて、何が要因となってうまく予測できていないかを確認する

ここではデータの準備をしてdata/classifyに保存する
メモ：P_appは透過係数
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import lightgbm as lgb

from m4_8_prepare import get_sorted_diff
from m4_8_graph import compare_with_graph
from regression import prepare_dataset, calc_score


def get_params(df):
    """
    予測値のインデックスから二次元の記述子を取得する
    :param df:
    :return:
    """
    df_param = pd.read_csv("../data/2d_desc.csv", index_col="index")

    df_s = pd.concat([df["compare"], df_param], join="inner", axis=1)
    return df_s.drop("Unnamed: 0", axis=1)


def split_3type(df, threshold=0.5):
    """
    測定値より高いものと低いものに分ける
    :param df:
    :param threshold:
    :return:
    """
    df.loc[df["Log_app(pred)"] - df["Log_app(true)"] > threshold, "compare"] = "pred>exp"
    df.loc[df["Log_app(true)"] - df["Log_app(pred)"] > threshold, "compare"] = "exp>pred"
    df["compare"].fillna("pred=exp", inplace=True)
    print(df["compare"].value_counts())
    return df


def train_and_test(test_ratio=0.2):
    """
    予測と実験値の差を並べ替えてアッセイIDなどといっしょにまとめたものをCSVに保存する
    :param test_ratio:
    :return:
    """
    best_param = {'learning_rate': 0.05, 'max_depth': 25, 'n_estimators': 200, 'num_leaves': 100}

    X, Y = prepare_dataset("../data/2d_desc.csv", "../data/fukunishi_data.csv")
    X = pd.DataFrame(X)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_ratio, shuffle=True)

    # モデルを学習させる
    pipe_model = make_pipeline(StandardScaler(), lgb.LGBMRegressor(**best_param))
    pipe_model.fit(X_train, Y_train)
    y_pred = pipe_model.predict(X_test)
    print(calc_score(Y_test, y_pred))

    # 予測値と測定値の差の絶対値で並び替え
    df_diff = get_sorted_diff(Y_test, y_pred, X_test)
    df_diff.to_csv("data/classify/diff_sorted_test" + str(test_ratio) + ".csv")
    return df_diff


def load_classify_datasets():
    """
    クラス分類用のデータセットをロードする
    :return:
    """
    df = pd.read_csv("data/classify/2d_param_classify.csv")
    df = drop_from_std(df)
    print(df.shape)

    X = df.drop(["compare", df.columns[0]], axis=1)
    y = df["compare"]
    return X, y


def drop_from_std(df):
    """
    標準偏差が0のものを外す
    :param df:
    :return:
    """
    df_desc = df.describe()
    # print(df_desc.loc["std"] == 0)
    df_zero = df_desc.loc[:, df_desc.loc["std"] == 0]
    drop_list = list(df_zero.columns)
    df = df.drop(drop_list, axis=1)
    return df


if __name__ == '__main__':
    """
    アッセイIDによって色分けされたグラフと
    予測の上、真ん中、下で色分けされたグラフを描画する
    
    その後、クラス分類用にラベル付されたデータをCSVに保存する
    """
    df = train_and_test(0.4)
    print(df.shape)

    # df = pd.read_csv("../result/diff_sorted_test.csv", index_col=0)
    df = split_3type(df)

    # グラフを書く
    compare_with_graph(df, split="compare", file_dir="data/classify/")
    compare_with_graph(df, file_dir="data/classify/")

    df_param = get_params(df)
    df_param.to_csv("data/classify/2d_param_classify.csv")
