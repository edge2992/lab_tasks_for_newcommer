import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, matthews_corrcoef
from sklearn.metrics import roc_curve, auc

from sklearn.model_selection import KFold, cross_val_score, cross_val_predict
from sklearn.svm import SVC


def preapare_dataset(filename, norm=True):
    df = pd.read_csv("data/ionosphere.csv", dtype=np.float64)
    df_na = df.fillna(df.median())

    Y = df_na["0"]
    X = df_na.drop(["0"], axis=1)

    if norm:
        # 標準化
        scaler = StandardScaler()
        X_norm = scaler.fit_transform(X)
        return X_norm, Y

    return X, Y


def eval_model(y_test, y_pred, y_score):
    fpr, tpr, thresholds = roc_curve(y_test, y_score[:, 1])
    print('precision score of test set: {:.5f}'.format(precision_score(y_test, y_pred)))
    print('recall score of test set: {:.5f}'.format(recall_score(y_test, y_pred)))
    print('auc score of test set: {:.5f}'.format(auc(fpr, tpr)))
    print('matthews_corrcoef score of test set: {:.5f}'.format(matthews_corrcoef(y_test, y_pred)))
    print('f score of test set: {:.5f}'.format(f1_score(y_test, y_pred)))


if __name__ == '__main__':
    X, Y = preapare_dataset("data/ionosphere.csv")

    kf = KFold(n_splits=10, shuffle=True, random_state=42)
    svm = SVC(kernel='rbf', probability=True)

    scores = cross_val_score(svm, X=X, y=Y, cv=kf)

    y_pred = cross_val_predict(svm, X, Y, cv=kf)
    y_score = cross_val_predict(svm, X, Y, cv=kf, method='predict_proba')

    eval_model(Y, y_pred, y_score)


# precision score of test set: 0.89919
# recall score of test set: 0.99111
# auc score of test set: 0.98106
# matthews_corrcoef score of test set: 0.83510
# f score of test set: 0.94292