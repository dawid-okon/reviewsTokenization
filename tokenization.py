import re
from collections import Counter

# Tokenization
def tokenize(text):
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    tokens = [token.lower() for token in tokens]
    return tokens

with open("reviews.txt", "r", encoding="utf-8") as file:
    reviews = file.readlines()

allTokens = []
for review in reviews:
    allTokens.extend(tokenize(review))


# All tokens count dict
tokenCount = Counter(allTokens)
print(tokenCount)
keywords = {"świetny", "dostawa", "słabo", "szybka", "dostawa", "polecam", "nie", "cena", "jakość"}

# Keywords count dict
keywordCount = Counter()
for token in allTokens:
    for keyword in keywords:
        if keyword in token:
            keywordCount[keyword] += 1
            # print(keywordCount)


print("Wystąpienia tokenów:")
for token, count in sorted(tokenCount.items(), key=lambda x: x[1], reverse=True):
    print(f"{token}: {count}")

print("\nWystąpienia słów kluczowych:")
for keyword, count in sorted(keywordCount.items(), key=lambda x: x[1], reverse=True):
    print(f"{keyword}: {count}")