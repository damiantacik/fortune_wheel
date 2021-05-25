from random import randint

sentences = [
    {
        "name": "Cztery osiemnastki jeden",
        "category": "Music",
        "level": 1,
        "used": False
    },
    {
        "name": "Cztery osiemnastki dwa",
        "category": "Music",
        "level": 1,
        "used": False
    },
    {
        "name": "Cztery osiemnastki trzy",
        "category": "Music",
        "level": 1,
        "used": False
    }
]

def get_random_sentence():
    not_used_sentences = [sentence for sentence in sentences if not sentence["used"]]
    sentence = not_used_sentences[randint(0, len(sentences) - 1)]

    sentence["used"] = True
    return sentence


print(get_random_sentence())