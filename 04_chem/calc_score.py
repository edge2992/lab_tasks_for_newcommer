# m4_6以降のために作成
# 評価用の関数

import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, KFold


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


def regression(model, x, y, graph=True, score=False):
    """

    :param model:
    :param x:
    :param y:
    :param graph: グラフを出力するかどうか
    :return:
    """
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, shuffle=True)
    model.fit(X_train, Y_train)
    y_pred = model.predict(X_test)
    if score:
        calc_score(Y_test, y_pred)
    if graph:
        show_graph(Y_test, y_pred)

    return model


def cv_regression(model, x, y):
    kf = KFold(n_splits=4, shuffle=True, random_state=10)

    rse = cross_val_score(model, x, y, scoring='neg_mean_squared_error', cv=kf)
    r2 = cross_val_score(model, x, y, scoring='r2', cv=kf)

    rmse = np.sqrt(np.abs(rse))

    print(rmse)
    print(r2)

    print('mean rmse: {:.5f}'.format(np.mean(rmse)))
    print('mean r2: {:.5f}'.format(np.mean(r2)))
