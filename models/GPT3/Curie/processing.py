import pandas as pd
from datasets import load_dataset
from tqdm import tqdm

# Load the TaPaCo dataset in English language from HuggingFace datasets library
# https://huggingface.co/datasets/tapaco
dataset = load_dataset("tapaco", "en")

def collect_data(data):
    # Process data from the "train" split of the dataset
    processed_data = []
    for data in tqdm(dataset["train"]):
        keys = data.keys()
        processed_data.append([data[key] for key in keys])

    # Create a Pandas DataFrame from the processed data and save it
    processed_df = pd.DataFrame(
        data=processed_data,
        columns=[
            "language",
            "lists",
            "paraphrase",
            "paraphrase_set_id",
            "sentence_id",
            "tags",
        ],
    )

    processed_df.to_csv("raw_training_data_preprocessed.csv", index=None)
    return processed_df

# Calling collect_data function and saving its return value to a variable
processed_df = collect_data(dataset)

# Function call
processed_df = collect_data(dataset)


def generate_dataset(dataset):
    # Selecting only "paraphrase" and "paraphrase_set_id" columns from the TAPACO dataset
    dataset_df = dataset[["paraphrase", "paraphrase_set_id"]]

    # Selecting only those paraphrase set ids which have more than one paraphrase
    non_single_labels = (
        dataset_df["paraphrase_set_id"]
        .value_counts()[dataset_df["paraphrase_set_id"].value_counts() > 1]
        .index
        .tolist()
    )

    # Creating a new DataFrame with only those paraphrases which belong to the selected paraphrase set ids
    sorted_df = dataset_df.loc[dataset_df["paraphrase_set_id"].isin(non_single_labels)]

    # Generating paraphrase pairs from the selected paraphrase set ids
    paraphrases = []

    for paraphrase_id in tqdm(sorted_df["paraphrase_set_id"].unique()):
        phrases_id = sorted_df.loc[sorted_df["paraphrase_set_id"] == paraphrase_id]

        # Making sure that there are an even number of paraphrases in each paraphrase set
        phrases_length = (
            phrases_id.shape[0]
            if phrases_id.shape[0] % 2 == 0
            else phrases_id.shape[0] - 1
        )

        # Generating paraphrase pairs by iterating over each paraphrase set
        for i in range(0, phrases_length, 2):
            cur_phrase = phrases_id.iloc[i][0]
            for count_idx in range(i+1, i+2):
                next_phrase = phrases_id.iloc[i+1][0]
                paraphrases.append([cur_phrase, next_phrase])

    # Creating a new DataFrame from the generated paraphrase pairs and saving it to a CSV file
    paraphrases_dataset_df = pd.DataFrame(paraphrases, columns=["input", "target"])
    paraphrases_dataset_df.to_csv("processed_dataset.csv", index=None)

    return paraphrases_dataset_df

# Calling generate_dataset function and saving its return value to a variable
paraphrases_dataset_df = generate_dataset(processed_df)

