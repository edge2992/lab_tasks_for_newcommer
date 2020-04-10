# 最も良かったのは2d記述子で、
# LightBGM
#　{'learning_rate': 0.05, 'max_depth': 25, 'n_estimators': 200, 'num_leaves': 100}
from sklearn.model_selection import train_test_split

from calc_score import cv_regression
from m4_6_2d import prepare_dataset
import pandas as pd
import numpy as np
import lightgbm as lgb


def get_sorted_diff(y_true, y_pred, x_test):
    df_ex = pd.read_csv("data/fukunishi_data.csv")
    y_diff = [abs(y_p - y_t) for y_p, y_t in zip(y_pred, y_true)]
    df_diff = pd.DataFrame(y_diff, x_test.index, columns=["diff"])
    df_diff = pd.concat([df_diff, df_ex[["Assay ID", "SMILES"]]], join="inner", axis=1)
    df_s = df_diff.sort_values('diff')
    return df_s

best_param = {'learning_rate': 0.05, 'max_depth': 25, 'n_estimators': 200, 'num_leaves': 100}

X, Y = prepare_dataset("data/2d_desc.csv", "data/fukunishi_data.csv")
X = pd.DataFrame(X)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, shuffle=True)

model = lgb.LGBMRegressor(**best_param)
model.fit(X_train, Y_train)
y_pred = model.predict(X)

df_diff = get_sorted_diff(Y, y_pred, X)

print(df_diff.head())



