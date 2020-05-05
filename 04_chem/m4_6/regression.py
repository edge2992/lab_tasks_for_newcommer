import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def prepare_dataset(filename_X, filename_Y, norm=True):
    X = pd.read_csv(filename_X, index_col=0)
    Y = pd.read_csv(filename_Y, index_col=0)["LogP app"]

    if norm:
        # 標準化
        scaler = StandardScaler()
        X_norm = scaler.fit_transform(X)
        return X_norm, Y

    return X, Y


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


def grid_many(model, X, Y, param):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

    pipe_model = make_pipeline(StandardScaler(), model)

    gs = GridSearchCV(estimator=pipe_model,
                      param_grid=param,
                      scoring='neg_mean_squared_error',
                      cv=4,
                      n_jobs=-1)
    gs.fit(X_train, y_train)
    print('best_param')
    print(gs.best_params_)
    y_pred = gs.predict(X_test)
    # y_score = gs.predict_proba(X_test)
    calc_score(y_test, y_pred)
