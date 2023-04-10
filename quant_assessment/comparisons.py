import glob
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# get the sample commentaries
with open('testing_file.txt', 'r') as f:
    testing_df = f.readlines()
f.close()

# get the model-generated commentaries
with open('summary_file.txt', 'r') as f:
    summary_df = f.readlines()
f.close()

# get the list of matches
with open('/Users/avimalhotra/Desktop/Uni/Year4/CS4514 FYP/FYP Code/matches.txt', 'r') as f:
    matches = f.readlines()
f.close()

# sort the matches
matches = sorted(matches)
generated_summaries = sorted(glob.glob('/Users/avimalhotra/Desktop/Uni/Year4/CS4514 FYP/FYP Code/summaries/*csv'))
sample_commentaries = sorted(glob.glob('/Users/avimalhotra/Desktop/Uni/Year4/CS4514 FYP/FYP Code/testing/*csv'))
full_commentaries = sorted(glob.glob('/Users/avimalhotra/Desktop/Uni/Year4/CS4514 FYP/FYP Code/match_commentary/*csv'))

# define variables for comparison
x_values = []
y_values = []

count_summaries = []
unique_count_summaries = []

count_sample = []
unique_count_sample = []

count_commentaries = []
unique_count_commentaries = []

# store the word count data for all summaries
for i in range(len(matches)):
    with open(generated_summaries[i], 'r') as f:
        lines = f.read()
        count_summaries.append(len(lines.split()))
        unique_count_summaries.append(len(set(lines.split())))
    f.close()

    with open(sample_commentaries[i], 'r') as f:
        lines = f.read()
        count_sample.append(len(lines.split()))
        unique_count_sample.append(len(set(lines.split())))
    f.close()

    with open(full_commentaries[i], 'r') as f:
        lines = f.read()
        count_commentaries.append(len(lines.split()))
        unique_count_commentaries.append(len(set(lines.split())))
    f.close()


for i in range(len(testing_df)):
    # Load BERT model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

    # select the sentences
    sentence1 = testing_df[i]
    sentence2 = summary_df[i]

    # Tokenize sentences and convert to PyTorch tensors
    inputs = tokenizer(sentence1, sentence2, return_tensors='pt', padding=True, truncation=True)

    # Run model and get the similarity score
    outputs = model(**inputs)
    similarity_score = torch.softmax(outputs.logits, dim=1)[0][1].item()

    # Print similarity score
    print(f"Similarity score for {matches[i]}:", similarity_score)
    x_values.append(matches[i].strip('\n'))

    # round to 3 decimal places
    y_values.append(round(similarity_score, 3))

# write the data to a file
with open('scores.txt', 'w') as f:
    f.write('Match\t'
            'Similarity Score\t'
            'Summary Length\t'
            'Unique Words in Summary\t'
            'Sample Commentary Length\t'
            'Unique Words in Sample Commentary\t'
            'Full Commentary Length\t'
            'Unique Words in Full Commentary\n')

    for i in range(len(x_values)):
        f.write(x_values[i] + '\t'
                + str(y_values[i]) + '\t'
                + str(count_summaries[i])
                + '\t' + str(unique_count_summaries[i])
                + '\t' + str(count_sample[i])
                + '\t' + str(unique_count_sample[i])
                + '\t' + str(count_commentaries[i])
                + '\t' + str(unique_count_commentaries[i]) + '\n')
f.close()