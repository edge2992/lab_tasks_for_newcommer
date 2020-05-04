import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from m3_1 import eval_model, preapare_dataset

X, Y = preapare_dataset("data/ionosphere.csv", norm=False)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=1)

pipe_svc = make_pipeline(StandardScaler(), SVC(kernel='rbf', probability=True))

param_range = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
param_grid = {
    'svc__C': param_range,
    'svc__gamma': param_range
}
scores = ['roc_auc', 'f1']

for score in scores:
    print('='*20 + score + '='*20)

    gs = GridSearchCV(estimator=pipe_svc,
                      param_grid=param_grid,
                      scoring=score,
                      cv=10,
                      n_jobs=-1)
    gs.fit(X_train, y_train)
    print('best_param')
    print(gs.best_params_)

    y_pred = gs.predict(X_test)
    y_score = gs.predict_proba(X_test)
    eval_model(y_test, y_pred, y_score)