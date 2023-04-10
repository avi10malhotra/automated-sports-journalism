import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def match_1_plot():
    # open the xlsx file
    dataset = pd.read_excel('MORvCRO.xlsx')
    sns.set_theme(style="whitegrid")

    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # create the violinplot
    vplot = sns.violinplot(data=dataset, y="Criteria Score", x="Criteria", hue="Survey Group",
                           palette="Set2",scale="count", scale_hue=True, bw=0.2, cut=0, linewidth=1.5
                           )
    vplot.set_ylim(1, 10)
    vplot.set_xlabel("")
    vplot.set_title("Commentary grading for Morocco vs Croatia (Group Stage Match)")

    # Improve the legend
    sns.move_legend(
        ax, loc="best", ncol=1, frameon=True, columnspacing=1, handletextpad=1, handlelength=1, borderpad=1
    )

    plt.show()
    f.savefig("MORvCRO.png", dpi=300)


def match_2_plot():
    # open the xlsx file
    dataset = pd.read_excel('ARGvFRA.xlsx')
    sns.set_theme(style="whitegrid")

    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # create the violinplot
    vplot = sns.violinplot(data=dataset, y="Criteria Score", x="Criteria", hue="Survey Group",
                           palette="Set2", scale="count", scale_hue=True, bw=0.2, cut=0, linewidth=1.5
                           )
    vplot.set_ylim(1, 10)
    vplot.set_xlabel("")
    vplot.set_title("Commentary grading for Argentina vs France (World Cup Final)")

    # Improve the legend
    sns.move_legend(
        ax, loc="best", ncol=1, frameon=True, columnspacing=1, handletextpad=1, handlelength=1, borderpad=1
    )

    plt.show()
    f.savefig("ARGvFRA.png", dpi=300)


def match_3_plot():
    # open the xlsx file
    dataset = pd.read_excel('GERvJAP.xlsx')
    sns.set_theme(style="whitegrid")

    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # create the violinplot
    vplot = sns.violinplot(data=dataset, y="Criteria Score", x="Criteria", hue="Survey Group",
                           palette="Set2", scale="count", scale_hue=True, bw=0.2, cut=0, linewidth=1.5
                           )
    vplot.set_ylim(1, 10)
    vplot.set_xlabel("")
    vplot.set_title("Commentary grading for Germany vs Japan (Group Stage Match)")

    # Improve the legend
    sns.move_legend(
        ax, loc="best", ncol=1, frameon=True, columnspacing=1, handletextpad=1, handlelength=1, borderpad=1
    )

    plt.show()
    f.savefig("GERvJapan.png", dpi=300)


def match_4_plot():
    # open the xlsx file
    dataset = pd.read_excel('PORvSWI.xlsx')
    sns.set_theme(style="whitegrid")

    f, ax = plt.subplots()
    sns.despine(bottom=True, left=True)

    # create the violinplot
    vplot = sns.violinplot(data=dataset, y="Criteria Score", x="Criteria", hue="Survey Group",
                           palette="Set2", scale="count", scale_hue=True, bw=0.2, cut=0, linewidth=1.5
                           )
    vplot.set_ylim(1, 10)
    vplot.set_xlabel("")
    vplot.set_title("Commentary grading for Portugal vs. Switzerland (Round of 16 Match)")

    # Improve the legend
    sns.move_legend(
        ax, loc="best", ncol=1, frameon=True, columnspacing=1, handletextpad=1, handlelength=1, borderpad=1
    )

    plt.show()
    f.savefig("PORvSWI.png", dpi=300)


