import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# open the file containing the semantic similarity scores
with open('scores.txt', 'r') as f:
    scores = f.readlines()
f.close()

# store all info as a pandas dataframe
df = pd.read_csv('scores.csv', sep='\t', header=0,
                 dtype={'Match': str, 'Similarity Score': float, 'Summary Length': int,
                        'Unique Words in Summary': int, 'Sample Commentary Length': int,
                        'Unique Words in Sample Commentary': int, 'Full Commentary Length': int,
                        'Unique Words in Full Commentary': int})


def cor_heatmap():
    # create a correlation heatmap
    sns.heatmap(df.corr(), annot=True, vmin=-1, vmax=1, fmt='.2f', linewidths=0.5, cmap='coolwarm')
    sns.diverging_palette(145, 300, s=60, as_cmap=True)
    plt.title('Correlation Heatmap for Quantitative Assessment')
    plt.tight_layout()

    plt.show()
    plt.savefig('heatmap.png')


def similarity_graph():
    # create a barplot of the semantic similarity scores
    colors = []
    for i in range(len(df['Similarity Score'])):
        if df['Similarity Score'][i] > 0.6:
            colors.append('#000000')
        elif df['Similarity Score'][i] > 0.4:
            colors.append('#2E4F4F')
        else:
            colors.append('#146C94')

    sns.barplot(x='Match', y='Similarity Score', data=df, palette=colors)
    plt.xticks(rotation=90)
    plt.xlabel('')
    plt.title('Semantic Similarity Score for Generated Summaries using BERT')
    plt.ylim(0,1)

    # set the legend to be the color of the bar
    plt.legend(handles=[plt.Rectangle((0, 0), 1, 1, fc=color, edgecolor='none') for color in ['#000000', '#2E4F4F', '#146C94']],
                                      labels=['Score > 0.6', '0.4 < Score < 0.6', 'Score < 0.4'])
    plt.tight_layout()
    plt.savefig('semantic similarity.png')


def word_count_graph():
    # create a strip-plot and a boxplot side-by-side from the word count data
    sns.stripplot(data=[df['Summary Length'], df['Unique Words in Summary'],
                        df['Sample Commentary Length'], df['Unique Words in Sample Commentary']],
                  dodge=True, alpha=.75, zorder=1, legend=True, palette=['#146C94', '#97DEFF', '#A84448', '#F48484'])
    sns.boxplot(data=[df['Summary Length'], df['Unique Words in Summary'],
                      df['Sample Commentary Length'], df['Unique Words in Sample Commentary']],
                dodge=True, width=0.1, palette=['#146C94', '#97DEFF', '#A84448', '#F48484'])

    plt.xticks([])
    plt.ylabel('Word Count')
    plt.title('Word Count comparisons for Generated Summary and Sample Commentary')
    plt.tight_layout()

    plt.show()
    plt.savefig('word count comparisons.png')