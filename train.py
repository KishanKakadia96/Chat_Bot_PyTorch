import json
from src.utils.nltk_utils import tokenize,stem

with open(r'C:\Kishan\Github\NLP\Chat_Bot_PyTorch\intent.json','r') as f:
    intents = json.loads(f)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['pattern']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy = .append((w,tag))





