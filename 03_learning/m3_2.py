from sklearn.metrics import confusion_matrix, roc_curve
from sklearn.model_selection import GridSearchCV, KFold, train_test_split
from sklearn.svm import SVC

from m3_1 import eval_model, preapare_dataset


def grid(X, Y, params, model, scoring='neg_mean_squared_error',  n_jobs=-1):
    """
    グリッドサーチをする
    :param X:
    :param Y:
    :param params:
    :param model:
    :param scoring:
    :param n_jobs:
    :return:
    """
    kf = KFold(n_splits=10, shuffle=True, random_state=42)

    # TODO: 評価手法をAUROCとF-Scoreの二通りで試す
    gs = GridSearchCV(
        estimator=model,
        param_grid=params,
        cv=kf,
        scoring=scoring,
        n_jobs=n_jobs)

    gs.fit(X, Y)
    print(gs.best_params_)

    return gs


def regression(model, x, y):
    """

    :param model:
    :param x:
    :param y:
    :return:
    """
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, shuffle=True)
    model.fit(X_train, Y_train)

    y_pred = model.predict(X_test)
    y_score = model.predict_proba(X_test)

    eval_model(Y_test, y_pred, y_score)
    return model


def svc_p_search_and_score(X, Y, params, method):
    svm = SVC(kernel='rbf', probability=True)
    gs = grid(X, Y, params, svm, method)

    svm_b = SVC(kernel='rbf', probability=True, **gs.best_params_)
    regression(svm_b, X, Y)

    return svm_b




if __name__ == '__main__':

    X, Y = preapare_dataset("data/ionosphere.csv")

    params = {
        'C': list(range(50, 150, 20)),
        'gamma': [i / 10 for i in range(1, 6, 1)],
    }


    method1 = 'roc_auc'
    method2 = 'f1'

    print("==================" + method1 + "==================" )
    svc_p_search_and_score(X, Y, params, method1)

    print("==================" + method2 + "==================" )
    svc_p_search_and_score(X, Y, params, method2)




