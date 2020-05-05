"""
次元を削減して組み合わせる
"""
from functools import partial

import optuna
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import lightgbm as lgb
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

import sys

sys.path.append("./m4_6")
from regression import prepare_dataset, calc_score, calc_rmse


def above90(ratio):
    """
    寄与率が90%を超えるインデックスを取る
    :param ratio:
    :return:
    """
    cum_var_exp = np.cumsum(ratio)
    return np.where(cum_var_exp > 0.95)[0][0]


def objective(X, y, trial):
    # paramter_tuning using optuna
    num_leaves = trial.suggest_int('num_leaves', 2, 1000),
    n_estimators = trial.suggest_int('n_estimators', 1, 1000)
    max_depth = trial.suggest_int('max_depth', 1, 75)
    min_child_weight = trial.suggest_int('min_child_weight', 1, 75)
    subsample = trial.suggest_discrete_uniform('subsample', 0.5, 0.9, 0.1)
    colsample_bytree = trial.suggest_discrete_uniform('colsample_bytree', 0.5, 0.9, 0.1)

    params = {
        "random_state": 42,
        "n_estimators": n_estimators,
        "max_depth": max_depth,
        "num_leaves": num_leaves,
        "min_child_weight": min_child_weight,
        "subsample": subsample,
        "colsample_bytree": colsample_bytree
    }

    model_opt = lgb.LGBMRegressor(**params)
    y_pred = cross_val_predict(model_opt, X, y, cv=4)
    return calc_rmse(y, y_pred)


if __name__ == '__main__':
    df_2d, Y = prepare_dataset("data/2d_desc.csv", "data/fukunishi_data.csv", norm=False)
    df_3d, Y = prepare_dataset("data/3d_desc.csv", "data/fukunishi_data.csv", norm=False)
    df_fing, Y = prepare_dataset("data/fing_desc.csv", "data/fukunishi_data.csv", norm=False)
    df_all = pd.concat([df_2d, df_3d, df_fing], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(df_all, Y, test_size=0.2, random_state=2)

    # 標準化
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)

    # pca = PCA(n_components=None)
    # X_train_pca = pca.fit_transform(X_train_std)
    # X_test_pca = pca.transform(X_test_std)
    # print(above90(pca.explained_variance_ratio_))    # 結果　256
    # exit()

    # 次元削減
    pca = PCA(n_components=50)
    X_train_pca = pca.fit_transform(X_train_std)
    X_test_pca = pca.transform(X_test_std)

    # optunaを利用する
    study_rmse = optuna.create_study(direction='minimize')
    f = partial(objective, X_train_pca, y_train)
    study_rmse.optimize(f, n_trials=500)
    print(study_rmse.best_params)

    # trial = study_rmse.best_trial

    f_model = lgb.LGBMRegressor(**study_rmse.best_params)
    f_model.fit(X_train_pca, y_train)
    y_pred = f_model.predict(X_test_pca)
    print(calc_score(y_test, y_pred))

    # params = {
    #     "max_depth": [10, 25, 50, 75],
    #     "learning_rate": [0.001, 0.01, 0.05, 0.1],
    #     "num_leaves": [100, 300, 900, 1200],
    #     "n_estimators": [100, 200, 500]
    # }
    #
    # lgb_reg = lgb.LGBMRegressor()
    #
    # gs = GridSearchCV(estimator=lgb_reg,
    #                   param_grid=params,
    #                   scoring='neg_mean_squared_error',
    #                   cv=4)
    #
    # gs.fit(X_train_pca, y_train)
    # print('best_param')
    # print(gs.best_params_)
    # y_pred = gs.predict(X_test_pca)
    # print(calc_score(y_test, y_pred))
    #
