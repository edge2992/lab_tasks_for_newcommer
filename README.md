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

### 4.6 4.7 回帰モデルの比較
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
![予測と実験値の関係](https://github.com/kaz-i-54/lab_tasks_for_newcommer/blob/master/04_chem/m4_8/data/Assay%20ID_scatter_pred_true.png)

test全体（199個）  
>CHEMBL3431937    86  
CHEMBL1034536    43  
CHEMBL905613     34  
Astellas         14  
CHEMBL3430218    11  
CHEMBL905612     10  
Enamine           1  

予測が良かったもの（25個）
>CHEMBL3431937    14  
CHEMBL905613      5  
CHEMBL1034536     4  
CHEMBL905612      1  
CHEMBL3430218     1  

予測が悪かったもの（25個）  
>CHEMBL1034536    12  
CHEMBL3431937     7  
CHEMBL905613      3  
CHEMBL3430218     2  
CHEMBL905612      1  

CHEMBL1034536において12/43が予測のワースト25に該当した  

#### 3.化合物を記述してみて見た目でなにか違いがあるかを調べる
[結果](https://github.com/kaz-i-54/lab_tasks_for_newcommer/tree/master/04_chem/result/diff_all)

ベンゼン環が一つしかないものが予測の悪いもので比較的多いことがわかった。

### 4. 予測と実験値の関係についてラベリングをして、クラス分類してみる
![予測と実験値の関係_0.4](https://github.com/kaz-i-54/lab_tasks_for_newcommer/blob/master/04_chem/m4_8/data/classify/Assay%20ID_scatter_pred_true.png)

次のように分類した

![分類](https://github.com/kaz-i-54/lab_tasks_for_newcommer/blob/master/04_chem/m4_8/data/classify/compare_scatter_pred_true.png)

予測が外れたものに重みをつけてSVCでグリッドサーチをしてみたところあまりうまく学習できなかった。
GridSearchでのクラス分類による混同行列は以下のようになった。評価ではマシューズ相関係数を利用した。

![混同行列](https://github.com/kaz-i-54/lab_tasks_for_newcommer/blob/master/04_chem/m4_8/data/classify/svc_confusion.png)

SBSによる特徴量抽出も試みた。マシューズ相関係数で評価をすると特徴量の数が20ほどでも良いスコアが出ることがわかったので、これらの特徴量からペアプロットを描画した。予測の悪さの原因となるような特徴量を見つけることができなかった。

![SBS](https://github.com/kaz-i-54/lab_tasks_for_newcommer/blob/master/04_chem/m4_8/data/classify/sbs.png)

![ペアプロット](https://github.com/kaz-i-54/lab_tasks_for_newcommer/blob/master/04_chem/m4_8/data/classify/pairplot.png)


### 4.9 発展
2D, 3D記述子とfinger printを合わせて、次元削減した。次元削減では固有値の分散説明率の累積が0.9以上となるn_component = 256として、optunaを利用してハイパーパラメーターを探索した。  

n_trials=500 とした

#### n_component~50 の場合
>{'num_leaves': 763, 'n_estimators': 116, 'max_depth': 3, 'min_child_weight': 22, 'subsample': 0.7, 'colsample_bytree': 0.8}  
RMSE: 0.59108  
q2  : 0.70698  

#### n_component=100 の場合
>{'num_leaves': 120, 'n_estimators': 59, 'max_depth': 39, 'min_child_weight': 21, 'subsample': 0.7, 'colsample_bytree': 0.8}  
RMSE: 0.56623  
q2  : 0.73111  

#### n_component=256 の場合
>{'num_leaves': 337, 'n_estimators': 591, 'max_depth': 3, 'min_child_weight': 24, 'subsample': 0.5, 'colsample_bytree': 0.7}  
RMSE: 0.56858  
q2  : 0.72886

#### 参考
普通に2d記述子(201個)でoptunaを用いた場合のスコア  
>{'num_leaves': 5, 'n_estimators': 289, 'max_depth': 53, 'min_child_weight': 17, 'subsample': 0.5, 'colsample_bytree': 0.7}  
RMSE: 0.48588  
q2  : 0.80200  

