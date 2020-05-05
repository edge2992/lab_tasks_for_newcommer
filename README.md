ラボ新規配属者向けの課題


# 1. 配列処理
01dna/resultに結果を記載

# 2. タンパク質処理
ローカルのpymolで実行
02protein/resultに結果を記載した。

# 3. 機械学習
## 3.1 結果を以下に記載する

>precision score of test set: 0.89919   
recall score of test set: 0.99111   
auc score of test set: 0.98106  
matthews_corrcoef score of test set: 0.83510  
f score of test set: 0.94292  
## 3.2 結果を以下に記載する
>====================roc_auc====================  
best_param
{'svc__C': 10.0, 'svc__gamma': 0.1}  
precision score of test set: 0.91304  
recall score of test set: 0.97674  
auc score of test set: 0.98256  
matthews_corrcoef score of test set: 0.85324  
f score of test set: 0.94382  
====================f1====================  
best_param
{'svc__C': 1.0, 'svc__gamma': 0.1}  
precision score of test set: 0.89362  
recall score of test set: 0.97674  
auc score of test set: 0.98754  
matthews_corrcoef score of test set: 0.82462  
f score of test set: 0.93333

# 4. 創薬情報処理
2d記述子、3d記述子、fingerprintは04chem/m4_1-4.ipynbで用意した。

回帰のモデルはRidge, RandomForest, lightGBM, SVRをそれぞれ比較した。

- [2D記述子での学習の結果](https://github.com/kaz-i-54/lab_tasks_for_newcommer/tree/master/04_chem/result/param_2d)
- [3D記述子での学習の結果](https://github.com/kaz-i-54/lab_tasks_for_newcommer/tree/master/04_chem/result/param_3d)
- [finger printでの学習の結果](https://github.com/kaz-i-54/lab_tasks_for_newcommer/tree/master/04_chem/result/param_fing)


最も良かったのは2D記述子を使って、lightGBMで学習したモデルだった。

ハイパーパラメーターと結果は以下に示す
- [結果](https://github.com/kaz-i-54/lab_tasks_for_newcommer/blob/master/04_chem/result/param_2d/LGBMRegressor.txt)

>{"lgbmregressor__learning_rate": 0.01, "lgbmregressor__max_depth": 25, "lgbmregressor__n_estimators": 500, "lgbmregressor__num_leaves": 100}  
RMSE: 0.48626  
q2  : 0.80169  


### 4.8 考察
それぞれの化合物の予測のスコアをLogPappの実験値と予測値の差で示す。

#### 1.LogP_appについて予測があたっていたものと外れていたものについて比べるために差の絶対値を取って並び替える
[テストケース199個での結果](https://github.com/kaz-i-54/lab_tasks_for_newcommer/blob/master/04_chem/result/diff_sorted_test.csv)

#### 2.良いものと悪いものについて出処に差があったかを調べる  
全体（199個）  
CHEMBL3431937    86  
CHEMBL1034536    43  
CHEMBL905613     34  
Astellas         14  
CHEMBL3430218    11  
CHEMBL905612     10  
Enamine           1  

予測が良かったもの（25個）
CHEMBL3431937    14  
CHEMBL905613      5  
CHEMBL1034536     4  
CHEMBL905612      1  
CHEMBL3430218     1  

予測が悪かったもの（25個）  
CHEMBL1034536    12  
CHEMBL3431937     7  
CHEMBL905613      3  
CHEMBL3430218     2  
CHEMBL905612      1  

CHEMBL1034536において12/43が予測のワースト25に該当した  

#### 3.化合物を記述してみて見た目でなにか違いがあるかを調べる
[結果](https://github.com/kaz-i-54/lab_tasks_for_newcommer/tree/master/04_chem/result/diff_all)

ベンゼン環が一つしかないものが予測の悪いもので比較的多いことがわかった。

### 4.9 発展
次元削減をして2d, 3d, fingerprintをあわせた。(4_9.py)
optunaでパラメーター探索したスコアは

>{'bagging_freq': 2, 'min_data_in_leaf': 7, 'max_depth': 26, 'learning_rate': 0.046492270347490636, 'num_leaves': 798, 'num_threads': 9, 'min_sum_hessian_in_leaf': 3}  
RMSE: 0.54475  
q2  : 0.75112  


