ラボ新規配属者向けの課題


# 1. 配列処理
01dna/resultに結果を記載

# 2. タンパク質処理
ローカルのpymolで実行
02protein/resultに結果を記載した。

# 3. 機械学習
.scaleのファイルの処理方法が分からなかったので、kaggleで検索してcsvのファイルをダウンロードした。
## 3.1 結果を以下に記載する

precision score of test set: 0.89919  
recall score of test set: 0.99111  
auc score of test set: 0.98106  
matthews_corrcoef score of test set: 0.83510  
f score of test set: 0.94292  
## 3.2 結果を以下に記載する
==================roc_auc==================  
{'C': 50, 'gamma': 0.2}  
precision score of test set: 0.98077  
recall score of test set: 0.91071  
auc score of test set: 0.96429  
matthews_corrcoef score of test set: 0.86047  
f score of test set: 0.94444  
==================f1==================  
{'C': 50, 'gamma': 0.1}  
precision score of test set: 0.94340  
recall score of test set: 0.92593  
auc score of test set: 0.97495  
matthews_corrcoef score of test set: 0.83339  
f score of test set: 0.93458  
# 4. 創薬情報処理
2d記述子、3d記述子、fingerprintは04chem/m4_1-4.ipynbで用意した。
機械学習はそれぞれの.pyで実行して、結果をresultに記載した。

最も良かったのは2D記述子を使って、lightGBMで学習したモデルでハイパーパラメータは

{'learning_rate': 0.05, 'max_depth': 25, 'n_estimators': 200, 'num_leaves': 100}  
mean rmse: 0.47811  
mean r2: 0.82085  
のようになった。


### 4.8 考察
それぞれの化合物の予測のスコアをLogPappの実験値と予測値の差で示す。
予測のスコアとAssayIDに関連はない。 
04_chem/result/diff_test には予測のスコアがが良いものと悪いものの描画を保存する。一見して２つの画像間から推測できることはない。

### 4.9 発展
次元削減をして2d, 3d, fingerprintをあわせた。(4_9.py)
optunaでパラメーター探索したスコアは
Best is trial#5 with value: 0.5431523303034916.  
{'bagging_freq': 2, 'min_data_in_leaf': 11, 'max_depth': 30, 'learning_rate': 0.06322568717428279, 'num_leaves': 486, 'num_threads': 8, 'min_sum_hessian_in_leaf': 8}  

mean rmse: 0.54587  
mean r2: 0.76672
となった。
