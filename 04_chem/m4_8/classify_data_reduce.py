"""
特徴量選択をするクラス
SBSから特徴量を抽出する便利関数たち
"""


import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import precision_score, matthews_corrcoef, plot_confusion_matrix, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from classify_SBS import SBS
import pandas as pd

from classify_dataprepare import load_classify_datasets


class Reduce_label():
    # 機能
    # １．後ろからみて良いところのラベルをゲットする
    # ２．混合行列を取得する
    # ３.スコアリングを変更できる

    def __init__(self, X, y, model, k_features=150, scoring=precision_score):
        """
        Xは標準化するのでそのままで良い
        :param X:
        :param y:
        :param model:
        :param k_features:
        :param scoring:
        """
        self.X = X
        self.y = y
        self.prepare_datasets(X, y)
        self.sbs = SBS(model, k_features=k_features, scoring=scoring)
        self.trained = False

    def prepare_datasets(self, X, y):
        """
        データセットを分ける
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)

        stdsc = StandardScaler()
        self.X_train_std = stdsc.fit_transform(X_train)
        self.X_test_std = stdsc.transform(X_test)
        self.y_train = y_train
        self.y_test = y_test

    def _weight_calc(self, weight):
        """
        重みをつける
        """
        sample_weight = np.random.randn(len(self.y_train))
        self.sample_weight = [w if y_t == "pred=score" else w * 10 for w, y_t in zip(sample_weight, y)]
        return self.sample_weight

    def fit(self):
        """
        SBSを学習させる
        """
        if self.trained:
            print("already trained")
            return

        self.sbs.fit(self.X_train_std, self.y_train)

    def plot_performance(self, path="./sbs.png"):
        """
        SBSでの結果をプロットする
        """
        # plotting performance of feature subsets
        sbs = self.sbs
        k_feat = [len(k) for k in sbs.subsets_]

        plt.plot(k_feat, sbs.scores_, marker='o')
        plt.ylim([0.1, 1.1])
        plt.ylabel('f1 score')
        plt.xlabel('Number of features')
        plt.grid()
        plt.tight_layout()
        plt.savefig(path, dpi=300)
        plt.show()

    def get_label_name(self, index):
        """
        dfのcolumnsの名前を取得
        """
        column_num = self._get_label_id(index)
        self.column_name = self.X.columns[column_num]
        return self.column_name

    def _get_label_id(self, index):
        """
        columnsの番号を取得
        """
        max_score = np.max(self.sbs.scores_[-index:])
        max_index = np.argmax(self.sbs.scores_[-index:])
        print(max_score)
        return list(self.sbs.subsets_[-index:][max_index])

    def get_datasets_reduced(self, index):
        """
        削減したデータセットを取得する
        """
        columns_num = self._get_label_id(index)
        X_train_reduced = self.X_train_std[:, columns_num]
        X_test_reduced = self.X_test_std[:, columns_num]
        return X_train_reduced, X_test_reduced, self.y_train, self.y_test

    def get_datasets(self):
        """
        データセットを取得する
        """
        return self.X_train_std, self.X_test_std, self.y_train, self.y_test


if __name__ == '__main__':
    """
    特徴量を30以下に減らして混同行列を書く
    """
    X, y = load_classify_datasets()

    svc = SVC(C=1.0, gamma=1.0, class_weight={"exp>pred": 1000, "pred=exp": 1, "pred>exp": 1000})

    # クラスに偏りがあるのでmatthews_corrcoefを利用する
    rel = Reduce_label(X, y, svc, 1, f1_score)

    rel.fit()

    rel.plot_performance("data/classify/sbs.png")
    print(rel.get_label_name(25))


    X_train, X_test, y_train, y_test = rel.get_datasets_reduced(30)
    
    svc.fit(X_train, y_train)
    plot_confusion_matrix(svc ,X_test ,y_test)
    plt.show()



