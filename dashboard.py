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


def check_letter(sentence, letter):
    counter = 0
    special_chars = [" ", "?", "."]
    for char in sentence:
        if char.lower() == letter.lower() and letter not in special_chars:
            counter += 1

    return counter


def show_sentences(sentence):
    
    converted_sentence = "".join([u"\u2593" if letter == " " else "_" for letter in sentence])
    print(converted_sentence)


s = get_random_sentence()["name"]
show_sentences(s)
