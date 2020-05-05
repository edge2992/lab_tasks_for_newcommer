"""
finger printから回帰を試す
Ridge
SVR
lightGBM
random forest regression
"""

from m_3d import check_all


if __name__ == '__main__':
    Xfile = "../data/fing_desc.csv"
    Yfile = "../data/fukunishi_data.csv"
    dir_path = "../result/param_fing/"
    check_all(Xfile, Yfile, dir_path)
