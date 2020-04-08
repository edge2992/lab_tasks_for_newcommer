# m4_6以降のために作成
# 評価用の関数

import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def calc_rmse(y_true,y_pred):
    """
    RMSEを計算する
    :param y_true:
    :param y_pred:
    :return:
    """
    rmse = np.sqrt(mean_squared_error(y_true,y_pred))
    return rmse


def calc_score(y_true, y_pred):
    q2_score = r2_score(y_true, y_pred)
    rmse_score = calc_rmse(y_true, y_pred)

    print('best rmse: {:.5f}'.format(rmse_score))
    print('q2: {:.5f}'.format(q2_score))


def show_graph(y_true, y_pred):
    plt.figure(figsize=(20,10))
    plt.plot(y_true.values,label="True")
    plt.plot(y_pred, label="predicted")
    plt.legend()


def regression(model, x, y, graph=False):
    """
    回帰モデルの比較をするための巻数
    :param model:
    :param x:
    :param y:
    :param graph: グラフを出力するかどうか
    :return:
    """
    # TODO:  評価をするときは交差検証をするべき
    X_train, X_test, Y_train, Y_test = train_test_split(x, y)
    model.fit(X_train, Y_train)
    y_pred = model.predict(X_test)

    calc_score(Y_test, y_pred)
    if graph:
        show_graph(Y_test, y_pred)

    return model