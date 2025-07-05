def number_of_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    counter = {}
    for character in text.lower():
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter

def new_dictionary(dictionary):
    characters = []
    for char, count in dictionary.items():
        new_item = {"char": char, "num": count}
        characters.append(new_item)
    characters.sort(reverse = True, key = lambda item: item["num"])
    return characters
