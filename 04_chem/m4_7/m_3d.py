"""
3d記述子から回帰を試す
Ridge
SVR
lightGBM
random forest regression
"""

from lgb_reg import check_lgb
from randomforest import check_rfr
from svr import check_svr
from ..m4_6.ridge import check_ridge


def check_all(Xfile, Yfile, dir_path):
    check_ridge(Xfile, Yfile, dir_path)
    check_svr(Xfile, Yfile, dir_path)
    check_lgb(Xfile, Yfile, dir_path)
    check_rfr(Xfile, Yfile, dir_path)

if __name__ == '__main__':
    Xfile = "../data/3d_desc.csv"
    Yfile = "../data/fukunishi_data.csv"
    dir_path = "../result/param_3d/"
    check_all(Xfile, Yfile, dir_path)
