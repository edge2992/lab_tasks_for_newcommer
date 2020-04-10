from sklearn import linear_model
from sklearn.svm import SVR

from sklearn.preprocessing import StandardScaler
import pandas as pd

from calc_score import cv_regression
from hyper_params import grid
from sklearn.ensemble import RandomForestRegressor as RFR
import lightgbm as lgb


def prepare_dataset(filename_X, filename_Y, norm=True):
    X = pd.read_csv(filename_X, index_col=0)
    Y = pd.read_csv(filename_Y, index_col=0)["LogP app"]

    if norm:
        # 標準化
        scaler = StandardScaler()
        X_norm = scaler.fit_transform(X)
        return X_norm, Y

    return X, Y


def try_all_models(filename_X, filename_Y):
    X, Y = prepare_dataset(filename_X, filename_Y)
    # print("==========-RIDGE==========-")
    # params = {
    #     'alpha': [0.01, 0.1, 1.0, 10.0]
    # }
    #
    # reg = linear_model.Ridge()
    # gs = grid(X, Y, params, reg)
    # reg_b = linear_model.Ridge(**gs.best_params_)
    # cv_regression(reg_b, X, Y)
    #
    # print("==========-SVR==========-")
    #
    # params = {
    #     'C': [0.001, 0.01, 0.1, 1, 10],
    #     'gamma': [0.001, 0.01, 0.1, 1],
    # }
    #
    # svr = SVR(kernel='linear')
    # gs = grid(X, Y, params, svr)
    # svr_b = SVR(kernel='linear', **gs.best_params_)
    # cv_regression(svr_b, X, Y)
    #
    # print("==========Random Forest Regression==========-")
    #
    # params = {
    #     'n_estimators': [5, 10, 20, 30, 50, 100, 300],
    #     'max_features': ['auto', 'sqrt', 'log2'],
    #     'random_state': [2525],
    #     'n_jobs': [-1],
    #     'min_samples_split': [3, 5, 10, 15, 20, 25, 30, 40, 50, 100],
    #     'max_depth': [3, 5, 10, 15, 20, 25, 30, 40, 50, 100]
    # }
    #
    # rf = RFR()
    # gs = grid(X, Y, params, rf)
    # rfr_reg = RFR(**gs.best_params_)
    # cv_regression(rfr_reg, X, Y)

    print("==========lightGBM==========-")

    param_grid = {"max_depth": [10, 25, 50, 75],
                  "learning_rate": [0.001, 0.01, 0.05, 0.1],
                  "num_leaves": [100, 300, 900, 1200],
                  "n_estimators": [100, 200, 500]
                  }

    lgb_reg = lgb.LGBMRegressor()
    gs = grid(X, Y, param_grid, lgb_reg, n_jobs=1) # not pararel
    lgb_reg_b = lgb.LGBMRegressor(**gs.best_params_)
    cv_regression(lgb_reg_b, X, Y)


if __name__ == '__main__':
    try_all_models("data/2d_desc.csv", "data/fukunishi_data.csv")


