import glob
import os.path
import openai
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# paste the OpenAI API key here
API_KEY = "sk-REDACTED"
NUM_OF_MATCHES = 64


def paraphrase(text):
    openai.api_key = API_KEY

    # define the parameters for the fine-tuned Curie model
    response = openai.Completion.create(
        engine="curie:ft-personal-2023-03-19-14-51-14",
        prompt="paraphrase: "+text,
        temperature=0.2,
        max_tokens=256,
        frequency_penalty=0,
        presence_penalty=0
    )

    # store the best paraphrase response
    ans = response.choices[0].text
    print(ans)
    return response.choices[0].text


def summarize(text):

    # import the BART model and tokenizer, and define the parameters
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
    inputs = tokenizer.encode(
        "summarize: " + text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    # generate the summary and return the best summary response
    outputs = model.generate(inputs,
                             max_length=200,
                             min_length=100,
                             length_penalty=2.0,
                             num_beams=4,
                             early_stopping=True
                             )

    return tokenizer.decode(outputs[0])


with open('matches.txt', 'r') as file:
    matches = sorted(file.readlines())

# get all match commentary data
path = os.getcwd() + '/match_commentary'
files = sorted(glob.glob(os.path.join(path,'*.csv')))

# iterate through all matches
for i in range(NUM_OF_MATCHES):
    with open(files[i], 'r') as f:
        lines = f.readlines()
    f.close()

    goals = []
    post_match = []

    # clean the data and extract key-events
    for line in lines:
        text = line.split('\t')
        if text[0] == 'COMMENTARY' and text[1] == 'Post Match':
            post_match = text[-1]
        elif text[0] == 'GOOOAAALLL!!!':
            goals.append((text[1], text[-1]))

    # write the data to a file
    with open(f'testing/{matches[i].strip()}.csv', 'w') as f:
        if post_match:
            f.write(post_match)
        for goal in goals:
            f.write(goal[0] + '\t' + goal[1])
    f.close()

    # generate the paraphrase and the match summary, then save it to a file
    with open(f'summaries/{matches[i].strip()}.csv', 'w') as f:
        if post_match:
            paraphrased_text = paraphrase(post_match)
            final_summary = summarize(paraphrased_text)
            f.write(final_summary)

        else:
            paraphrased_text = paraphrase(goals[0][1])
            final_summary = summarize(paraphrased_text)
            f.write(final_summary)

    f.close()


