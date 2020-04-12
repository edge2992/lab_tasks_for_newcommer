from sklearn.metrics import confusion_matrix, roc_curve
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

from m3_1 import eval_model, preapare_dataset


def grid(X, Y, params, model, n_jobs=-1):
    #     kf = KFold(n_splits=10, shuffle=True, random_state=42)

    gs = GridSearchCV(estimator=model,
                      param_grid=params,
                      cv=10,
                      n_jobs=n_jobs)

    gs.fit(X, Y)
    print(gs.best_params_)

    # 評価
    y_pred_gs = gs.predict(X)
    confusion_matrix(Y, y_pred_gs)

    y_score_gs = gs.predict_proba(X)

    eval_model(Y, y_pred_gs, y_score_gs)

    return gs

if __name__ == '__main__':

    X, Y = preapare_dataset("data/ionosphere.csv")
    # candidate_params = {
    #     'C': [1, 10, 100, 1000],
    #     'gamma': [00.1, 0.1, 1, 10],
    # }
    #
    # svm = SVC(kernel='rbf', probability=True)
    #
    # gs = grid(X, Y, candidate_params, svm)
    #

    params2 = {
        'C': list(range(50, 150, 20)),
        'gamma': [i / 10 for i in range(1, 6, 1)],
    }

    svm = SVC(kernel='rbf', probability=True)
    gs2 = grid(X, Y, params2, svm)


# {'C': 50, 'gamma': 0.2}
# precision score of test set: 1.00000
# recall score of test set: 1.00000
# auc score of test set: 1.00000
# matthews_corrcoef score of test set: 1.00000
# f score of test set: 1.00000


