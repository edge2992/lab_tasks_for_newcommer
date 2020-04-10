from sklearn import linear_model
from sklearn.model_selection import GridSearchCV, KFold, cross_val_predict
from sklearn.utils import cpu_count

from calc_score import calc_rmse


def grid(X, Y, params, model, n_jobs=-1):
    kf = KFold(n_splits=4, shuffle=True, random_state=42)

    # MSE
    gs = GridSearchCV(
        estimator=model,
        param_grid=params,
        cv=kf,
        scoring='neg_mean_squared_error',
        n_jobs=n_jobs)

    gs.fit(X, Y)
    print(gs.best_params_)

    return gs

