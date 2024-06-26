def main():
    file_path = "books/frankenstein.txt"
    content = read_file_content(file_path)
    total_words = numbers_of_words(content)
    total_characters = numbers_of_characters(content)
    total_characters_sorted = {k: v for k, v in sorted(total_characters.items(), key = lambda v: v[1], reverse = True)}
    print("--- Begin report of books/frankestein.txt ---")
    print(f"{total_words} words found in the document")
    print("\n")
    for character in total_characters_sorted:
        if character.isalpha():
            print(
                f"The {character} character was found {total_characters_sorted.get(character)} times"
            )
    print("--- End report ---")


def read_file_content(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def numbers_of_words(text):
    words = text.split()
    return len(words)


def numbers_of_characters(text):
    dictionary_of_characters = {}
    for character in text:
        char = character.lower()
        if char in dictionary_of_characters:
            dictionary_of_characters[char] += 1
        else:
            dictionary_of_characters[char] = 1
    return dictionary_of_characters


main()
