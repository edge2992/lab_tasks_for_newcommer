from regression import prepare_dataset, grid_many
import lightgbm as lgb


def check_lgb(Xfile, Yfile):
    X, Y = prepare_dataset(Xfile, Yfile, norm=False)
    print('=' * 5 + "lightGBM" + '=' * 5)

    params = {
        "lgbmregressor__max_depth": [10, 25, 50, 75],
        "lgbmregressor__learning_rate": [0.001, 0.01, 0.05, 0.1],
        "lgbmregressor__num_leaves": [100, 300, 900, 1200],
        "lgbmregressor__n_estimators": [100, 200, 500]
    }

    lgb_reg = lgb.LGBMRegressor()
    grid_many(lgb_reg, X, Y, params)


if __name__ == '__main__':
    check_lgb("../data/2d_desc.csv", "../data/fukunishi_data.csv")
