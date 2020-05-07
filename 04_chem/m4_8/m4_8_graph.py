"""
AssayIDごとに散布図を描画する
"""

import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties

font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams["font.size"] = 10


def compare_with_graph(df, split="Assay ID", file_dir="./"):
    """
    予測値と測定値について散布図を描画して比較する
    :param youso: グラフの色分けに利用するインデックスの名前
    :param df:
    """
    logpapp_min = min([df["Log_app(pred)"].min(), df["Log_app(true)"].min()])
    logpapp_max = max([df["Log_app(pred)"].max(), df["Log_app(true)"].max()])

    # グラフを描画する

    pred = df["Log_app(pred)"]
    true = df["Log_app(true)"]

    fig, ax = plt.subplots()
    ax.set_title("予測値と測定値の比較", fontsize=15)
    ax.set_xlim(logpapp_min, logpapp_max)
    ax.set_ylim(logpapp_min, logpapp_max)
    ax.set_xlabel("Log_app(pred)", size=10)
    ax.set_ylabel("Log_app(true)", size=10)

    for assay in df[split].unique():
        buf = df[df[split] == assay]
        ax.scatter(buf["Log_app(pred)"], buf["Log_app(true)"], label=assay)
    ax.legend(loc="upper left", fontsize=10)

    file_path = file_dir + split + "_scatter_pred_true.png"
    print(file_path)
    plt.savefig(file_path)

    # plt.show()


if __name__ == '__main__':
    df = pd.read_csv("../result/diff_sorted_test.csv")

    compare_with_graph(df, file_dir="data/")
