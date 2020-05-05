"""
比較のため２ｄ記述子で学習させる
"""
from functools import partial

import optuna
import lightgbm as lgb
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_predict
from sklearn.preprocessing import StandardScaler

import sys

from m4_9 import objective

sys.path.append("./m4_6")
from regression import prepare_dataset, calc_score, calc_rmse



if __name__ == '__main__':
    df_2d, Y = prepare_dataset("data/2d_desc.csv", "data/fukunishi_data.csv", norm=False)
    X_train, X_test, y_train, y_test = train_test_split(df_2d, Y, test_size=0.2, random_state=2)

    # 標準化
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)

    # optunaを利用する
    study_rmse = optuna.create_study(direction='minimize')
    f = partial(objective, X_train_std, y_train)
    study_rmse.optimize(f, n_trials=500)
    print(study_rmse.best_params)

    # trial = study_rmse.best_trial

    f_model = lgb.LGBMRegressor(**study_rmse.best_params)
    f_model.fit(X_train_std, y_train)
    y_pred = f_model.predict(X_test_std)
    print(calc_score(y_test, y_pred))

