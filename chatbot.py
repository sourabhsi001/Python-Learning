import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# train data
training_data = {
    "greet": [
        "hello", "hi", "hey", "good morning"
    ],
    "bye" : [
        "goodbye", "see you", "take care"
    ],
    "age": [
        "how old are you", "your age", "when were you created"
    ]
}

responses = {
    "greet" : [
        "Hello 🤗", "Hi There ❤", "Hey, how are you doing"
    ],
    "bye" : [
        "Goodbye 😌", "See you soon sunshine", "take care!"
    ],
    "age" : [
        "I'm am timless", "I'm created by Kratagya Sir right now", "asking someone age is not legal"
    ],
    "unknown": [
        "Hmm" , "Sorry samaj ni aaya", " I'm not sure magar manvendra mota h"
    ]
}

#data ko train krte h
X, y = [], []
for intent, examples in training_data.items():
    for ex in examples:
        X.append(ex)
        y.append(intent)

vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
clf= MultinomialNB()
# 1/5 > 1.501 , 1/5 1/6

clf.fit(X_vec, y)

def chatbot():
    print("🤖 Hi, I'm Sangarsh, I'm your chatbot, type 'quit' antime to exit.")
    while True:
        user = input("You: ").strip()
        if user.lower() in ["quit", "exit", "goodbye"]:
            print("🤖 Goodbye mote, Sangarsh will miss you 🙋‍♂")
            break
        if not user:
            print("🤖, please say something")
            continue

        user_vec = vectorizer.transform([user])
        intent = clf.predict(user_vec)[0]
        reply = random.choice(responses.get(intent, responses["unknown"]))
        print("🤖Sangarsh: ", reply)


if __name__ == "_main_":
    chatbot()