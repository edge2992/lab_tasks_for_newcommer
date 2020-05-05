from sklearn.svm import SVR

from regression import prepare_dataset, grid_many


def check_svr(Xfile, Yfile, dir_path):
    X, Y = prepare_dataset(Xfile, Yfile, norm=False)
    param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]
    # test_range = [0.1, 1.0,  10.0]
    print('=' * 5 + "SVR" + '=' * 5)
    params = {
        'svr__C': param_range,
        'svr__gamma': param_range
    }

    svr = SVR(kernel='linear')

    grid_many(svr, X, Y, params, dir_path)


if __name__ == '__main__':
    check_svr("../data/2d_desc.csv", "../data/fukunishi_data.csv", "../result/param_2d/")
