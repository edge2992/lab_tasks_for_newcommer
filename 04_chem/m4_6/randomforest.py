
from regression import prepare_dataset, grid_many
from sklearn.ensemble import RandomForestRegressor as RFR


def check_rfr(Xfile, Yfile, dir_path):
    X, Y = prepare_dataset(Xfile, Yfile, norm=False)
    print('=' * 5 + "Random Forest Regression" + '=' * 5)

    params = {
        'randomforestregressor__n_estimators': [5, 10, 20, 30, 50, 100, 300],
        'randomforestregressor__max_features': ['auto', 'sqrt', 'log2'],
        'randomforestregressor__random_state': [2525],
        'randomforestregressor__n_jobs': [-1],
        'randomforestregressor__min_samples_split': [3, 5, 10, 15, 20, 25, 50, 100],
        'randomforestregressor__max_depth': [3, 5, 10, 15, 20, 25, 50, 100]
    }

    rf = RFR()
    grid_many(rf, X, Y, params, dir_path)


if __name__ == '__main__':
    check_rfr("../data/2d_desc.csv", "../data/fukunishi_data.csv", "../result/param_2d/")
