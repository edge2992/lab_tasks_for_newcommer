from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import cohen_kappa_score, make_scorer, matthews_corrcoef, plot_confusion_matrix, confusion_matrix
from sklearn.svm import SVC

from classify_data_reduce import Reduce_label
from classify_dataprepare import load_classify_datasets
import matplotlib.pyplot as plt

X, y = load_classify_datasets()

svc = SVC(C=1.0, gamma=1.0, class_weight={"exp>pred": 1000, "pred=exp": 1, "pred>exp": 1000})


#標準化してテストとトレインに分けるためだけに利用する(機能を持ちすぎ)
rel = Reduce_label(X, y, svc, 1, matthews_corrcoef)

# rel.fit()
# rel.plot_performance()
# print(rel.get_label_name(25))

X_train, X_test, y_train, y_test = rel.get_datasets()


param_range = [0.001, 0.01, 0.1, 1.0, 10.0, 100.0]

params = {
        'C': param_range,
        'gamma': param_range
}

mcc_scorer = make_scorer(matthews_corrcoef)

svc = SVC(C=1.0, gamma=1.0, class_weight={"exp>pred": 10, "pred=exp": 1, "pred>exp": 10})
# svc = SVC(C=1.0, gamma=1.0)

gs = GridSearchCV(estimator=svc,
                      param_grid=params,
                      scoring =mcc_scorer,
                      cv=4,
                      n_jobs=-1)

gs.fit(X_train, y_train)
print('best_param')
print(gs.best_params_)
plot_confusion_matrix(gs, X_test, y_test)

plt.savefig("data/classify/svc_confusion.png")
plt.show()
y_pred = gs.predict(X_test)
print(matthews_corrcoef(y_test, y_pred))