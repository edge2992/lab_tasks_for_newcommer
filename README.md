ラボ新規配属者向けの課題


# 1. 配列処理
01dna/resultに結果を記載

# 2. タンパク質処理
pymolで実行
02protein/resultに結果を記載した

# 3. 機械学習
.scaleのファイルの処理方法が分からなかったので、kaggleで検索してcsvのファイルをダウンロードしてきました。

# 4. 創薬情報処理
2d記述子、3d記述子、fingerprintは04chem/m4_1-4.ipynbで用意しています。
機械学習はそれぞれの.pyで実行して、結果をresultに入れています。

最も良かったのは2D記述子を使って、lightGBMで学習したモデルでハイパーパラメータは

#　{'learning_rate': 0.05, 'max_depth': 25, 'n_estimators': 200, 'num_leaves': 100}

のようになりました
