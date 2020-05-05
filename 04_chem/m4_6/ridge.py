from sklearn import linear_model

from regression import prepare_dataset, grid_many


def check_ridge(Xfile, Yfile):
    X, Y = prepare_dataset(Xfile, Yfile, norm=False)
    param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]

    print('=' * 5 + "RIDGE" + '=' * 5)
    params = {
        'ridge__alpha': param_range
    }

    reg = linear_model.Ridge()
    grid_many(reg, X, Y, params)


if __name__ == '__main__':
    check_ridge("../data/2d_desc.csv", "../data/fukunishi_data.csv")
