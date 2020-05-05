"""
次元を削減して組み合わせる
"""
import pandas as pd
from sklearn.decomposition import PCA
from regression import prepare_dataset


def zigen(df, n_components=10):
    """
    次元削減できるかどうか
    :param df:
    :param n_components:
    :return:
    """
    pca = PCA(n_components=n_components)
    vecs_list = pca.fit_transform(df)
    print(pca.explained_variance_ratio_)
    return pca


if __name__ == '__main__':
    df_2d, Y = prepare_dataset("data/2d_desc.csv", "data/fukunishi_data.csv")
    pca2 = zigen(df_2d, 20)
    df_3d, Y = prepare_dataset("data/2d_desc.csv", "data/fukunishi_data.csv")
    pca3 = zigen(df_3d, 20)
    df_fing, Y = prepare_dataset("data/2d_desc.csv", "data/fukunishi_data.csv")
    pca_f = zigen(df_fing, 20)

    X1 = pca2.fit_transform(df_2d)[:,:17]
    X2 = pca2.fit_transform(df_3d)[:,:17]
    X3 = pca2.fit_transform(df_fing)[:,:17]

    dX1 = pd.DataFrame(X1)
    dX2 = pd.DataFrame(X2)
    dX3 = pd.DataFrame(X3)
    print(X1.shape)

    X_all = pd.concat([dX1, dX2, dX3], axis=1)
    print(X_all.shape)

    X_all.to_csv("data/pca_all_X.csv")

    # param_grid = {"max_depth": [10, 25, 50, 75],
    #               "learning_rate": [0.001, 0.01, 0.05, 0.1],
    #               "num_leaves": [100, 300, 900, 1200],
    #               "n_estimators": [100, 200, 500]
    #               }
    #
    # lgb_reg = lgb.LGBMRegressor()
    # gs = grid(X_all, Y, param_grid, lgb_reg, n_jobs=1) # not pararel
    # lgb_reg_b = lgb.LGBMRegressor(**gs.best_params_)
    # cv_regression(lgb_reg_b, X_all, Y)

    """
    result of cv_regression
    
    {'learning_rate': 0.05, 'max_depth': 10, 'n_estimators': 100, 'num_leaves': 100}
    [0.46374623 0.56679926 0.51474936 0.60720363]
    [0.81077844 0.77094413 0.79797981 0.70989517]
    mean rmse: 0.53812
    mean r2: 0.77240

    """


